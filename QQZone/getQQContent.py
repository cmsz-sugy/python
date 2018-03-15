#coding:utf-8
import MySQLdb
import requests
import re
import datetime
from selenium import webdriver
from time import sleep
from PIL import Image

def getGTK(cookie):
    """ 根据cookie得到GTK """
    hashes = 5381
    for letter in cookie['p_skey']:
        hashes += (hashes << 5) + ord(letter)

    return hashes & 0x7fffffff




def parse_mood(i):
    '''从返回的json中，提取我们想要的字段'''
    text = re.sub('"commentlist":.*?"conlist":', '', i)
    if text:
        myMood = {}
        myMood["isTransfered"] = False
        tid = re.findall('"t1_termtype":.*?"tid":"(.*?)"', text)[0]  # 获取说说ID
        tid = qq + '_' + tid
        myMood['id'] = tid
        myMood['pos_y'] = 0
        myMood['pos_x'] = 0
        mood_cont = re.findall('\],"content":"(.*?)"', text)
        if re.findall('},"name":"(.*?)",', text):
            name = re.findall('},"name":"(.*?)",', text)[0]
            myMood['name'] = name
        if len(mood_cont) == 2:  # 如果长度为2则判断为属于转载
            myMood["Mood_cont"] = "评语:" + mood_cont[0] + "--------->转载内容:" + mood_cont[1]  # 说说内容
            myMood["isTransfered"] = True
        elif len(mood_cont) == 1:
            myMood["Mood_cont"] = mood_cont[0]
        else:
            myMood["Mood_cont"] = ""
        if re.findall('"created_time":(\d+)', text):
            created_time = re.findall('"created_time":(\d+)', text)[0]
            temp_pubTime = datetime.datetime.fromtimestamp(int(created_time))
            temp_pubTime = temp_pubTime.strftime("%Y-%m-%d %H:%M:%S")
            dt = temp_pubTime.split(' ')
            time = dt[1]
            myMood['time'] = time
            date = dt[0]
            myMood['date'] = date
        if re.findall('"source_name":"(.*?)"', text):
            source_name = re.findall('"source_name":"(.*?)"', text)[0]  # 获取发表的工具（如某手机）
            myMood['tool'] = source_name
        if re.findall('"pos_x":"(.*?)"', text):
            pos_x = re.findall('"pos_x":"(.*?)"', text)[0]
            pos_y = re.findall('"pos_y":"(.*?)"', text)[0]
            if pos_x:
                myMood['pos_x'] = pos_x
            if pos_y:
                myMood['pos_y'] = pos_y
            idname = re.findall('"idname":"(.*?)"', text)[0]
            myMood['idneme'] = idname
            cmtnum = re.findall('"cmtnum":(.*?),', text)[0]
            myMood['cmtnum'] = cmtnum
        return myMood
qq = '345281955'
headers={
'Host': 'h5.qzone.qq.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': '*/*',
    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://user.qzone.qq.com/790178228?_t_=0.22746974226377736',
    'Connection':'keep-alive'
}#伪造浏览器头
conn = MySQLdb.connect('localhost', 'jkapp', 'jkapp', 'test', charset="utf8", use_unicode=True)#连接mysql数据库
cursor = conn.cursor()#定义游标

browser = webdriver.PhantomJS(
    executable_path="D:\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")  # 这里要输入你的phantomjs所在的路径
url = "https://qzone.qq.com/"  # QQ登录网址
browser.get(url)
browser.maximize_window()  # 全屏
sleep(2)  # 等三秒
browser.get_screenshot_as_file('QR.png')  # 截屏并保存图片
im = Image.open('QR.png')  # 打开图片
im.show()  # 用手机扫二维码登录qq空间
sleep(10)  # 等二十秒，可根据自己的网速和性能修改
print(browser.title)  # 打印网页标题
cookie = {}  # 初始化cookie字典
for elem in browser.get_cookies():  # 取cookies
    cookie[elem['name']] = elem['value']
print('Get the cookie of QQlogin successfully!(共%d个键值对)' % (len(cookie)))
html = browser.page_source  # 保存网页源码
g_qzonetoken = re.search(r'window\.g_qzonetoken = \(function\(\)\{ try\{return (.*?);\} catch\(e\)',                         html)  # 从网页源码中提取g_qzonetoken
gtk = getGTK(cookie)  # 通过getGTK函数计算gtk
browser.quit()
# qzonetoken = g_qzonetoken.group(1)
# cookie,gtk,qzonetoken=login.QR_login()#通过登录函数取得cookies，gtk，qzonetoken
s=requests.session()#用requests初始化会话
params={
'uin':qq,
        'ftype':'0',
        'sort':'0',
        'pos':0,
        'num':'20',
        'replynum':'100',
        'g_tk':gtk,
        'callback':'_preloadCallback',
        'code_version':'1',
        'format':'jsonp',
        'need_private_comment':'1',
        'qzonetoken':None
        }
response=s.request('GET','https://h5.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6',params=params,headers=headers,cookies=cookie)
text=response.text#读取响应内容
if not re.search('lbs', text):#通过lbs判断此qq的说说是否爬取完毕
     print('%s说说下载完成'% qq)
textlist = re.split('\{"certified"', text)[1:]
for i in textlist:
    myMood=parse_mood(i)
    try:
        insert_sql = '''
                               insert into mood(id,content,time,sitename,pox_x,pox_y,tool,comments_num,date,isTransfered,name)
                               VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                            '''
        cursor.execute(insert_sql, (
        myMood['id'], myMood["Mood_cont"], myMood['time'], myMood['idneme'], myMood['pos_x'], myMood['pos_y'],
        myMood['tool'], myMood['cmtnum'], myMood['date'], myMood["isTransfered"], myMood['name']))
        conn.commit()
    except:
        pass


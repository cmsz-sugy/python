#encoding: utf-8
import  requests
import json
# url = 'https://www.toutiao.com/api/pc/focus/'#今日头条主页
url ='https://www.toutiao.com/api/pc/feed/?min_behot_time=0&category=%E7%BB%84%E5%9B%BE&utm_source=toutiao&widen=1&tadrequire=true&as=A105794EB526980&cp=59E5A689A890AE1'
url1='http://www.toutiao.com/api/pc/feed/?min_behot_time=0&category=%E7%BB%84%E5%9B%BE&utm_source=toutiao&widen=1&tadrequire=true&as=A185797EC5CA714&cp=59E51A07D164BE1'
url2='https://www.toutiao.com/api/comment/list/?group_id=6477495931151073550&item_id=6477503334692422157&offset=0&count=5'

def http(url,data_pa,focus_data):
    wbdata = requests.get(url).text
    data = json.loads(wbdata)
    news = data[data_pa][focus_data]
    return news

def http1(url1,data_pa):
    wbdata = requests.get(url).text
    data = json.loads(wbdata)
    news = data[data_pa]
    return news
data = 'data'
focus_data='comments'
news = http(url2,data,focus_data)
for n in news:
    title =n['text']
    # image_url=n['image_url']
    # media_url=n['media_url']
    # print title,image_url,media_url
    print title
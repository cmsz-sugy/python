#encoding: utf-8
import requests
import json
import re,sys
reload(sys)
sys.setdefaultencoding('utf-8')
def replaceCharEntity(htmlstr):
    CHAR_ENTITIES = {'nbsp': '', '160': ' ',
                     'lt': '<', '60': '<',
                     'gt': '>', '62': '>',
                     'amp': '&', '38': '&',
                     'quot': '"', '34': '"',
                      '<strong>':' ','</srong>':' '}

    re_charEntity = re.compile(r'&#?(?P<name>\w+);')
    sz = re_charEntity.search(htmlstr)
    while sz:
        entity = sz.group()  # entity全称，如>
        key = sz.group('name')  # 去除&;后entity,如>为gt
        try:
            htmlstr = re_charEntity.sub(CHAR_ENTITIES[key], htmlstr, 1)
            sz = re_charEntity.search(htmlstr)
        except KeyError:
            # 以空串代替
            htmlstr = re_charEntity.sub('', htmlstr, 1)
            sz = re_charEntity.search(htmlstr)
    return htmlstr
if __name__ == '__main__':
    url = 'https://export.focus.cn/xian/rss/zixun/14818293/?channelId=433&type=2&'
    html = requests.get(url).text
    pattern = '<p ><b>(.*)</p>'
    res = re.findall(pattern, html)
    for date in res:
        date =  content = replaceCharEntity(date)
        print date
    # url = 'https://toutiao.com/group/6480652583420559885/'
    # html = requests.get(url).text
    # pattern ='articleInfo:(.*\s.*\s.*)'
    # res = re.findall(pattern,html)
    # print type(res)
    # for new in res:
    #     pattern_title = 'title:.*'
    #     pattern_content = 'content:.*'
    #     pattern_fiter = '<p>.*?</p>'
    #     res_title = re.findall(pattern_title, new)
    #     res_content = re.findall(pattern_content, new)
    #     for title in res_title:
    #        print title
    #     for content in  res_content:
    #         content = replaceCharEntity(content)
    #         content_filter = re.findall(pattern_fiter,content)
    #         for content_filter in content_filter:
    #             # print content_filter
    #             replace = content_filter.replace("<p>","")
    #             replace = replace.replace("</p>", "")
    #             replace = replace.replace("<strong>", "")
    #             replace = replace.replace("</strong>", "")
    #             print replace

    # dic1 = {"type": "dic1", 'username': 'loleina', 'age': 16}
    # jsonSource = {"count":8,"sub_images":[{"url":"\/\/p3.pstatp.com\/origin\/3a05000282ecf7dfad9d"},{"url_1":"\/\/p3.pstatp.com\/origin\/3a05000282ecf7dfad9d"}]}
    # jsonSource_1 =  {"count":8,"sub_images":[{"url":"\/\/p3.pstatp.com\/origin\/3a05000282ecf7dfad9d","width":1047,"url_list":[{"url":"http:\/\/p3.pstatp.com\/origin\/3a05000282ecf7dfad9d"},{"url":"http:\/\/pb9.pstatp.com\/origin\/3a05000282ecf7dfad9d"},{"url":"http:\/\/pb1.pstatp.com\/origin\/3a05000282ecf7dfad9d"}],"uri":"origin\/3a05000282ecf7dfad9d","height":648},{"url":"\/\/p1.pstatp.com\/origin\/3a0700026b5ce76ad651","width":1021,"url_list":[{"url":"http:\/\/p1.pstatp.com\/origin\/3a0700026b5ce76ad651"},{"url":"http:\/\/pb3.pstatp.com\/origin\/3a0700026b5ce76ad651"},{"url":"http:\/\/pb9.pstatp.com\/origin\/3a0700026b5ce76ad651"}],"uri":"origin\/3a0700026b5ce76ad651","height":688},{"url":"\/\/p3.pstatp.com\/origin\/3a06000279f1012d0108","width":1062,"url_list":[{"url":"http:\/\/p3.pstatp.com\/origin\/3a06000279f1012d0108"},{"url":"http:\/\/pb9.pstatp.com\/origin\/3a06000279f1012d0108"},{"url":"http:\/\/pb1.pstatp.com\/origin\/3a06000279f1012d0108"}],"uri":"origin\/3a06000279f1012d0108","height":768},{"url":"\/\/p1.pstatp.com\/origin\/3a0900024ed44580b7f6","width":923,"url_list":[{"url":"http:\/\/p1.pstatp.com\/origin\/3a0900024ed44580b7f6"},{"url":"http:\/\/pb3.pstatp.com\/origin\/3a0900024ed44580b7f6"},{"url":"http:\/\/pb9.pstatp.com\/origin\/3a0900024ed44580b7f6"}],"uri":"origin\/3a0900024ed44580b7f6","height":598},{"url":"\/\/p3.pstatp.com\/origin\/3a0900024ed6467c9797","width":980,"url_list":[{"url":"http:\/\/p3.pstatp.com\/origin\/3a0900024ed6467c9797"},{"url":"http:\/\/pb9.pstatp.com\/origin\/3a0900024ed6467c9797"},{"url":"http:\/\/pb1.pstatp.com\/origin\/3a0900024ed6467c9797"}],"uri":"origin\/3a0900024ed6467c9797","height":771},{"url":"\/\/p3.pstatp.com\/origin\/3afb00008986b57c46da","width":1045,"url_list":[{"url":"http:\/\/p3.pstatp.com\/origin\/3afb00008986b57c46da"},{"url":"http:\/\/pb9.pstatp.com\/origin\/3afb00008986b57c46da"},{"url":"http:\/\/pb1.pstatp.com\/origin\/3afb00008986b57c46da"}],"uri":"origin\/3afb00008986b57c46da","height":776},{"url":"\/\/p9.pstatp.com\/origin\/3afb000089873f33de27","width":1057,"url_list":[{"url":"http:\/\/p9.pstatp.com\/origin\/3afb000089873f33de27"},{"url":"http:\/\/pb1.pstatp.com\/origin\/3afb000089873f33de27"},{"url":"http:\/\/pb3.pstatp.com\/origin\/3afb000089873f33de27"}],"uri":"origin\/3afb000089873f33de27","height":773},{"url":"\/\/p1.pstatp.com\/origin\/3a0800027d7cd7ada957","width":1049,"url_list":[{"url":"http:\/\/p1.pstatp.com\/origin\/3a0800027d7cd7ada957"},{"url":"http:\/\/pb3.pstatp.com\/origin\/3a0800027d7cd7ada957"},{"url":"http:\/\/pb9.pstatp.com\/origin\/3a0800027d7cd7ada957"}],"uri":"origin\/3a0800027d7cd7ada957","height":759}],"max_img_width":1062,"labels":["\u65b0\u80fd\u6e90\u6c7d\u8f66","\u6bd4\u4e9a\u8fea","\u6bd4\u4e9a\u8feaE6","\u56fd\u4ea7\u8f66","SUV"],"sub_abstracts":["\u6bd4\u4e9a\u8fea-E6","\u5916\u89c2\uff1b\u662f\u6bd4\u4e9a\u8fea\u81ea\u4e3b\u7814\u53d1\u7684\u4e00\u6b3e\u7eaf\u7535\u52a8crossover\uff0c\u5b83\u517c\u5bb9\u4e86SUV\u548cMPV\u7684\u8bbe\u8ba1\u7406\u5ff5\u3002","\u4e2d\u63a7\uff1b\u662f\u4e00\u6b3e\u6027\u80fd\u826f\u597d\u7684\u8de8\u754c\u8f66\uff0c\u7eed\u9a76\u91cc\u7a0b\u8d85\u8fc7300Km\uff0c\u4e3a\u540c\u7c7b\u8f66\u578b\u4e4b\u51a0\u3002","\u4e2d\u63a7\uff1b\u52a8\u529b\u7535\u6c60\u548c\u542f\u52a8\u7535\u6c60\u5747\u91c7\u7528\u6bd4\u4e9a\u8fea\u81ea\u4e3b\u7814\u53d1\u751f\u4ea7\u7684ET-POWER\u94c1\u7535\u6c60\uff0c\u4e0d\u4f1a\u5bf9\u73af\u5883\u9020\u6210\u4efb\u4f55\u5371\u5bb3\u3002\n","\u5ea7\u6905\uff1b\u53ef\u4f7f\u7528220V\u6c11\u7528\u7535\u6e90\u6162\u5145\uff0c\u5feb\u5145\u4e3a3C\u5145\u7535\uff0c15\u5206\u949f\u5de6\u53f3\u53ef\u5145\u6ee1\u7535\u6c6080%\u3002","\u5ea7\u6905","\u7ec6\u8282","\u7ec6\u8282"],"sub_titles":["\u6c7d\u8f66\u56fe\u96c6\uff1a\u6bd4\u4e9a\u8fea-E6","\u6c7d\u8f66\u56fe\u96c6\uff1a\u6bd4\u4e9a\u8fea-E6","\u6c7d\u8f66\u56fe\u96c6\uff1a\u6bd4\u4e9a\u8fea-E6","\u6c7d\u8f66\u56fe\u96c6\uff1a\u6bd4\u4e9a\u8fea-E6","\u6c7d\u8f66\u56fe\u96c6\uff1a\u6bd4\u4e9a\u8fea-E6","\u6c7d\u8f66\u56fe\u96c6\uff1a\u6bd4\u4e9a\u8fea-E6","\u6c7d\u8f66\u56fe\u96c6\uff1a\u6bd4\u4e9a\u8fea-E6","\u6c7d\u8f66\u56fe\u96c6\uff1a\u6bd4\u4e9a\u8fea-E6"]}
    # json_dic1 = json.dumps(jsonSource_1)
    # json_data = json.loads(json_dic1)
    # json_dic1 = json_data['sub_abstracts']
    # for json_dic in json_dic1:
    #      print json_dic.decode('unicode-escape').encode('utf-8')#十六进制转化为汉字

    # json_dic2 = json.dumps(dic1, sort_keys=True, indent=4, separators=(',', ': '), encoding="gbk", ensure_ascii=True)
    # print json_dic2
    # SecHalf = ''
    # http = ''
    # url ='http://www.toutiao.com/a6465951049604661774'
    # index = url.index(':')
    # SecHalf += url[index:len(url)]
    # http  += url[0:index]
    # s= 's'
    # https =http+s;
    # httpsUrl =(https+SecHalf)
    # print httpsUrl

    # try:
    #     response = requests.get(url)
    #     if response.status_code == 200:
    #         print response.text
    # except RequestException:
    #     print('请求详情页出错', url)
    # jsonSource ='{"count":8,"sub_images":[{"url":"\/\/p3.pstatp.com\/origin\/3a05000282ecf7dfad9d","width":1047,"url_list":[{"url":"http:\/\/p3.pstatp.com\/origin\/3a05000282ecf7dfad9d"}]}'
    # jsonSource = {"count":8,"sub_images":"123"}
    # news =  json.dumps(jsonSource)
    # new = json.load(news)
    # data  = new['count']
    # print data
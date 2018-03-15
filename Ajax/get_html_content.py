#encoding: utf-8
import requests
import json
import re,sys
reload(sys)
sys.setdefaultencoding('utf-8')
def replaceCharEntity(htmlstr):
    CHAR_ENTITIES = {'nbsp': ' ', '160': ' ',
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
def print_content(url):
    url = http_convert_https(url)
    html = requests.get(url).text
    pattern = 'articleInfo:(.*\s.*\s.*)'
    res = re.findall(pattern, html)
    print type(res)
    for new in res:
        pattern_title = 'title:.*'
        pattern_content = 'content:.*'
        pattern_fiter = '<p>.*?</p>'
        res_title = re.findall(pattern_title, new)
        res_content = re.findall(pattern_content, new)
        for title in res_title:
            print title
        for content in res_content:
            content = replaceCharEntity(content)
            content_filter = re.findall(pattern_fiter, content)
            for content_filter in content_filter:
                # print content_filter
                replace = content_filter.replace("<p>", "")
                replace = replace.replace("</p>", "")
                replace = replace.replace("<strong>", "")
                replace = replace.replace("</strong>", "")
                print replace
def http_convert_https(url):
    SecHalf = ''
    http = ''
    index = url.index(':')
    SecHalf += url[index:len(url)]
    http += url[0:index]
    s = 's'
    https = http + s;
    httpsUrl = (https + SecHalf)
    return  httpsUrl
def get_not_toutiao_content(url):
    # url = http_convert_https(url)
    html = requests.get(url).text
    pattern = '<p ><b>(.*)</p>'
    res = re.findall(pattern, html)
    for date in res:
        date =  content = replaceCharEntity(date)
        print date
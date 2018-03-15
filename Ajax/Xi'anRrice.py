# encoding:utf-8

import urllib
import requests
import json
import sys
import get_html_content
from requests.exceptions import RequestException
reload(sys)
sys.setdefaultencoding('utf-8')
def get_inde_page():
    data ={
        'count': 20,
        'keyword': u'西安房价',
        'format':'json',
        'cur_tab': 1,
        'autoload': 'ture',
        'offset': 0
    }
    print sys.getdefaultencoding()
    param = urllib.urlencode(data)
    base_url = 'https://www.toutiao.com/search_content/?'
    url = base_url +param
    return url
def get_detail_page(url):
    Reponse_json = json.loads(url)
    data = Reponse_json['data']
    for data_new in data:
        if data_new.has_key('article_url'):
            print data_new['article_url']
            data_new = data_new['article_url']
            if data_new.find('toutiao') > 0:
              get_html_content.print_content(data_new)
              print '========================================================'
            if data_new.find('toutiao') < 0:
                get_html_content.get_not_toutiao_content(data_new)
                print '========================================================'
        # print data_new.decode('unicode-escape').encode('utf-8')
if __name__ == '__main__':
    try:
        headers = {'content-type': 'application/x-www-form-urlencoded',
                   'X-Requested-With':'XMLHttpRequest',
                   'Host':'www.toutiao.com',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
        url = get_inde_page()
        reponse = requests.get(url,headers=headers)
        # print reponse.text
        if reponse.status_code == 200:
            print '网页请求成功'
            get_detail_page(reponse.text)
        else:print 'request errer'
    except RequestException:
        print('请求索引页出错', url)






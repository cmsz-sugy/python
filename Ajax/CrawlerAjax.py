#encoding: utf-8

import os
import re
from multiprocessing import Pool
from hashlib import md5
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import requests
import json
import urllib

# 获取索引页
def get_index_page(offset, keyword):
    # Ajax请求参数
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': '%E8%A1%97%E6%8B%8D',
        'autoload': 'true',
        'count': '20',
        'cur_tab': 3
    }
    params = urllib.urlencode(data)
    base = 'https://www.toutiao.com/search_content/'
    url = base + '?' + params
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引页出错', url)
        return None


# 解析索引页
def parse_index_page(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')


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

# 获取详情页
def get_detail_page(url):
    try:
        url = http_convert_https(url)
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求详情页出错', url)
        return None


# 解析详情页
def parse_detail_page(html, url):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select('title')[0].get_text()
    pattern ='gallery:+(.*).*'
    res = re.findall(pattern,html)
    for info in res:
        index = info.find('},')
        info = info[0:index+1]
        print info

    print 1
    # images_pattern = re.compile('gallery:+(.*);', re.S)
    # result = re.search(images_pattern, html)
    # print result.group(0)
    # if result:
    #     data = json.loads(result.group(0))
    #     if data and 'sub_images' in data.keys():
    #         sub_images = data.get('sub_images')
    #         images = [image.get('url') for image in sub_images]
    #         res = {
    #             'title': title,
    #             'url': url,
    #             'images': images
    #         }
    #         print(res)
    #         for image in images:
    #             download_image(image)
    #         return res


# 下载图片
def download_image(url):
    print('downloading', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # content和text的区别：content返回二进制内容
            save_image(response.content)
        return None
    except RequestException:
        print('请求图片出错', url)
        return None


# 保存图片
def save_image(content):
    file_path = '{0}/{1}.{2}'.format(os.getcwd(), md5(content).hexdigest(), 'jpg')
    if not os._exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)
            f.close()


def main(offset):
    html = get_index_page(offset, KEYWORD)
    urls = parse_index_page(html)
    for url in urls:
        html = get_detail_page(url)
        res = parse_detail_page(html, url)

KEYWORD = '街拍'
if __name__ == '__main__':
    main(0)

# 开启多线程
# 指定搜索的参数offset范围为[GROUP_START*20,(GROUP_END+1)*20]
GROUP_START = 1
GROUP_END = 5
# 搜索关键字，可以改变


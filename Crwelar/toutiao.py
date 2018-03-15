#encoding:utf-8
import requests

import HTTP

base_url = 'https://www.toutiao.com'
data ='data'
pc_feed_focus ='pc_feed_focus'
url = 'https://www.toutiao.com/api/pc/focus/'#今日头条主页
news = HTTP.http2(url, data, pc_feed_focus)
for new in news:
   display_url = new['display_url']
   sec_url = base_url+display_url
   sec_data =requests.get(sec_url).text
   print sec_data
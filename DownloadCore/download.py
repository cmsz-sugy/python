#coding:utf-8

import urlparse
import urllib2
import random
import time
from datetime import  datetime,timedelta
import socket
import Throttle

DEFAULT_AGENT = 'wswp'
DEFAULT_DELAY = 5
DEFAULT_RETRIES = 1
DEFAULT_TIMEOUT = 60
class Downloader:
    def __init__(self,delay=DEFAULT_DELAY,user_agent=DEFAULT_AGENT,proxies=None,num_reties =DEFAULT_RETRIES,
                 timeout = DEFAULT_TIMEOUT,opener=None,cache= None):
        socket.setdefaulttimeout(timeout)
        self.throttle = user_agent
        self.user_agent = user_agent
        self.proxies =proxies
        self.num_retried = num_reties
        self.opener = opener
        self.cache = cache

    def __call__(self, url):
        '''
        先从缓存中取出该url对应的数据，如果缓存中有该数据则不必下载也不必限速
         如果缓存中没有该数据，则需要重新下载，并且下载前需要限速throttle
        '''
        result = None
        if self.cache:
            try:
                result = self.cache[url]
            except KeyError:
                # 如果这个url不在缓存中
                pass
            else:
                if self.num_retries > 0 and 500 <= result['code'] < 600:
                    # 如果有服务器错误，说明之前缓存的数据有误不可用
                    #并且num_retries>0,则重新下载
                    result = None
        if result is None:
            # 此时才是真正发生下载，不是从缓存中下载获取，故需要限速，防止被封
            self.throttle =Throttle.wait(self,url)
            proxy = random.choice(self.proxies) if self.proxies else None
            headers = {'User-agent': self.user_agent}
            self.num_retries =1
            result = self.download(url, headers, proxy=proxy, num_retries=self.num_retries)
            if self.cache:
                # 把下载得到的html网页存进缓存中
                self.cache[url] = result
        return result['html']

    def download(self, url, headers, proxy, num_retries, data=None):
        print 'Downloading:', url
        request = urllib2.Request(url, data, headers or {})
        opener = self.opener or urllib2.build_opener()
        if proxy:
            proxy_params = {urlparse.urlparse(url).scheme: proxy}
            opener.add_handler(urllib2.ProxyHandler(proxy_params))
        try:
            response = opener.open(request)
            html = response.read()
            code = response.code
        except Exception as e:
            print 'Download error:', str(e)
            html = ''
            if hasattr(e, 'code'):
                code = e.code
                if num_retries > 0 and 500 <= code < 600:
                    # 服务器错误，并且下载num_retries>0,需重新下载
                    return self._get(url, headers, proxy, num_retries - 1, data)
            else:
                code = None
        ##返回html同时，也返回其HTTP状态码用来检查该html可用不可用
        return {'html': html, 'code': code}


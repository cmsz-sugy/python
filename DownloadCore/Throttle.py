#coding:utf-8
import urlparse
import urllib2
import random
import time
from datetime import  datetime,timedelta
import socket
# """
#    爬虫速度过快，可能会造成服务器过载，或者是ip地址被封，为了避免这个问题，我们的爬虫将会设置一个delay标识，
#    用于设定请求同一域名时最小时间间隔。注意是同一域名。
#    爬取同一域名下不同网页时，需要注意两次下载之间至少需要1秒钟的间隔。
#    """


def __init__(self, delay):
    # amount of delay between downloads for each domain
    self.delay = delay
    # timestamp of when a domain was last accessed
    self.domains = {}


def wait(self, url):
    """Delay if have accessed this domain recently
    """
    domain = urlparse.urlsplit(url).netloc
    last_accessed = self.domains.get(domain)
    if self.delay > 0 and last_accessed is not None:
        sleep_secs = self.delay - (datetime.now() - last_accessed).seconds
        if sleep_secs > 0:
            time.sleep(sleep_secs)
    self.domains[domain] = datetime.now()
#coding:utf-8
import os
import re
import urlparse
import shutil
import zlib
from datetime import datetime, timedelta

try:
    import cPickle as pickle
except ImportError:
    import pickle
from link_crawler import link_crawler


class DiskCache:

    def __init__(self, cache_dir='cache', expires=timedelta(days=30), compress=True):
        """
        cache_dir: 数据缓存的根目录地址
        expires: 若缓存数据的存储时间超过expires，则文件失效，将其删除
        compress: 布尔变量，是否将数据压缩存进缓存
        """
        self.cache_dir = cache_dir
        self.expires = expires
        self.compress = compress

    def __getitem__(self, url):
        """
        由url，从硬盘加载数据
        """
        path = self.url_to_path(url) ##由url映射出其存储地址
        if os.path.exists(path):
            with open(path, 'rb') as fp:
                data = fp.read()
                if self.compress:
                    data = zlib.decompress(data)
                result, timestamp = pickle.loads(data)
                if self.has_expired(timestamp): ##查看加载出的数据是否已经过期
                    raise KeyError(url + ' has expired')
                return result
        else:
            # 该url数据还没有被加载到缓存
            raise KeyError(url + ' does not exist')

    def __setitem__(self, url, result):
        """Save data to disk for this url
        """
        path = self.url_to_path(url)
        folder = os.path.dirname(path)
        if not os.path.exists(folder):
            os.makedirs(folder)

        ## 将该url对应数据以及当前时间存进本地磁盘内，将时间存进为后期检查是否已经过期
        ##将输入数据转化为字符串，然后保存到磁盘
        data = pickle.dumps((result, datetime.utcnow()))
        if self.compress: ##是否对数据进行压缩存储
            data = zlib.compress(data)
        with open(path, 'wb') as fp:
            fp.write(data)

    def __delitem__(self, url):
        """Remove the value at this key and any empty parent sub-directories
        """
        path = self._key_path(url)
        try:
            os.remove(path)
            os.removedirs(os.path.dirname(path))
        except OSError:
            pass

    def url_to_path(self, url):
        """
        根据url创建一个本地文件，用来存储该url对应的数据
        """
        components = urlparse.urlsplit(url)
        # when empty path set to /index.html
        path = components.path
        if not path:
            path = '/index.html'
        elif path.endswith('/'):
            path += 'index.html'

        filename = components.netloc + path + components.query
        # 将除数字，字母和基本符号外的其他符号用"_"代替
        filename = re.sub('[^/0-9a-zA-Z\-.,;_ ]', '_', filename)
        # 每个目录限制在255个字符内
        filename = '/'.join(segment[:255] for segment in filename.split('/'))

        return os.path.join(self.cache_dir, filename) ##cache_dir/filename

    def has_expired(self, timestamp):
        """
        查看缓存文件是否已经过期
        """
        return datetime.utcnow() > timestamp + self.expires

    def clear(self):
        """Remove all the cached values
        """
        if os.path.exists(self.cache_dir):
            shutil.rmtree(self.cache_dir)


if __name__ == '__main__':
    cache = DiskCache()
    cache.clear()
    link_crawler('https://example.webscraping.com/', '/(index|view)', cache=DiskCache())
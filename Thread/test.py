#coding=utf-8
import requests
import time
from threading import Thread
from multiprocessing import Process
def count(x, y):
    # 使程序完成150万计算
    c = 0
    while c < 500000:
        c += 1
        x += x
        y += y


def write():
    f = open("test.txt", "w")
    for x in range(5000000):
        f.write("testwrite\n")
    f.close()


def read():
    f = open("test.txt", "r")
    lines = f.readlines()
    f.close()# CPU密集操作
_head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
url = "https://www.tieba.com"
def http_request():
    try:
        webPage = requests.get(url, headers=_head)
        html = webPage.text
        return {"context": html}
    except Exception as e:
        return {"error": e}



t = time.time()
for x in range(10):
    count(1, 1)
print("Line cpu", time.time() - t)

# IO密集操作
t = time.time()
for x in range(10):
    write()
    read()
print("Line IO", time.time() - t)

# 网络请求密集型操作
t = time.time()
for x in range(10):
    http_request()
print("Line Http Request", time.time() - t)

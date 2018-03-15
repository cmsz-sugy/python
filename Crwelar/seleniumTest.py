#coding:utf-8
import unittest
from selenium import webdriver
from bs4 import BeautifulSoup
class seleniumTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS(executable_path='D:\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')

    def testEle(self):
        driver = self.driver
        driver.get('http://www.toutiao.com/a6375738133513765122/')
        # print driver.page_source
        soup = BeautifulSoup(driver.page_source, 'xml')
        titles = soup.find_all('title')
        for title in titles:
             print title.text
        # while True:
        #     titles = soup.find_all('title')
        #     nums = soup.find_all('span', {'class': 'dy-num fr'})
        #     for title, num in zip(titles, nums):
        #         print title.get_text(), num.get_text()
        #     if driver.page_source.find('shark-pager-disable-next') != -1:
        #         break
        #     elem = driver.find_element_by_class_name('shark-pager-next')
        #     elem.click()
        #     soup = BeautifulSoup(driver.page_source, 'xml')

    def tearDown(self):
        print 'down'

if __name__ == "__main__":
    unittest.main()

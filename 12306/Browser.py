# encoding :utf-8
from splinter import Browser


def main():
    browser = Browser(driver_name="chrome")
    browser.visit('https://www.baidu.com')


#     browser.fill('q', 'splinter - python acceptance testing for web applications')
#     button = browser.find_by_name('btnK')
#     button.click()

#     if browser.is_text_present('splinter.cobrateam.info'):
#         print 'yes, the official website was found!'
#     else:
#         print "No, it wasn't found... We need o improve our SEO techniques"
#

#     browser.quit()


if __name__ == '__main__':
    main()
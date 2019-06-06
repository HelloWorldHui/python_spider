#
# from selenium import webdriver
# import time
#
# # phantomjs路径
# path = r'D:\yuan\phantomjs-2.1.1-windows\bin\phantomjs'
# browser = webdriver.PhantomJS(path)
#
# # 打开百度
# url = 'http://www.baidu.com/'
# browser.get(url)
#
# time.sleep(1)
#
# browser.save_screenshot(r'baidu.png')
#
# # 查找input输入框
# my_input = browser.find_element_by_id('kw')
# # 往框里面写文字
# my_input.send_keys('美女')
# time.sleep(3)
# #截屏
# browser.save_screenshot(r'meinv.png')
# # 查找搜索按钮
# button = browser.find_elements_by_class_name('s_btn')[0]
# button.click()
# time.sleep(1)
# browser.save_screenshot(r'show.png')
# time.sleep(1)
# browser.quit()

################################################ 案例 ##########################################################

from selenium import webdriver
from time import sleep
import time

if __name__ == '__main__':
    url = 'https://movie.douban.com/typerank?type_name=%E6%81%90%E6%80%96&type=20&interval_id=100:90&action='
    # 发起请求前，可以让url表示的页面动态加载出更多的数据
    path = r'D:\yuan\phantomjs-2.1.1-windows\bin\phantomjs'
    # 创建无界面的浏览器对象
    bro = webdriver.PhantomJS(path)
    # 发起url请求
    bro.get(url)
    time.sleep(2)
    # 截图
    bro.save_screenshot('1.png')

    # 执行js代码（让滚动条向下偏移n个像素（作用：动态加载了更多的电影信息））
    js = 'window.scrollTo(0,document.body.scrollHeight)'
    bro.execute_script(js)  # 该函数可以执行一组字符串形式的js代码
    time.sleep(2)

    bro.execute_script(js)  # 该函数可以执行一组字符串形式的js代码
    time.sleep(2)
    bro.save_screenshot('2.png')
    time.sleep(2)
    # 使用爬虫程序爬去当前url中的内容
    html_source = bro.page_source # 该属性可以获取当前浏览器的当前页的源码（html）
    print(html_source)
    with open('new_source.html', 'w',encoding="utf8") as fp:
        fp.write(html_source)
    bro.quit()
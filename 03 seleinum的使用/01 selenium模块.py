from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
# ################################## 1 简单使用 # ##################################
# 用get打开百度页面
driver.get("http://www.baidu.com")
input=driver.find_element_by_id("kw")
input.send_keys("美女")
sleep(2)
# input.send_keys(Keys.ENTER)
search=driver.find_element_by_id("su")
search.click()
#
# ################################## 2 元素定位方法 # ##################################
# # search.find_element_by_class_name()
# # search.find_element_by_name()
# # search.find_element_by_link_text()
# # search.find_element_by_partial_link_text()
# # search.find_element_by_css_selector(".c1 p")
# # search.find_element_by_xpath("//*[@id=i1]/a")
#
# # 结果是一个列表
# search.find_elements_by_class_name()
    ################  隐式等待:在查找所有元素时，如果尚未被加载，则等10秒
# driver.implicitly_wait(10)

###############   显示等待
from selenium.webdriver.common.by import By #按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys #键盘按键操作
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
#显式等待：显式地等待某个元素被加载
wait=WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.ID,'content_left')))

content_left=driver.find_element_by_id("content_left")

#################  节点信息
print(content_left.tag_name) # div
print(content_left.get_attribute("id"))
print(content_left.size) # {'height': 1453, 'width': 661}
print(content_left.location) # {'x': 0, 'y': 133}
driver.close()
######################################### 3节点交互 ###########################
# driver.get("https://www.jd.com/")
#
# # 节点定位:搜索框标签
# input=driver.find_element_by_id("key")
# input.send_keys("MAC")
# sleep(2)
# input.clear()
# input.send_keys("西游记")
# sleep(1)
# input.send_keys(Keys.ENTER)
#
# driver.close()


################################# 4 动作链 #####################################

# from selenium.webdriver import ActionChains
# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# # actions.drag_and_drop(source, target)
# actions.click_and_hold(source).perform()
# sleep(1)
# actions.move_to_element(target).perform()
# sleep(1)
# actions.move_by_offset(xoffset=50,yoffset=0).perform()
#
# actions.release()
# browser.close()

#################################### 5 执行JavaScript ##########################


# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('https://www.jd.com/')
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("123")')

#####################################  cookie ##############################
# from selenium import webdriver

#
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())


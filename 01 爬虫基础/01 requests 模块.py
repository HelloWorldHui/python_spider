import requests


######################################基本请求####################################################
# url="https://www.jd.com/"
# res=requests.get(url)
#
# with open("jd.html","w",encoding="utf8") as f:
#     f.write(res.text)

######################################含参数，请求头####################################################
# 1 爬取百度搜索
# url="https://www.baidu.com/s"
# res=requests.get(url,
#                  params={
#                  "wd":"刘传盛"
#                         }
#                  ,headers={
#                             "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
#                         })
#
# with open("baidu.html","wb") as f:
#     f.write(res.content)

# 2 爬取抽屉网
# url="https://dig.chouti.com/"
# res=requests.get(url,headers={
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
# })
#
# with open("chouti.html","wb") as f:
#     f.write(res.content)
######################################cookie参数####################################################

# import uuid
# import requests
#
# url = 'http://httpbin.org/cookies'
# cookies = {"sbid":str(uuid.uuid4()),"a":"1"}
#
# res = requests.get(url, cookies=cookies)
# print(res.text)

######################################  session 对象######################################
# res=requests.post("/login/")
# dic={}
# requests.get("/index/",cookies=dic)
# ########
# session=requests.session()
# session.post("/login/")
# session.get("/index/")

######################################### post请求 ########################################


# requests.post(url="/login/",headers={},cookies={},params={"next":"index"},data={},json={})

import requests

# res1 = requests.post(url='http://httpbin.org/post?a=1',
#                      data={'name': 'yuan'})  # 没有指定请求头,#默认的请求头:application/x-www-form-urlencoed
# print(res1.text)

# res2 = requests.post(url='http://httpbin.org/post',data={"name":"alex"})  # 默认的请求头:application/json
# print(res2.text)


###################################### IP代理

res=requests.get('http://httpbin.org/ip', proxies={'http':'111.177.177.87:9999'}).json()
print(res)

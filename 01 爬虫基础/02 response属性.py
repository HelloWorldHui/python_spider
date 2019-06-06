

import requests

#####################################################  content text ##################################
response=requests.get("https://www.autohome.com.cn/beijing/")
#################### 爬取文件方式1
# print(response.content)
# print(response.encoding)
# print(response.text)
# response.encoding="gbk"
# with open("autohome.html","w") as f:
#     f.write(response.text)

#################### 爬取文件方式2
# with open("autohome.html","wb") as f:
#     f.write(response.content)

#################### 爬取图片，音频，视频

# res=requests.get("https://b-ssl.duitang.com/uploads/item/201602/20/20160220095515_ya4YU.thumb.700_0.jpeg")
# with open("heben.jpeg","wb") as f:
#     f.write(res.content)

# res=requests.get("http://y.syasn.com/p/p95.mp4")
# with open("xiaoshipin.mp4","wb") as f:
#     for line in res.iter_content():
#         f.write(line)

####################  响应json数据

# res=requests.get("http://httpbin.org/get")
# print(res.text)
# print(type(res.text))
# import json
# print(json.loads(res.text))
# print(type(json.loads(res.text)))
# print("-----")
# print(res.json())
# print(type(res.json()))

######################### 重定向

# res=requests.get("http://www.jd.com/")
# print(res.history) # [<Response [302]>]
# print(res.text)
# print(res.status_code) # 200

# res=requests.get("http://www.jd.com/",allow_redirects=False)
# print(res.history) # [<Response [302]>]
# print(res.status_code) # 200



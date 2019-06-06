
import requests
import re

session=requests.session()

# login请求：目的获取动态token值
res1=session.get("https://github.com/login")
token=re.findall('<input type="hidden" name="authenticity_token" value="(.*?)" />',res1.text,re.S)[0]
print(token)


res2=session.post("https://github.com/session",data={
        "commit": "Sign in",
        "utf8":"✓",
        "authenticity_token": token,
        "login": "yuanchenqi0316@163.com",
        "password": "yuanchenqi0316"
})

# res=requests.get("https://github.com/settings/emails")

with open("github.html","wb") as f:
    f.write(res2.content)

print(res2.history)
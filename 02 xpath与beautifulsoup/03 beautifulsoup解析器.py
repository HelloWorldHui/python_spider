

from bs4 import BeautifulSoup

html_doc ="""
<html><head><title>The Dormouse's story</title></head>
<body>

<div class="c1">
   <p>123</p>
   <p>345</p>
   <div>
     <a>111</a>
    </div>
</div>

<p id="my p" class="title"><b id="bbb" class="boldest">The Dormouse's story</b><span>123</span></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup=BeautifulSoup(html_doc,"lxml")

# 查找第一个a标签对象
# print(soup.a)
# print(type(soup.a)) # <class 'bs4.element.Tag'>
################################################### 一 Tag对象的操作 ###################################################
##################### 属性操作
# print(soup.a.attrs) # {'href': 'http://example.com/elsie', 'class': ['sister'], 'id': 'link1'}
# print(soup.a.attrs["href"])
# print(soup.a.attrs["class"])
# print(soup.a.attrs.get("id"))
# #  简单写法
# print(soup.a["href"]) # http://example.com/elsie
##################### 文本操作
# print(soup.a.text) # Elsie
# print(soup.a.get_text()) # Elsie
# print(soup.a.string)  # Elsie
# print(soup.p.text)   # The Dormouse's story123
# print(soup.p.string) # None

################################################ 二 find，find_all()###########################################

################################################ 2.1 find_all()

# print(soup.find_all('a'))
# for link in soup.find_all("a"):
#     print(link["href"],link['class'])

################## 2.1.1 name参数：四种name过滤器

# print(soup.find_all("a"))  # name="a"
# print(soup.find_all(["a","b"])) # name=["a","b"]
# import re
# print(soup.find_all(re.compile('^b'))) # name=re.compile('^b')   找出b开头的标签，结果有body和b标签
# def has_class_but_no_id(tag):
#     return tag.has_attr('class') and not tag.has_attr('id')
# print(soup.find_all(has_class_but_no_id)) # name=has_class_but_no_id

################## 2.1.2 属性参数

# print(soup.find_all("a",attrs={"class":"sister","id":"link2"}))
# 简写
# print(soup.find_all('a',id="link3"))
# print(soup.find_all('a',class_="sister"))

################## 2.1.3 文本参数
# print(soup.find_all("a",text="Elsie"))

################## 2.1.4 limit参数
# print(soup.find_all("a",limit=2))

################## 2.1.5 recursive参数
# print(soup.find_all(recursive=False))
#  局部查找
# print(soup.div.find_all(recursive=False))

################################################ 2.2 find()

# print(soup.find("a")) # 等同于 soup.a
#  find参数和find_all完全一样

################################################ 三 selector ##################################################

#  这个selector等同于css选择器

# print(soup.select(".sister"))
# print(soup.select("#link2"))
# print(soup.select(".c1 a"))

# 今日作业：# 爬取58二手房  解析器：xpath或者BS
            # crm整理



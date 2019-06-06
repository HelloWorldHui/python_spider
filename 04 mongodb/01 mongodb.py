import pymongo


# 1 连接mongo数据库
client = pymongo.MongoClient(host='localhost', port=27017)

# 2 获取数据库以及集合
db=client.spider
collection = db.students

################################ 添加文档 ############################
# 3 添加一个文档
# student = {
#     'id': '20100101',
#     'name': 'Yuan',
#     'age': 20,
#     'gender': 'male'
# }
# 方式1:
#result = collection.insert_one(student)
#print(result)
# 方式2:
# obj=collection.save(student)

# 3 添加多个文档
# student1 = {
#     'id': '20170104',
#     'name': 'Amy',
#     'age': 20,
#     'gender': 'male'
# }
#
# student2 = {
#     'id': '20170202',
#     'name': 'Mike',
#     'age': 21,
#     'gender': 'male'
# }
#
# result = collection.insert_many([student1, student2])
# print(result)

################################ 查询文档 ############################

# results=collection.find({"age":{"$gt":20}})
# print('results',results)

# 计数
# print(collection.find({'age': 20}).count())

# 排序
# results = collection.find().sort([('age',pymongo.ASCENDING),("_id",pymongo.DESCENDING)])

# 分页
# results = collection.find().sort('age', pymongo.ASCENDING).skip(2).limit(2)
# for obj in results:
#     print(obj["name"],obj["age"])

################################ 更新文档 ############################
# 覆盖更新
# collection.update({"name":"Mike"},{"xxx":'yyy'})
# 局部更新
# collection.update({"name":"Amy"},{"$set":{"age":100}})
# collection.update_many({},{"$inc":{"age":20}})

################################ 删除文档 ############################
# result = collection.remove({'name': 'Amy'})
# # print(result)
# # result = collection.delete_many({'age': {'$lt': 25}})

# -*- coding:utf-8 -*-
import pymongo
conn  = pymongo.MongoClient('localhost',27017)
db = conn.mydb  #连接mydb数据库，没有则自动创建
my_set = db.test_set  #使用test_set集合，没有则自动创建
#my_set.insert({"name":"zhangsan","age":18})
my_set.update({'name':'zhangsan'},{'$set':{'age':28}})
for i in my_set.find():
    print(i)
for i in my_set.find({"name":"zhangsan"}):
    print(i)
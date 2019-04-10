#coding=utf8
import redis
# r = redis.Redis(host='127.0.0.1',port=6379)
# r.set('name','root')

pool = redis.ConnectionPool(host='127.0.0.1',port=6379)
r = redis.Redis(connection_pool=pool)

def setName(name,val):
    r.set(name,val)
def getName(name):
    return r.get(name)

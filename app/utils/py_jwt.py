#coding=utf8
import jwt
import time
import datetime
import json

token = jwt.encode({"name":"lls"},'123',algorithm='HS256')
print(datetime.datetime.utcnow())
print(jwt.decode(token,'123',algorithm=['HS256'])['name'])
print(json.loads(json.dumps(jwt.decode(token,'123',algorithm=['HS256'])))['name'])
print(int(time.time()))
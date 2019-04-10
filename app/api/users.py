#coding=utf8
from app.api import user
from flask import jsonify,request,Response
from functools import wraps
import json
from app.mongodb import redisdb
from app.mysqldb import read
from app.utils import resdto,py_jwt

# 登录限制的装饰器
def login_required(func):
    @wraps(func)
    def wapper(*args,**kwargs):
        token = request.headers['access_token']
        if py_jwt.validate(token):
            user = (py_jwt.validate(token))['name']
            if token and token == str(redisdb.getName(user), encoding = "utf8"):
                return func(*args,**kwargs)
            else:
                return jsonify(resdto.falseReturn(99,"登录信息过期"))
        else:
            return jsonify(resdto.falseReturn(99,"登录信息过期"))
    return wapper

@user.route('/q',methods=['GET','POST'])
@login_required
def q():
    #print(py_jwt.auth())
    return jsonify(resdto.falseReturn("哈哈哈","1"))
#折线
@user.route('/q1',methods=['GET','POST'])
def q1():
    data = json.loads(read.fetchData("select table_name from information_schema.tables where table_schema='fsttour'and table_type='base table';"))
    return jsonify(resdto.trueReturn(data,"ss"))
#折线
@user.route('/q2',methods=['GET','POST'])
def q2():
    data = json.loads(read.fetchData("select * from t_sys_role_function where rid =2"))
    return jsonify(resdto.trueReturn(data,"ss"))
#coding=utf8
from app.api import user
from flask import jsonify,request,Response
from functools import wraps
import json
from app.mysqldb import read
from app.utils import resdto

# 登录限制的装饰器
def login_required(func):
    @wraps(func)
    def wapper(*args,**kwargs):
        token = request.headers['access_token']
        if token and token == 'lld':
            return func(*args,**kwargs)
        else:
            return '请先登录'
    return wapper

@user.route('/q',methods=['GET','POST'])
@login_required
def q():
    return resdto.falseReturn({},"1")
#折线
@user.route('/q1',methods=['GET','POST'])
def q1():
    data = json.loads(read.fetchData("select table_name from information_schema.tables where table_schema='fsttour'and table_type='base table';"))
    return jsonify(resdto.trueReturn(data,"ss"))
#折线
@user.route('/q2',methods=['GET','POST'])
def q2():
    data = json.loads(read.fetchData("select * from bi_complain_total_mon"))
    return jsonify(resdto.trueReturn(data,"ss"))
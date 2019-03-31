#coding=utf8
from app.api import user
from flask import jsonify,request,Response
from functools import wraps
import json
from app.mysqldb import dao,rdao

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
	return json.dumps({
    "ret": 0,
    "msg": "OK",
    "errorcode": 0,
    "data": {
        "xAxis": {
          "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        },
        "series": {
          "data": [10, 52, 200, 334, 390, 330, 220]
        }
    }
	})
#折线
@user.route('/q1',methods=['GET','POST'])
def q1():
	return rdao.CJ("select table_name from information_schema.tables where table_schema='fsttour'and table_type='base table';")
#折线
@user.route('/q2',methods=['GET','POST'])
def q2():
	return jsonify({'user':'name'})
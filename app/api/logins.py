#coding=utf8
import json
from app.api import login
from flask import jsonify,request,Response,redirect
from app.mongodb import redisdb
from app.utils import py_jwt,resdto
from app.mysqldb import read

@login.route('/login',methods=['get','post'])
def log():
    reqUser = request.values['name']
    reqPwd = request.values['password']
    data = json.loads(read.fetchData("select * from t_sys_user where uid = "+reqUser))
        
    if len(data)!=0 and data[0]['passwd']==reqPwd:
        token = py_jwt.auth(reqUser)
        redisdb.setName(reqUser,token)
        return jsonify(resdto.trueReturn(str(token, encoding = "utf8"),'登陆成功'))
    else:
        return jsonify(resdto.falseReturn(0,'用户名密码错误'))

@login.route('/logout',methods=['get','post'])
def logout():
    redisdb.setName('1','')
    return ''
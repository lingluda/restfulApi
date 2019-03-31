#coding=utf8
from app.api import role

@role.route('q',methods=['GET','POST'])
def q():
	return 'roles'
#我哈哈
@role.route('q1',methods=['GET','POST'])
def q1():
	return '11111'
#coding=utf8
from app.api import func

@func.route('/q',methods=['GET','POST'])
def q1():
    return 'sss'

#coding=utf8
from app.user import user
from flask import jsonify
import json
	
@user.route('/q',methods=['GET','POST'])
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
	return 'holle world'
#折线
@user.route('/q2',methods=['GET','POST'])
def q2():
	return jsonify({'user':'name'})
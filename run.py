#coding=utf8
from flask import Flask
from app.user import user
from app.role import role
from app.func import func
app =Flask(__name__)

app.register_blueprint(user,url_prefix='/user')
app.register_blueprint(role,url_prefix='/role')
app.register_blueprint(func,url_prefix='/func')

if __name__ == '__main__':
	app.run('0.0.0.0',port=5000,debug=True)

#coding=utf8
from flask import Flask
from app.api import login
from app.api import user
from app.api import role
from app.api import func

app =Flask(__name__)
app.register_blueprint(login,url_prefix='/')
app.register_blueprint(user,url_prefix='/user')
app.register_blueprint(role,url_prefix='/role')
app.register_blueprint(func,url_prefix='/func')

if __name__ == '__main__':
	app.run('0.0.0.0',port=5000,debug=True)

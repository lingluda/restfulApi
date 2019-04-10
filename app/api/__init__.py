#coding=utf8
from flask import Blueprint
login = Blueprint('login',__name__)
func = Blueprint('func',__name__)
role = Blueprint('role',__name__)
user = Blueprint('user',__name__)
from app.api import logins
from app.api import funcs
from app.api import roles
from app.api import users
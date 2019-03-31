#coding=utf8
from flask import Blueprint

func = Blueprint('func',__name__)
role = Blueprint('role',__name__)
user = Blueprint('user',__name__)

from app.api import funcs
from app.api import roles
from app.api import users
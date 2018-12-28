#coding=utf8
from flask import Blueprint

user = Blueprint('user',__name__)

from app.user import users
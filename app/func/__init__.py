#coding=utf8
from flask import Blueprint

func = Blueprint('func',__name__)

from app.func import funcs
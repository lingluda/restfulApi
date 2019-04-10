#coding=utf8
import jwt
import time
import datetime
import json

def auth(val):
    print(val)
    token = jwt.encode({'name':val,'exp':datetime.datetime.utcnow() + datetime.timedelta(days=1)},'123',algorithm='HS256')
    #token = jwt.encode({'name':'lld'},'123',algorithm='HS256')
    return token

def validate(token):
    try:
        payload=jwt.decode(token,'123',algorithm=['HS256'])
        if payload:
            return payload
        else:
            raise jwt.InvalidTokenError
    except jwt.ExpiredSignatureError:
        return False
        # return 'token is outTime'
    
    except jwt.InvalidTokenError:
        return False
        # return 'token is invalid'

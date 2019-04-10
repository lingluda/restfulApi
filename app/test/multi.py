#coding=utf8
from concurrent.futures import ThreadPoolExecutor
import time
import requests

def task(url):
    res = requests.get(url)
    print(url,res)

pool = ThreadPoolExecutor(5)
url_list = [
    'http://127.0.0.1:5000/user/q1',
    'http://127.0.0.1:5000/user/q2',  
    'http://127.0.0.1:5000/user/q1',
    'http://127.0.0.1:5000/user/q2',  
    'http://127.0.0.1:5000/user/q1',
    'http://127.0.0.1:5000/user/q2',  
    'http://127.0.0.1:5000/user/q1',
    'http://127.0.0.1:5000/user/q2',  
    'http://127.0.0.1:5000/user/q1',
    'http://127.0.0.1:5000/user/q2',  
]
for url in url_list:
    pool.submit(task,url)

pool.shutdown(wait=True)
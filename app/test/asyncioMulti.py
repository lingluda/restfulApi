#coding=utf8
import asyncio
import requests
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
loop = asyncio.get_event_loop()
async def holle():
    print('holle')
    await asyncio.sleep(1)
async def fetch_data(url):
    res = requests.get(url)
    if res.json()['status']:
        print(111111111111111111111111)
    print(url,res.json()['status'])
    await asyncio.sleep(1)
for url in url_list:
    loop.run_until_complete(fetch_data(url))
loop.run_until_complete(holle())

'''
async def add(x,y):
    r = x+y
    return r

async def bad_call(a,b,c,d):
    a_b = await add(a,b)
    print ('a_b*c_d')
    await asyncio.sleep(1)
    c_d = await add(c,d)
    print (a_b*c_d)
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bad_call(1,2,3,4))
'''
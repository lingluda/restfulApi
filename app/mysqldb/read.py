#coding=utf8
import pymysql
import json
import datetime
from DBUtils.PooledDB import PooledDB

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)

def fetchData(sql):
    conn = pool.connection()  #以后每次需要数据库连接就是用connection（）函数获取连接就好了
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor) 
    # 查询
    #sql = "select t.*,s.* from test t left join t_sys_function s on t.id=s.id"
    reCount = cur.execute(sql)  
    # 返回受影响的行数
    print(reCount)
    data = cur.fetchall()
    # 返回数据,返回的是tuple类型
    return json.dumps(data, cls=Encoder,sort_keys=True, indent=4)
    cur.close()
    conn.close()
def commitData(sql):
    conn = pool.connection()  #以后每次需要数据库连接就是用connection（）函数获取连接就好了
    cur = conn.cursor()
    try:
		# 执行sql语句
	    cur.execute(sql)
		# 提交到数据库执行
	    conn.commit()
    except:
		# Rollback in case there is any error
        conn.rollback()
    cur.close()
    conn.close()
#coding=utf8
import pymysql
import json
import datetime

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)
conn = pymysql.connect(host='gz-cdb-kx9p12uu.sql.tencentcdb.com', user='dbig', passwd='Lovelock2017', db='fsttour',port=63312)

def fetchData(sql):
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
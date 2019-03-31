#coding=utf8
import MySQLdb as mdb
import MySQLdb.cursors

def CJ(sql):
	conn = mdb.connect(host='gz-cdb-kx9p12uu.sql.tencentcdb.com',port=63312,user='dbig',passwd='Lovelock2017',db='fsttour')
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
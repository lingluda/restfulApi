#coding=utf8  
import MySQLdb
import json
import datetime

class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)
# 定义查询SQL语句
def CJ(sql):
	restData=''
	#sql = "SELECT * FROM "+tablename

# 设置列的别名或者直接用表字段名:（下面的sql含有别名）

# sql="SELECT s.id AS 1_id,s.name AS 2_na,s.local AS 3_lo,s.mobile AS 4_mo,s.CreateTime AS 5_ct FROM db1.s1 s;"

# 定义连接MySQL的登录信息（此处以字典形式）
	Loginfo = {'USER':'dbig', 'PSWD':'Lovelock2017', 'HOST':'gz-cdb-kx9p12uu.sql.tencentcdb.com', 'PORT':63312}

# Python 连接MySQL
	conn=MySQLdb.connect(host=Loginfo['HOST'],user=Loginfo['USER'],passwd=Loginfo['PSWD'],port=Loginfo['PORT'],charset='utf8',db='fsttour')
	cur=conn.cursor()
	cur.execute(sql)                        # 执行SQL查询
	data = cur.fetchall()  
	print len(data)
# 查询结果给data。如果执行：print data 显示结果：（（第一行内容），（第二行内容），（第三行内容），（第四行内容））
	fields = cur.description               # 获取查询结果中列的字段名，如果查询SQL中使用别名，此处显示别名。  
#print (fields)  
	cur.close()
	conn.close()

# Main 
	column_list = []                       # 定义字段名的列表
	cc = 0
	for i in fields:
		column_list.append(i[0])
#print column_list
	length = len(column_list)
	#f=open('json.txt','w')

# 一次循环，row代表一行，row以元组的形式显示。
	for row in data:
		result = {}
		while cc < length:
			#print row[cc]
			# 将row中的每个元素，追加到字典中.
			result[column_list[cc]] = row[cc]
			# Python的dict --转换成----> json的object
			jsondata=json.dumps(result,cls=CJsonEncoder,ensure_ascii=False,encoding='gbk') 
			cc=cc+1
		# 写入文件
		cc=0
		#f.write(jsondata + ',\n')
		restData=restData+''.join(jsondata + ',\n')
	return '['+restData[:-2]+']'
	#f.close() 
#nums = CJ('test')
#print (nums)


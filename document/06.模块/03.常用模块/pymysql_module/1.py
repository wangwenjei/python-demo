import pymysql
conn = pymysql.connect(
           host='127.0.0.1',
           port=3306,
           user='stu',
           passwd='123456',
           db='student',
           charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()

sql = "select * from student where id>20;"
cursor.execute(sql)


data = cursor.fetchone()

print(data)
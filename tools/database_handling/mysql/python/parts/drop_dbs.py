import pymysql

# connection = pymysql.connect(host="localhost",user="root",passwd="tlove759")
connection = pymysql.connect(host="localhost", user="root")
# connection = pymysql.connect(host="localhost")

cursor = connection.cursor()
sql = 'DROP DATABASE testdb1'
cursor.execute(sql)
connection.commit()

connection.close()
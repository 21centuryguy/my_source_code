import pymysql
 
# connection = pymysql.connect(host="localhost",user="root",passwd="tlove759")
connection = pymysql.connect(host="localhost", user="root")
# connection = pymysql.connect(host="localhost")
 
cursor = connection.cursor()
 
connection.close()

import pymysql

# connection = pymysql.connect(host="localhost",user="root",passwd="tlove759")
connection = pymysql.connect(host="localhost", user="root")
# connection = pymysql.connect(host="localhost")

cursor = connection.cursor()
sql = 'SHOW DATABASES' ### or "SHOW DATABASES"
cursor.execute(sql)
connection.close()

print "\n\n=========== db list ==========="
m = 0
for sql in cursor:
	m = m + 1
	print sql[0]
print "\n=========== db count ==========="
print m
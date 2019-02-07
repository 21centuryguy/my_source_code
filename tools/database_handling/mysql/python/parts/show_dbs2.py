import pymysql

# connection = pymysql.connect(host="localhost",user="root",passwd="tlove759")
connection = pymysql.connect(host="localhost", user="root")
# connection = pymysql.connect(host="localhost")

cursor = connection.cursor()
sql = 'SHOW DATABASES' ### or "SHOW DATABASES"
cursor.execute(sql)

sql_list = []
for sql in cursor:
	sql_list.append(sql[0])

print "\n=========== db count ==========="
print len(sql_list)

print "\n=========== db list ==========="
m = 0
while m < len(sql_list):
	print "db",m+1,"is :",sql_list[m]
	m = m + 1

connection.close()
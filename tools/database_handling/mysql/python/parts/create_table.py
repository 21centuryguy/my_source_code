import pymysql

##################################################################
###################### connecting to server 

# connection = pymysql.connect(host="localhost",user="root",passwd="tlove759")
connection = pymysql.connect(host="localhost", user="root")
# connection = pymysql.connect(host="localhost")
cursor = connection.cursor()


##################################################################
###################### showing database

def showdb():
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


##################################################################
###################### creating database

def createdb():
	print '\n\n\nTyep a dbname to create.\n'
	input_value = raw_input('>> ')

	sql = 'CREATE DATABASE '+input_value ### or "SHOW DATABASES"
	cursor.execute(sql)
	connection.commit()
	print  "db ", input_value, "is created."


##################################################################
###################### selecting database

def usedb():
	print '\n\n\nTyep a dbname to use.\n'
	input_value = raw_input('>> ')
 
	sql = 'USE '+input_value ### or "SHOW DATABASES"
	cursor.execute(sql)
	print  "db ", input_value, "is selected."


##################################################################
###################### Query for creating table

def createtable():
	print '\n\n\nTyep a table name to create.\n'
	input_value = raw_input('>> ')	
	# create_tablesql = "CREATE TABLE"+input_value+"""(ID INT(20) PRIMARY KEY AUTO_INCREMENT, NAME  CHAR(20) NOT NULL, TRACK CHAR(10))"""
	create_tablesql = 'CREATE TABLE '+input_value+'(ID INT(20) PRIMARY KEY AUTO_INCREMENT,NAME  CHAR(20) NOT NULL,TRACK CHAR(10))'
	cursor.execute(create_tablesql)
	print  "db ", input_value, "is created."


##################################################################
###################### Showing table

def showtable():
	print '\n\n\n========== Table list ==========\n' 
	sql = 'SHOW TABLES'
	cursor.execute(sql)

	sql_list = []
	for sql in cursor:
		sql_list.append(sql[0])
 
	print "\n=========== table count ==========="
	print len(sql_list)
 
	print "\n=========== table list ==========="
	m = 0
	while m < len(sql_list):
		print "db",m+1,"is :",sql_list[m]
		m = m + 1

##################################################################
###################### Main fun

def main():
	print "\n\n\n==============================="
	showdb()

	print "\n\n\n==============================="
	createdb()

	print "\n\n\n==============================="
	showdb()

	print "\n\n\n==============================="
	usedb()

	print "\n\n\n==============================="
	createtable()

	print "\n\n\n==============================="
	showtable()

	connection.close()


main()
print "\n\n\nbye ^_^\n\n\n"

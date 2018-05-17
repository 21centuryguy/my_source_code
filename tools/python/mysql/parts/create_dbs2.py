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
	print '\nTyep a dbname to delete.\n'
	input_value = raw_input('>> ')

	sql = 'CREATE DATABASE '+input_value ### or "SHOW DATABASES"
	cursor.execute(sql)
	connection.commit()
	print  "db ", input_value, "is created."


##################################################################
######################  main

def main():
	print "\n\n\n==============================="
	showdb()

	print "\n\n\n==============================="
	createdb()

	print "\n\n\n==============================="
	showdb()

	connection.close()


main()
print "\n\n\nbye ^_^\n\n\n"
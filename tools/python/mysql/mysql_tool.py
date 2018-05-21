#!/usr/bin/python
# -*- coding: utf-8 -*-
#print(chr(27) + "[2J")
print("\033c")
print "###################################################"
print "###################################################"
print "###                                             ###"
print "###             mysql v0.4 (by Jack)            ###"
print "###                                             ###"
print "###################################################"
print "###################################################\n\n\n\n\n"

### import module
import pymysql


############################################################################
############################################################################
############################################################################
###                                                                      ###
###                      [ 1 ] connect to mysql server                   ###
###                                                                      ###
###                                                                      ###
############################################################################
############################################################################


# 000
def connecting():
  # print '>>>>>>> debugging >>>>>>> [1] def connecting(): [1]'

  print "\n\n\n\n======================================================================\n"
  print "=============== => [1] connect to mysql server\n"
  print "===============    [2] SHOW DBs / Tables and SELECT\n"
  print "===============    [3] xxxxxxxxxxxxxxxxxxxxxx\n"
  print "===============    [4] xxxxxxxxxxxxxxxxxxxxxx\n"

# 111
  ans="y"
  while not ans ==  "n":
    # print '>>>>>>> debugging >>>>>>> [1] def connecting(): [2] while not ans ==  "n":'

    print "========================================================================="
    print "========================================================================="
    print "[1] Do you want to set connection (again) ?  'y'(yes) / 'n'(no)"
    ans = raw_input('>> ')

# 222
    if ans == "y":
      # print '>>>>>>> debugging >>>>>>> [1] def connecting(): [3] ans == "y":'
    
      ### set host
      print "\n\n\n\n======================================================================\n"
      print "================== ==> [1.1] set hostname\n"
      print "==================     [1.2] set user name\n"
      print "==================     [1.3] set password\n"

      print "[1.1] Do you want to set hostname? 'y'(yes) / 'n'(no : use 'localhost')"
      input_value = raw_input('>> ')

# 333
      if input_value == "y":
        # print '>>>>>>> debugging >>>>>>> [1] def connecting(): [4] if input_value == "y":'

        ########################################################################################
        ########################################################################################
        ########################################################################################

        print "\n\n\nPlease type target hostname."
        host_value = raw_input('>> ')
        print "\n\n\nYour target hostname is [",host_value,"]"

        ########################################################################################
        ########################################################################################
        ########################################################################################

# 333
      elif input_value == "n":
        # print '>>>>>>> debugging >>>>>>> [1] def connecting(): [5] elif input_value == "n":'
        host_value = "localhost"

# 333
      else:
        # print '>>>>>>> debugging >>>>>>> [1] def connecting(): [6] else:'

        print "wrong input -_-"

      ### set user

      print "\n\n\n\n======================================================================\n"
      print "==================     [1.1] set hostname\n"
      print "================== ==> [1.2] set user name\n"
      print "==================     [1.3] set password\n"

      print "[1.2] Do you want to set user name? 'y'(yes) / 'n'(no : 'root')"
      input_value = raw_input('>> ')

# 333
      if input_value == "y":
        # print '>>>>>>> debugging >>>>>>> [1] def connecting(): [7] if input_value == "y":'

        ########################################################################################
        ########################################################################################
        ########################################################################################
   
        print "\n\n\nPlease type an user name."
        user_value = raw_input('>> ')
        print "\n\n\nUser name is [",user_value,"]"

        ########################################################################################
        ########################################################################################
        ########################################################################################

# 333
      elif input_value == "n":
        # print '>>>>>>> debugging >>>>>>> [1] def connecting(): [8] elif input_value == "n":'

        user_value = "root"

# 333
      else:
        # print '>>>>>>> debugging >>>>>>> [1] def connecting(): [9] else:'

        print "wrong input -_-"

      ### set password

      print "\n\n\n\n======================================================================\n"
      print "==================     [1.1] set hostname\n"
      print "==================     [1.2] set user name\n"
      print "================== ==> [1.3] set password\n"

      print "[1.3] Do you want to set password? 'y'(yes) / 'n'(no : 'default')"
      input_value = raw_input('>> ')

# 333
      if input_value == "y":
        # print '>>>>>>> debugging >>>>>>> [1] def connecting(): [10] if input_value == "y":'

        ########################################################################################
        ########################################################################################
        ########################################################################################

        print "\n\n\nPlease type password."
        passwd_value = raw_input('>> ')

        ########################################################################################
        ########################################################################################
        ########################################################################################

# 333
      elif input_value == "n":
        # print '>>>>>>> debugging >>>>>>> [1] def connecting(): [11] elif input_value == "n":'

        passwd_value = "tlove759"

# 333
      else:
        # print '>>>>>>> debugging >>>>>>> [1] def connecting(): [12] else:'

        print "wrong input -_-"

      ### connect mongodb

      # connection = pymysql.connect(host=host_value, user=user_value, passwd=passwd_value)
      connection = pymysql.connect(host=host_value, user=user_value)
      # connection = pymysql.connect(host="localhost")
      return connection

        ########################################################################################
        ########################################################################################
        ########################################################################################

# 222
    elif ans == "n":
      # print '>>>>>>> debugging >>>>>>> [1] def connecting(): [13] elif ans == "n":'

      ### connect mongodb
      # connection = pymysql.connect(host="localhost",user="root",passwd="tlove759")
      connection = pymysql.connect(host="localhost", user="root")
      # connection = pymysql.connect(host="localhost")
      return connection

      print "Connection setting is over.\n"
      ans = False
      break

# 222
    else:
      # print '>>>>>>> debugging >>>>>>> [1] def connecting(): [14] else:'

      print "wrong input -_-\n"
      print "Please try again."




############################################################################
############################################################################
############################################################################
###                                                                      ###
###                                                                      ###
###                                SHOW DBs                              ###
###                                                                      ###
###                                                                      ###
############################################################################
############################################################################

# 000
def SHOW_dbs(connection):
  # print '>>>>>>> debugging >>>>>>> [2] def SHOW_dbs(connection): [1]'

  sql = 'SHOW DATABASES' ### or "SHOW DATABASES"
  cursor = connection.cursor()
  cursor.execute(sql)

  # 111
  dbs_list = []
  for sql in cursor:
    # print '>>>>>>> debugging >>>>>>> [2] def SHOW_dbs(connection): [2] for sql in cursor:'

    dbs_list.append(sql[0])

  print "\n=========== db count ==========="
  print len(dbs_list)

  print "\n=========== db list ==========="

  # 111
  m = 0
  while m < len(dbs_list):
    # print '>>>>>>> debugging >>>>>>> [2] def SHOW_dbs(connection): [3] while m < len(sql_list):'

    print "db",m+1,"is :",dbs_list[m]
    m = m + 1

  return connection, dbs_list

############################################################################
############################################################################
############################################################################
###                                                                      ###
###                                                                      ###
###                       SHOW / SELECT FROM Tables                      ###
###                                                                      ###
###                                                                      ###
############################################################################
############################################################################

# 000
def SHOW_tables(connection, dbs_list):
  # print '>>>>>>> debugging [3] : def SHOW_tables(connection, dbs_list): [1]'

  print "\n\n\nPlease select a DB"
  selected_db_val = raw_input('>> ')

  selected_db = dbs_list[int(selected_db_val)-1]

  sql = 'USE '+selected_db
  cursor = connection.cursor()
  cursor.execute(sql)

  sql = 'SHOW TABLES'
  cursor = connection.cursor()
  cursor.execute(sql)

  # 111
  tables_list = []
  for sql in cursor:
    # print '>>>>>>> debugging >>>>>>> [3] def SHOW_tables(connection, dbs_list): [2] for sql in cursor:'
    tables_list.append(sql[0])

  print "\n=========== Tables count ==========="
  print len(tables_list)

  print "\n=========== Tables list ==========="

  # 111
  m = 0
  while m < len(tables_list):
    # print '>>>>>>> debugging >>>>>>> [3] : def SHOW_tables(connection, dbs_list): [3] while m < len(tables_list):'

    print "tables",m+1,"is :",tables_list[m]
    m = m + 1

  print "\n\n\nPlease select a table"
  selected_table_val = raw_input('>> ')

  selected_table = tables_list[int(selected_table_val)-1]

############################################################

  sql = 'SELECT * FROM '+selected_table
  cursor1 = connection.cursor()
  cursor1.execute(sql)
  column_field_tuple = cursor1.description

  cursor2 = connection.cursor()
  cursor2.execute(sql)
  row_field_tuple = cursor2.fetchall()

  #####################

  print "\n\n\n=========== column and row count ==========="
  column_count = len(column_field_tuple)
  row_count = len(row_field_tuple)

  print "Column count :",column_count
  print "Row count",row_count

  # 111
  print "\n\n\n=========== column field key list ==========="
  m = 0
  while m < column_count:
    print column_field_tuple[m][0]
    m = m + 1

  # 111
  print "\n\n\n=========== column field key row ==========="
  m = 0
  column_field_key_list = []
  while m < column_count:
    column_field_key_list.append(column_field_tuple[m][0])
    m = m + 1
  column_field_key_tuple = tuple(column_field_key_list)
  print column_field_key_tuple

  # 111
  print "\n\n\n=========== all column info ==========="
  m = 0
  while m < column_count:
    print column_field_tuple[m]
    m = m + 1

  #####################

  # 111
  print "\n\n\n=========== row head field value ==========="
  m = 0
  while m < row_count:
    print row_field_tuple[m][0]
    m = m + 1

  # 111
  print "\n\n\n=========== whole row field value ==========="
  m = 0
  while m < row_count:
    print row_field_tuple[m]
    m = m + 1



############################################################################
############################################################################
############################################################################
###                                                                      ###
###                                                                      ###
###                   [2]  SHOW DBs / Tables and SELECT                  ###
###                                                                      ###
###                                                                      ###
############################################################################
############################################################################

# 000
def SHOW(connection):
  # print '>>>>>>> debugging [15] : def SHOW(cursor):'

  print "\n\n\n\n======================================================================\n"
  print "===============    [1] connect to mysql server\n"
  print "=============== => [2] SHOW DBs / Tables and SELECT\n"
  print "===============    [3] xxxxxxxxxxxxxxxxxxxxxx\n"
  print "===============    [4] xxxxxxxxxxxxxxxxxxxxxx\n"

# 111
  ans="y"
  while not ans ==  "n":
    # print '>>>>>>> debugging [16] : while not ans ==  "n":'

    print "\n\n\n\n======================================================================\n"
    print "================== ==> [2] SHOW DBs / Tables and SELECT\n"

    print "========================================================================="
    print "[2] Do you want to SHOW DBs / Tables and SELECT (again)?  'y'(yes) / 'n'(no)\n"
    ans = raw_input('>> ')

# 222
    if ans == "y":
      # print '>>>>>>> debugging [17] : if ans == "y":'
    
      ### SHOW dbs
      print "\n\n\n\n======================================================================\n"
      print "================== ==> [2.1] SHOW DBs\n"
      print "==================     [2.2] SHOW / SELECT * FROM Tables\n"

      print "[2.1] Do you want to SHOW DBs? 'y'(yes) / 'n'(no)"
      input_value = raw_input('>> ')

# 333
      if input_value == "y":
        # print '>>>>>>> debugging [18] : if input_value == "y":'

        ########################################################################################
        ########################################################################################
        ########################################################################################

        SHOW_dbs(connection)

        ########################################################################################
        ########################################################################################
        ########################################################################################

# 333
      elif input_value == "n":
        # print '>>>>>>> debugging [20] : elif input_value == "n":'

        pass

# 333
      else:
        # print '>>>>>>> debugging [21] : else:'

        print "wrong input -_-"


      ### SHOW tables
      print "\n\n\n\n======================================================================\n"
      print "==================     [2.1] SHOW DBs\n"
      print "================== ==> [2.2] SHOW / SELECT * FROM Tables\n"

      print "[2.2] Do you want to SHOW Tables? 'y'(yes) / 'n'(no)"
      input_value = raw_input('>> ')

# 333
      if input_value == "y":
        # print '>>>>>>> debugging [22] : if input_value == "y":'

        ########################################################################################
        ########################################################################################
        ########################################################################################

        return_from_SHOW_dbs = []
        return_from_SHOW_dbs = SHOW_dbs(connection)
        connection = return_from_SHOW_dbs[0]
        dbs_list = return_from_SHOW_dbs[1]

        SHOW_tables(connection, dbs_list)

        ########################################################################################
        ########################################################################################
        ########################################################################################

# 333
      elif input_value == "n":
        # print '>>>>>>> debugging [23] : elif input_value == "n":'

        connection.close()
        print "connection is closed"

# 333
      else:
        # print '>>>>>>> debugging [24] : else:'

        print "wrong input -_-"

        ########################################################################################
        ########################################################################################
        ########################################################################################

# 222
    elif ans == "n":
      # print '>>>>>>> debugging [25] : elif ans == "n":'

      try:
        connection.close()
        print "connection is closed"
      except Exception as e:
        pass

      print "SHOWing DBs and Tables is over.\n"

      ans = False
      break

# 222
    else:
      # print '>>>>>>> debugging [26] : else:'

      print "wrong input -_-\n"
      print "Please try again."


############################################################################
############################################################################
############################################################################
###                                                                      ###
###                                                                      ###
###                                  main()                              ###
###                                                                      ###
###                                                                      ###
############################################################################
############################################################################

def main():
  # print '>>>>>>> debugging [0] : def main():'

  connection = connecting() # return cursor

  SHOW(connection)

  # db_name = SHOW() # return db_name

  # edit(db_name)

  print "Bye !!!"

main()

###########################################
###########################################
###            ###                      ###
###   Bottom   ###     coded by Jack    ###
###            ###                      ###
###########################################
###########################################

# -*- coding: utf-8 -*-
#print(chr(27) + "[2J")
print("\033c")
print "###################################################"
print "###################################################"
print "###                                             ###"
print "###             mgdbtool v1.3.4 (by Jack)       ###"
print "###                                             ###"
print "###################################################"
print "###################################################\n\n\n\n\n"

### import module
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps
from pprint import pprint

### connect mongodb
client = MongoClient('localhost',27017)


############################################################################
############################################################################
############################################################################
###                                                                      ###
###                       1. Database error check                        ###
###                                                                      ###
###                                                                      ###
############################################################################
############################################################################


print "\n\n\n\n======================================================================\n"
print "=============== => [1] Database error check\n"
print "===============    [2] Validate_Collections\n"
print "===============    [3] Show contents(collections, documents) of databases )\n"
print "===============    [4] Search database, collection, document\n"
ans="y"
while not ans ==  "n":
  print "========================================================================="
  print "========================================================================="
  print "Do you want to check database status (again) ?  'y'(yes) / 'n'(no)"
  ans = raw_input('>> ')

  if ans == "y":

    ### getPrevError
    print "\n\n\n\n======================================================================\n"
    print "================== ==> [1.1] check [ Last Status ] of databases\n"
    print "==================     [1.2] check [ Previous Error ] of databases\n"
    print "==================     [1.3] check [ Last Error ] of databases\n"

    print " Do you want to check databases last status? 'y'(yes) / 'n'(no)"
    input_value = raw_input('>> ')
    if input_value == "y":
      print "\n\n\n======================[ result ]=========================\n"
      dbname_list = client.database_names()
      dbname_list_length = len(dbname_list)
      print "\n\ndatabase count:",dbname_list_length,"\n\n"
      m = 0
      while m < dbname_list_length:
        db = getattr(client, dbname_list[m])
        last_status = db.last_status()
        print "[", dbname_list[m],"]: [ ",last_status," ]\n"
        m = m + 1
      print "\n========================================="
      print "\ndatabase [ Last Status ] checking count:",dbname_list_length,"\n\n"
        
    elif input_value == "n":
      pass

    else:
      print "wrong input -_-"



    ### getPrevError
    print "\n\n\n\n======================================================================\n"
    print "==================     [1.1] check [ Last Status ] of databases\n"
    print "================== ==> [1.2] check [ Previous Error ] of databases\n"
    print "==================     [1.3] check [ Last Error ] of databases\n"

    print "Do you want to check previous error of databases? 'y'(yes) / 'n'(no)"
    input_value = raw_input('>> ')
    if input_value == "y":
      print "\n\n\n======================[ result ]=========================\n"
      dbname_list = client.database_names()
      dbname_list_length = len(dbname_list)
      print "\n\ndatabase count:",dbname_list_length,"\n\n"
      m = 0
      while m < dbname_list_length:
        db = getattr(client, dbname_list[m])
        last_error = db.previous_error()
        print "[", dbname_list[m],"]: [ ",last_error," ]\n"
        m = m + 1
      print "\n========================================="
      print "\ndatabase [ Previous Error ] checking count:",dbname_list_length,"\n\n"

    elif input_value == "n":
      pass

    else:
      print "wrong input -_-"



    ### getLastError
    print "\n\n\n\n======================================================================\n"
    print "==================     [1.1] check [ Last Status ] of databases\n"
    print "==================     [1.2] check [ Previous Error ] of databases\n"
    print "================== ==> [1.3] check [ Last Error ] of databases\n"

    print "Do you want to check last error of databases? 'y'(yes) / 'n'(no)"
    input_value = raw_input('>> ')
    if input_value == "y":
      print "\n\n\n======================[ result ]=========================\n"
      dbname_list = client.database_names()
      dbname_list_length = len(dbname_list)
      print "\n\ndatabase count:",dbname_list_length,"\n\n"
      m = 0
      while m < dbname_list_length:
        db = getattr(client, dbname_list[m])
        last_error = db.error()
        print "[", dbname_list[m],"]: [ ",last_error," ]\n"
        m = m + 1
      print "\n========================================="
      print "\ndatabase [ Last Error ] checking count:",dbname_list_length,"\n\n"
      print "\n\n\n\n\n"

    elif input_value == "n":
      pass

    else:
      print "wrong input -_-"

  elif ans == "n":
    print "database error check is over.\n"
    ans = False
    break

  else:
    print "wrong input -_-\n"
    print "Please try again."

############################################################################
############################################################################
############################################################################
###                                                                      ###
###								         ###                                            ###
###                        2. Validate_collection                        ###
###                                                                      ###
###                                                                      ###
############################################################################
############################################################################


print "\n\n\n\n======================================================================\n"
print "===============    [1] Database error check\n"
print "=============== => [2] Validate_Collections\n"
print "===============    [3] Show contents(collections, documents) of databases )\n"
print "===============    [4] Search database, collection, document\n"

ans="y"
while not ans ==  "n":
  print "\n\n\n\n======================================================================\n"
  print "================== ==> [2.1] Validating [ collectinos ] of databases\n"

  print "========================================================================="
  print "Do you want to validate collectinos (again)?  'y'(yes) / 'n'(no)\n"
  ans = raw_input('>> ')

  if ans == "y":
    ### show db name list
    print "\n\n\n================= database name list =================\n"
    database_name_list = client.database_names()
    # print dumps(client.database_names())
    # print "database count : ", len(database_name_list)
    k = 0
    while k < len(database_name_list):
      print k+1," : ",database_name_list[k]
      k = k + 1
    print "\n==================================================="


    ### select database
    print "\n1. Please type a number of database."
    num_db = raw_input('>> ')
    dbname = database_name_list[int(num_db)-1]
    db = getattr(client, dbname)
    print "\n\ndatabase [ "+dbname+" ]"+" is selected.\n\n"


    ### show collection name list
    coll_name_list = db.collection_names()
    print "\n\n\n================= collection name list of database [",dbname,"] =================\n"
    print coll_name_list

    coll_name_list_length = len(coll_name_list)
    print "\n\ncollection count:",coll_name_list_length,"\n\n"
    m = 0
    while m < coll_name_list_length:
      coll = getattr(db, coll_name_list[m])
      # coll_validate_result = db.validate_collection(coll_name_list[m], scandata=False, full=False)
      coll_validate_result = db.validate_collection(coll_name_list[m], scandata=True, full=True)
      # print "[ Validate_Collections ] check result of collection [ ",coll," ]: [ ",coll_validate_result," ]\n"

      ### validation result check
      print "Count :",m+1
      print "============ Validation result of collection [",coll_name_list[m],"] of database [",dbname,"] ====="
      print "errors :",coll_validate_result.get("errors","")
      print "valid :",coll_validate_result.get("valid",""),"\n\n"
      m = m + 1
    print "\n=========================================\n"
    print "Validated collection count :",m
    print "\n\n\n\n\n"

  elif ans == "n":
    print "validation check is over."
    ans = False
    break

  else:
    print "wrong input -_-\n"
    print "Please try again."



############################################################################
############################################################################
############################################################################
###									                                                     ###
###                                                                      ###
###         3. Show contents(collections, documents) of database         ###
###                                                                      ###
###                                                                      ###
############################################################################
############################################################################


print "\n\n\n\n======================================================================\n"
print "===============    [1] Database error check\n"
print "===============    [2] Validate_Collections\n"
print "=============== => [3] Show contents(collections, documents) of databases )\n"
print "===============    [4] Search database, collection, document\n"

ans="y"
while not ans ==  "n":
  print "========================================================================="
  print "========================================================================="
  print "Do you want to show contents of database (again)?  'y'(yes) / 'n'(no)\n"
  ans = raw_input('>> ')

  if ans == "y":

    ### show db name list
    print "\n\n\n================= database name list =================\n"
    database_name_list = client.database_names()
    # print dumps(client.database_names())
    # print "database count : ", len(database_name_list)
    k = 0
    while k < len(database_name_list):
      print k+1," : ",database_name_list[k]
      k = k + 1 
    print "\n==================================================="



    ### select database
    print "\n1. Please type a number of database."
    num_db = raw_input('>> ')
    dbname = database_name_list[int(num_db)-1]
    db = getattr(client, dbname)
    print "\n\ndatabase [ "+dbname+" ]"+" is selected.\n\n"



    ### show collection name list
    print "\n\n\n\n================= collection name list of database [ "+dbname+" ] =================\n"
    coll_name_list = db.collection_names()
    p = 0
    while p < len(coll_name_list):
      print p+1," : ",coll_name_list[p]
      p = p + 1    
    print "\n==================================================="



    ### select collections
    print "\n2. Please type a number of collection."
    num_coll = raw_input('>> ')
    collname = coll_name_list[int(num_coll)-1]
    coll = getattr(db, collname)
    print "\n\ncollection [ "+collname+" ]"+" is selected.\n\n"


    ### coll_count
    print "\n\n\n\n================ number of document of collection [ "+collname+" ]=================\n"
    print "document count ( collection [ "+collname+" ]): ",coll.count()



    ### fields of document
    print "\n\n\n\n======================================================================\n"
    print "================== ==> [3.1] field keys of document of collection [ "+collname+" ]\n"
    print "==================     [3.2] values of document of collection [ "+collname+" ]\n"
    print "==================     [3.3] show documents of colloection [ "+collname+" ]\n"    

    print "show field keys? 'y'(yes) / 'n'(no)"
    input_value = raw_input('>> ')
    if input_value == "y":
      print "\n\n\n======================[ result ]=========================\n"
      for xxx in coll.find():
        print dumps(xxx.keys())+"\n";\
        print "\n"
      print "\n============================================================"
      print "\n[Show field kyes] result list count ( collection [ "+collname+" ]): ",coll.count()

    elif input_value == "n":
      pass

    else:
      print "wrong input -_-"



    ### values of document
    print "\n\n\n\n======================================================================\n"
    print "==================     [3.1] field keys of document of collection [ "+collname+" ]\n"
    print "================== ==> [3.2] values of document of collection [ "+collname+" ]\n"
    print "==================     [3.3] show documents of colloection [ "+collname+" ]\n"

    print "show values? 'y'(yes) / 'n'(no)"
    input_value = raw_input('>> ')
    if input_value == "y":
      print "\n\n\n======================[ result ]=========================\n"
      for xxx in coll.find():
        print dumps(xxx.values())+"\n";\
        print "\n"
      print "\n============================================================"
      print "\n[Show values] result list count ( collection [ "+collname+" ]): ",coll.count()

    elif input_value == "n":
      pass

    else:
      print "wrong input -_-"



    ### show all document
    print "\n\n\n\n======================================================================\n"
    print "==================     [3.1] field keys of document of collection [ "+collname+" ]\n"
    print "==================     [3.2] values of document of collection [ "+collname+" ]\n"
    print "================== ==> [3.3] show documents of colloection [ "+collname+" ]\n"

    print "show documents? 'y'(yes) / 'n'(no)"
    input_value = raw_input('>> ')
    if input_value == "y":
      print "\n\n\n======================[ result ]=========================\n"
      for xxx in coll.find():
        print dumps(xxx);\
        print "\n"
      print "\n============================================================"
      print "\n[Show document] result list count ( collection [ "+collname+" ]): ",coll.count()

    elif input_value == "n":
      pass

    else:
      print "wrong input -_-"

    print "\n\n\n\n\n"

  elif ans == "n":
    print "show database contents is over.\n"
    ans = False
    break

  else:
    print "wrong input -_-\n"
    print "Please try again."


############################################################################
############################################################################
############################################################################
###                                                                      ###
###                                                                      ###
###               4. Search database, collection, document               ###
###                                                                      ###
###                                                                      ###
############################################################################
############################################################################
############################################################################


print "\n\n\n\n======================================================================\n"
print "===============    [1] Database error check\n"
print "===============    [2] Validate_Collections\n"
print "===============    [3] Show contents(collections, documents) of databases )\n"
print "=============== => [4] Search database, collection, document\n"

ans="y" ### loop condition of [4]
while not ans ==  "n":
  print "\n\n\n========================================================================="
  print "========================================================================="
  print "Do you want to search database, collection, document (again)?  'y'(yes) / 'n'(no)\n"
  ans = raw_input('>> ')
  if ans == "y":


############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################

    ### searching database(s) by keyword through all databases.
    print "\n\n\n\n=========================================================="
    print "================== ==> [4.1] Search database\n"
    print "==================     [4.2] Search collection\n"
    print "==================     [4.3] Search filed kye from document\n"
    print "==================     [4.4] Search document by filed kye and value\n"
    print "==================     [4.5] Search value from document\n"

    ans="y" ### loop condition of [4.1]
    while not ans ==  "n":
      print "\n\n\nDo you want to search database ( again )?  'y'(yes) / 'n'(no)"
      ans = raw_input('>> ')
      if ans == "y":

        print "\n\n\n================= database name list =================\n"
        database_name_list = client.database_names()
        print dumps(client.database_names())
        print "\n\n\ndatabase count : ",len(database_name_list),"\n"
        # print "database_name_list : ", database_name_list
        print "\n===================================================\n\n\n\n"

        print "Please type some keywords for searching database\n"
        key_word = raw_input('>> ')
        print "\n\nStarting to search database(s) by fuzzy matching for [ ",key_word," ]\n\n\n"

        matching = []
        matching = [xxx for xxx in database_name_list if key_word in xxx]
        # print matching
        print "Matching count : ",len(matching)
        print "\n\nMatching result : ",dumps(matching)

      elif ans == "n":
        print "Searching database is over.\n"
        ans = False
        break

      else:
        print "wrong input -_-\n"
        print "Please try again."


############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################

    ### searching collection(s) by keyword through all databases.
    print "\n\n\n\n=========================================================="
    print "==================     [4.1] Search database\n"
    print "================== ==> [4.2] Search collection\n"
    print "==================     [4.3] Search filed kye from document\n"
    print "==================     [4.4] Search document by filed kye and value\n"
    print "==================     [4.5] Search value from document\n"

    ans="y" ### loop condition of [4.2]
    while not ans ==  "n":
      print "\n\n\nDo you want to search collection(s) ( again )?  'y'(yes) / 'n'(no)"
      ans = raw_input('>> ')
      if ans == "y":
   
        print "\n\n\n================= collection name list from all database =================\n"

        ### database
        database_name_list = client.database_names()
        # print dumps(client.database_names())
        # print "database count : ", len(database_name_list)
        k = 0
        all_coll_list = []
        while k < len(database_name_list):
          dbname = database_name_list[k]
          # print dbname
          db = getattr(client, dbname)
  
          coll_name_list = db.collection_names()

          ## show [ collection (database) ] list one by one
          g = 0
          while g < len(coll_name_list):
            collname = coll_name_list[g]
            # print collname
            # print collname,"(",dbname,")\n"
            g = g + 1
          k = k + 1 


          ## get all collecion list

          for xxx in coll_name_list:
            all_coll_list.append(xxx)

        print "\n\nCount of all collectons : ",len(all_coll_list)
        print "\n\n\nList of all collectons:\n\n",
        pprint(all_coll_list)
        print "\n==================================================="


        ### searching collection(s) by keyword through all databases

        print "Please type some keywords for searching collection\n"
        key_word = raw_input('>> ')
        print "\n\nStarting to search collection(s) by fuzzy matching for [ ",key_word," ]\n\n\n"

        matching = []
        matching = [xxx for xxx in all_coll_list if key_word in xxx]
        # print matching
        print "Matching count : ",len(matching)
        print "\n\nMatching result : ",dumps(matching)
        # print "\n\nMatching result :\n\n"
        # pprint(matching)

      elif ans == "n":
        print "Searching collection is over.\n"
        ans = False
        break

      else:
        print "wrong input -_-\n"
        print "Please try again."

############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################


    ### searching document(s) by keyword through all databases and collections.
    print "\n\n\n\n=========================================================="
    print "==================     [4.1] Search database\n"
    print "==================     [4.2] Search collection\n"
    print "================== ==> [4.3] Search filed kye document\n"
    print "==================     [4.4] Search document by filed kye and value\n"
    print "==================     [4.5] Search value from document\n"

    ans="y" ### loop condition of [4.3]
    while not ans ==  "n":
      print "\n\n\nDo you want to search field kye from document(s) ( again )?  'y'(yes) / 'n'(no)"
      ans = raw_input('>> ')
      if ans == "y":
   
        print "\n\n\n================= collection name list from all database =================\n"

        ### select all databases one by one
        database_name_list = client.database_names()
        # print dumps(client.database_names())
        # print "database count : ", len(database_name_list)
        k = 0
        all_kyes_in_docs   = []
        while k < len(database_name_list):
          dbname = database_name_list[k]
          # print dbname
          db = getattr(client, dbname)
  
          coll_name_list = db.collection_names()

          ### show [ collection (database) ] list one by one
          g = 0
          while g < len(coll_name_list):
            collname = coll_name_list[g]
            print collname,"(",dbname,")\n"
            # document = getattr(collname, find)

            ### select all collections one by one
            coll = getattr(db, collname)
            g = g + 1
          k = k + 1 

          ### get all documents
          for xxx in coll.find(): ### dict data
            all_kyes_in_docs.append(xxx.keys()) ### put dtct data by using items() in list

        print "document count :",len(all_kyes_in_docs)
        pprint (all_kyes_in_docs)
        print "\n==================================================="
        print "document count :",len(all_kyes_in_docs)


        ### searching document(s) by keyword through all databases

        print "\n\n\nPlease type some keywords for searching filed keys\n"
        key_word = raw_input('>> ')
        print "\n\nStarting to search field keys from all document by fuzzy matching for [ ",key_word," ]\n\n\n"

        matching = []
        for i in range (0, len(all_kyes_in_docs)):
          matching = [xxx for xxx in all_kyes_in_docs[i] if key_word in xxx]
          print "count :",i+1
          print matching
        # print matching
        # print "Matching count : ",len(matching)
        # print "\n\nMatching result : ",dumps(matching)

      elif ans == "n":
        print "Searching document is over.\n"
        ans = False
        break

      else:
        print "wrong input -_-\n"
        print "Please try again."

############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################


    ### searching document(s) by keyword through all databases and collections.
    print "\n\n\n\n=========================================================="
    print "==================     [4.1] Search database\n"
    print "==================     [4.2] Search collection\n"
    print "==================     [4.3] Search filed kye document\n"
    print "================== ==> [4.4] Search document by filed kye and value\n"    
    print "==================     [4.5] Search value from document\n"

    ans="y" ### loop condition of [4.4]
    while not ans ==  "n":
      print "\n\n\nDo you want to search document by filed kyes and values ( again )?  'y'(yes) / 'n'(no)"
      ans = raw_input('>> ')
      if ans == "y":
   
        print "\n\n\n================= collection name list from all database =================\n"

        ### select all databases one by one
        database_name_list = client.database_names()
        # print dumps(client.database_names())
        # print "database count : ", len(database_name_list)
        k = 0
        all_docs = []
        while k < len(database_name_list):
          dbname = database_name_list[k]
          # print dbname
          db = getattr(client, dbname)
  
          coll_name_list = db.collection_names()

          ### show [ collection (database) ] list one by one
          g = 0
          while g < len(coll_name_list):
            collname = coll_name_list[g]
            print collname,"(",dbname,")\n"
            # document = getattr(collname, find)

            ### select all collections one by one
            coll = getattr(db, collname)
            g = g + 1
          k = k + 1 

          ### get all documents
          for xxx in coll.find(): ### dict data
            all_docs.append(xxx.items()) ### put dtct data by using items() in list

        print "document count :",len(all_docs)
        pprint (all_docs)
        print "\n==================================================="
        print "document count :",len(all_docs)


        ### searching document(s) by keyword through all databases
        print "\n\n\nPlease type a filed kye for searching documents.\n"
        key_word = raw_input('>> ')
        print "\n\nStarting to search all document by matching for [ ",key_word," ]\n\n\n"

        matching = []
        for i in range (0, len(all_docs)):
          matching = [xxx for xxx in all_docs[i] if key_word in xxx]
          print "count :",i+1
          print matching

      elif ans == "n":
        print "Searching document is over.\n"
        ans = False
        break

      else:
        print "wrong input -_-\n"
        print "Please try again."


############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################

##### 뭔가 에러가 난다. 이유를 모르겠다.
##### 키는 문서의 숫자만큼 존재하는데, 밸류는 그렇지 않은 건지
##### all_values_in_docs.append(ppp.values())의 values()의 쓰임을 잘 몰라서 그런건지....


    ### searching document(s) by keyword through all databases and collections.
    print "\n\n\n\n=========================================================="
    print "==================     [4.1] Search database\n"
    print "==================     [4.2] Search collection\n"
    print "==================     [4.3] Search filed kye document\n"
    print "==================     [4.4] Search document by filed kye and value\n"
    print "================== ==> [4.5] Search value from document\n"    

    ans="y" ### loop condition of [4.4]
    while not ans ==  "n":
      print "\n\n\nDo you want to search value from document(s) ( again )?  'y'(yes) / 'n'(no)"
      ans = raw_input('>> ')
      if ans == "y":
   
        print "\n\n\n================= collection name list from all database =================\n"

        ### select all databases one by one
        database_name_list = client.database_names()
        # print dumps(client.database_names())
        # print "database count : ", len(database_name_list)
        k = 0
        all_values_in_docs = []
        while k < len(database_name_list):
          dbname = database_name_list[k]
          # print dbname
          db = getattr(client, dbname)
  
          coll_name_list = db.collection_names()

          ### show [ collection (database) ] list one by one
          g = 0
          while g < len(coll_name_list):
            collname = coll_name_list[g]
            print collname,"(",dbname,")\n"
            # document = getattr(collname, find)

            ### select all collections one by one
            coll = getattr(db, collname)
            g = g + 1
          k = k + 1 

          ### get all documents
          for ppp in coll.find(): ### dict data
            all_values_in_docs.append(ppp.values()) ### put dtct data by using items() in list

        print "document count :",len(all_values_in_docs)
        pprint (all_values_in_docs)
        print "\n==================================================="
        print "document count :",len(all_values_in_docs)

        ### searching document(s) by keyword through all databases
        print "\n\n\nPlease type a value for searching documents\n"
        valule_word = raw_input('>> ')
        print "\n\nStarting to search all document by matching for [ ",valule_word," ]\n\n\n"

        matching = []
        for q in range (0, len(all_values_in_docs)):
          # all_values_in_docs = all_values_in_docs[i]
          # print "###################################"
          # print all_values_in_docs
          # print "###################################"          
          matching = [xxx for xxx in all_values_in_docs[q] if valule_word in xxx]
          print "count :",q+1
          print matching

      elif ans == "n":
        print "Searching document is over.\n"
        ans = False
        break

      else:
        print "wrong input -_-\n"
        print "Please try again."



############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################



  elif ans == "n":
    print "\n\n\nshow database contents is over.\n"
    print "Bye!\n"
    ans = False
    break

  else:
    print "wrong input -_-\n"
    print "Please try again."

###########################################
###########################################
###            ###                      ###
###   Bottom   ###     coded by Jack    ###
###            ###                      ###
###########################################
###########################################

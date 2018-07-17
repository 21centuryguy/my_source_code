# -*- coding: utf-8 -*-
import os
import Tkinter, tkFileDialog
from config import *
import difflib
import distutils.dir_util

def diff_that_damnit(current_data_time):

##################################################################### 
##### select before and after folder and get file list
	root = Tkinter.Tk()
	root.withdraw()

#####################################################

	def select_folder_and_get_file_list():
		######################################################################
		##### select before folder and get file list
		##### select before folder
		print "\n\n\n>"
		print "=>"
		print "==>>"
		print "===>>>"
		print "====>>>>"
		print "=====>>>>>   Please select [ Befre folder ] for checking html diff status from OS UI.\n\n\n"

		before_folder_path = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
		file_list_in_before_folder = os.listdir(before_folder_path)
		file_list_in_before_folder.sort()
		file_list_in_before_folder

		##### get file list
		file_count = len(file_list_in_before_folder)
		print "\n\n============ [ before folder path and file list ] ============"
		print "\nBefore folder path :",before_folder_path 
		print "\nFile list in the before folder :", file_list_in_before_folder
		print "\nTotal file count :", file_count


		######################################################################
		##### select after folder and get file list
		##### select after folder
		path_info = pass_path_info(current_data_time)
		folder_path_1 = path_info[0]
		folder_list_in_the_crawled_html_files = os.listdir(folder_path_1)
		folder_list_in_the_crawled_html_files.sort()
		folder_list_in_the_crawled_html_files.pop(0) ### delete '.DS_Store'
		folder_list_in_the_crawled_html_files.pop(-1) ### delete 'diff_result'
		# print folder_list_in_the_crawled_html_files

		last_folder_in_the_crawled_html_files = folder_list_in_the_crawled_html_files[-1]
		last_folder_in_the_crawled_html_files_path = folder_path_1 + last_folder_in_the_crawled_html_files

		##### get file list
		file_list_in_the_last_folder = os.listdir(last_folder_in_the_crawled_html_files_path)
		file_list_in_the_last_folder.sort()
		file_count = len(file_list_in_the_last_folder)
		print "\n\n============ [ after folder path and file list ] ============"
		print "\nLast folder path :", last_folder_in_the_crawled_html_files_path
		print "\nFile list in the last folder :", file_list_in_the_last_folder
		print "\nTotal file count :", file_count	

		return before_folder_path, file_list_in_before_folder, file_count, last_folder_in_the_crawled_html_files_path, file_list_in_the_last_folder




	def compare_before_and_after_folder(*arg):
		######################################################################
		##### diff each file in before folder and after folder

		print "\n\n\n\n\n[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]\n"
		print "            [[[[[[[  Diff checking  ]]]]]]]            \n"
		print "[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]\n"
		m = 0
		while m < file_count:

			############### diff one by one ###############
			before_file_full_path = before_folder_path + "/" + file_list_in_before_folder[m]
			after_file_full_path = last_folder_in_the_crawled_html_files_path + "/" + file_list_in_the_last_folder[m]

			print "\n\n============ [ before file ( " + str(m+1) + " ) ] ============\n"
			print before_file_full_path

			print "\n\n============ [ after file ( " + str(m+1) + " ) ] ============\n"
			print after_file_full_path

			with open(before_file_full_path) as before, open(after_file_full_path) as after:
				diff = difflib.context_diff(before.readlines(), after.readlines())
			
			############### save diff result ###############
			path_info = pass_path_info(current_data_time)
			folder_path_1 = path_info[0]

			before_folder_name = before_folder_path.replace(folder_path_1, ' ')
			after_folder_name = last_folder_in_the_crawled_html_files_path.replace(folder_path_1, ' ')
			before_file_name = file_list_in_before_folder[m].replace(folder_path_1, ' ')
			after_file_name = file_list_in_the_last_folder[m].replace(folder_path_1, ' ')

			diff_result_folder_path = folder_path_1 + "/diff_result/" +"diff"+ after_folder_name +"_"+ before_folder_name
			distutils.dir_util.mkpath(diff_result_folder_path)
			diff_result_fullpath = diff_result_folder_path +"/"+ before_folder_name+"-"+after_folder_name +"_"+ file_list_in_before_folder[m]+"_diff_resutl.txt"		
			with open(diff_result_fullpath, 'w') as diff_result:
				for line in diff:
					diff_result.write(line)

			############### report diff result ###############

			diff_result_size = os.path.getsize(diff_result_fullpath)
			
			if diff_result_size == 0: 
				print "\n>"
				print "=>"
				print "==>>"
				print "===>>>"
				print "====>>>>"
				print "=====>>>>>   [ Diff checking count : " + str(m+1)+" ] : [ "+ before_folder_name +"_"+ before_file_name +" ]"+ " and " + "[ "+ after_folder_name +"_"+ after_file_name + " ] is\n"
				print ">>>>>>>>>>>>><<<<<<<<<<<"
				print ">>>>>>>>>>>>><<<<<<<<<<<"
				print ">>>>>>>   SAME  <<<<<<<"
				print ">>>>>>>>>>>>><<<<<<<<<<<"
				print ">>>>>>>>>>>>><<<<<<<<<<<\n"

			else:
				print "\n>"
				print "=>"
				print "==>>"
				print "===>>>"
				print "====>>>>"				
				print "=====>>>>>   [ Diff checking count : " + str(m+1)+" ] : [ "+ before_folder_name +"_"+ before_file_name +" ]"+ " and " + "[ "+ after_folder_name +"_"+ after_file_name + " ] is\n"
				print ">>>>>>>>>>>>><<<<<<<<<<<"
				print ">>>>>>>>>>>>><<<<<<<<<<<"
				print ">>>>>>> NOT SAME <<<<<<<"
				print ">>>>>>>>>>>>><<<<<<<<<<<"
				print ">>>>>>>>>>>>><<<<<<<<<<<\n"

			m = m + 1

######################################################################
	xxx = select_folder_and_get_file_list()
	xxx = list(xxx)
	before_folder_path = xxx[0]
	file_list_in_before_folder = xxx[1]
	file_count = xxx[2]
	last_folder_in_the_crawled_html_files_path = xxx[3]
	file_list_in_the_last_folder = xxx[4]

	compare_before_and_after_folder(before_folder_path, file_list_in_before_folder, file_count, last_folder_in_the_crawled_html_files_path, file_list_in_the_last_folder)

######################################################################

if __name__ == "__main__":
	pass

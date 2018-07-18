# -*- coding: utf-8 -*-
import distutils.dir_util

def pass_path_info(current_data_time):
	folder_path_2 = "/Users/jack/Documents/GitHub/my_source_code/tools/python/check_paradox_html/crawled_html_files/"+current_data_time+"/"
	distutils.dir_util.mkpath(folder_path_2)
	
	folder_path_1 = "/Users/jack/Documents/GitHub/my_source_code/tools/python/check_paradox_html/crawled_html_files/"
	
	return folder_path_1, folder_path_2

if __name__ == "__main__":
	pass


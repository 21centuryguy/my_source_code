target_builtin_lib_path_list = []
# target_builtin_lib_path_list = ["/Users/jack/miniconda2/envs/py27/lib/python2.7/"]

"""
# --------------------------------
# --- target_builtin_lib_path_list

target_builtin_lib_path_list = [
								"/Users/jack/miniconda2/envs/py27/lib/python2.7/", 
								"/Users/jack/miniconda2/envs/py36/lib/python3.6/", 
								"/Users/jack/miniconda2/envs/py37/lib/python3.6/"
							]
"""

# --------------------------------
# --- func definition

import tkinter, tkinter.filedialog

def get_target_builtin_lib_path():
	root = tkinter.Tk()
	root.withdraw()

	target_builtin_lib_path = tkinter.filedialog.askdirectory(parent=root,initialdir="/Users/jack/miniconda2/envs/",title='Please select a directory')

	target_builtin_lib_path_list.append(target_builtin_lib_path)

	return target_builtin_lib_path_list

if __name__ == '__main__':
	get_target_builtin_lib_path()

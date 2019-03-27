import re

xxx = "/Users/jack/miniconda2/envs/py37/lib/python3.6/site-packages/aenum/__init__.py"

"""
sep = "/"
last_checked_module_path = last_checked_module_file_path.split(sep)[:-1]
print(last_checked_module_path)
last_checked_module_path = last_checked_module_path[0]
print(last_checked_module_path)
"""

yyy = xxx.rfind("/")
yyy = xxx[0:66]
print(yyy)

# xxx = re.sub("[/.*.py]", "", xxx)
# print(xxx)
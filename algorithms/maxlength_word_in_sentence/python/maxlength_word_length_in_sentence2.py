import tkinter as tk
from tkinter import simpledialog

### input
application_window = tk.Tk()
string = simpledialog.askstring("Input", ">>> type of paste here some string",parent=application_window)
string = string.encode('ascii', 'ignore')
string = string.decode('ascii')
string = string.encode('utf-8', 'ignore')
string = string.decode('utf-8')
print(">"*15 + "   string after removing some unsurppoted characters   " + "<"*15)
print(string)
print("\n")

### remove line breake
string = string.replace('\n', ' ').replace('\r', '').replace(',', '')
print(">"*15 + "   string after removing line breake, some punctuations   " + "<"*15)
print(string)
print("\n")

### split with dot
word_list = string.split(".") # word_list = string.split("\n")
try:
	word_list.remove("")
except Exception :
	pass
print(">"*15 + "   2list after spliting with dot   " + "<"*15)
print(word_list)
print(len(word_list))
print("\n")

### split with space
target_word_list = []
for word in word_list:
	word_list = word.split(" ")
	target_word_list = target_word_list + word_list
print(">"*15 + "   list after spliting with space   " + "<"*15)
print(target_word_list)
print(len(target_word_list))
print("\n")

print(">"*15 + "   Result   " + "<"*15)
### find max length word
i = 0
max_length = 0
for word in target_word_list:
	if len(word) > max_length:
		max_length = len(word)
		max_length_word = word
		print(">>>   count : " + str(i) + " / " + "word : [ " + max_length_word + " ] / " + "length : " + str(len(max_length_word)))
	else:
		pass
	i = i + 1

print("="*50)
print(">>> max_length_word : [ " + max_length_word + " ]")
print(">>> max_length : ", len(max_length_word))

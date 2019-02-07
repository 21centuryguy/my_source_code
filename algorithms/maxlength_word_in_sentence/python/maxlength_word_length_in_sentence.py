string = input(">>> type of paste here some string : ")
string = string.encode('ascii', 'ignore')
string = string.decode('ascii')
string = string.encode('utf-8', 'ignore')
string = string.decode('utf-8')



word_list = string.split("\n")
# print(word_list)

i = 0
max_length = 0
for word in word_list:
	word_list = string.split(" ")
	for word in word_list:
		if len(word) > max_length:
			max_length = len(word)
			max_length_word = word.replace("\n", "")
			# print("count : " + str(i) + " / " + "word : [ " + max_length_word + " ] / " + "length : " + str(len(max_length_word)))
		else:
			pass
		i = i + 1
print("="*50)
print(">>> max_length_word : [ ", max_length_word + " ]")
print(">>> max_length : ", len(max_length_word))





"""
word_list = string.split("\n")
# word_list = string.split(" ")
# print(word_list)

i = 0
max_length = 0
for word in word_list:
	if len(word) > max_length:
		max_length = len(word)
		max_length_word = word
	else:
		pass
	i = i + 1
	# print("count : " + str(i) + " / " + "word : [ " + word + " ] / " + "length : " + str(len(word)))
print("="*50)
print("max_length_word : ", max_length_word)
print("max_length : ", max_length)
"""



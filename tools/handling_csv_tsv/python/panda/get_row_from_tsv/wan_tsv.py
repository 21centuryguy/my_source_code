import pandas as pd

############################

trans_result = "aldjfkjdfljkljdsfl ccc adkjflkdsjflj aldjflkjdflj iii adlkjflkjfd ooo adljflkjds lll jfjyfghjf fff"

# file_path = "/Users/jack/Desktop/xxx.tsv"
file_path = "/Users/jack/Documents/GitHub/my_source_code/tools/python/panda/get_row_from_tsv/xxx.csv"

############################

if "tsv" in file_path:
	df = pd.read_csv(file_path, sep='\t', header=None)

if "csv" in file_path:
	df = pd.read_csv(file_path, sep=',', header=None)

print (df)
print ("\n")
row_len = (len(df.index)) - 1
# print (row_len)

row_list = []
i = 1
while i <= row_len:
	# print (df.at[i,2])
	row_list.append(df.at[i,2])
	i = i + 1

i = 1
for xxx in row_list:
	if xxx in trans_result:
		print("ud entry",i, " : [ ",xxx ," ] is IN trans result. ( OK ! )")
	else:
		print("ud entry",i, " : [ ",xxx ," ] is NOT IN trans result.( NG -_-; )")
	i = i + 1
print ("\n")


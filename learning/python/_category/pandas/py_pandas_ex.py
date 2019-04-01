import pandas as pd

# --------- read data as panda DataFrame
pd_DataFrame = pd.read_csv('example.csv', delimiter = ',')
print("#"*50)
print(pd_DataFrame)
print("#"*50)
print("\n\n\n")

# --------- funcdion definition
def csv_panda_columns():
	csv_panda_columns = pd_DataFrame.columns
	print("pd_DataFrame.columns : \n\n", pd_DataFrame.columns)

	my_list1=[]
	for column in csv_panda_columns:
		my_list1.append(column)
	print("my_list1 :", my_list1)

	my_list0=['aaa', 'bbb', 'ccc', 'ddd']
	print("my_list0 :", my_list0)

	assert my_list0 == my_list1, "they are not same -_-;"
	print("They are same !")

def csv_panda_head():
	csv_panda_head = pd_DataFrame.head
	print("pd_DataFrame.head : \n\n", csv_panda_head(3))

def csv_panda_tail():
	csv_panda_tail = pd_DataFrame.tail
	print("pd_DataFrame.tail : \n\n", csv_panda_tail(3))

def csv_panda_sample():
	csv_panda_sample = pd_DataFrame.sample(3)
	print("pd_DataFrame.sample : \n\n", csv_panda_sample)

def csv_panda_sample():
	csv_panda_sample = pd_DataFrame.sample(3)
	print("pd_DataFrame.sample : \n\n", csv_panda_sample)

def csv_panda_specific_column():
	csv_panda_some_column =  pd_DataFrame['aaa']
	print("pd_DataFrame['aaa'] : ", csv_panda_some_column)

def csv_panda_specific_columns():
	csv_panda_some_column =  pd_DataFrame[['aaa', 'ddd']]
	print("pd_DataFrame[['aaa', 'ddd']] : ", csv_panda_some_column)



# --------- call functions
# csv_panda_columns()
# csv_panda_head()
# csv_panda_tail()
# csv_panda_sample()
# csv_panda_specific_column()
csv_panda_specific_columns()



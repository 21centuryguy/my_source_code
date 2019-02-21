def func_a():
    print("This is message from func_a.")

func_a()

##############################

b = func_a

b()

##############################

func_c = func_a

def func_c():
	c = 100
	print("c : "+str(c*100))

func_c()

##############################

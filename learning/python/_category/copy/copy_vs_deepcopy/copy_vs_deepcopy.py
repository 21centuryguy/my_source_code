import copy

def copy_ex():
	a = [[1, 2], [3, 4]]
	b = copy.copy(a)
	print("="*25 + "  copy example  " + "="*25)
	print ("a = [[1, 2], [3, 4]] => a = %s" % a)
	print ("b = copy.copy(a) => b = %s" % b)

	a[1].append(5)

	print("\n"+ "="*20 + "  a[1].append(5)  " + "="*20)
	print ("a = [[1, 2], [3, 4]] => a = %s" % a)
	print ("b = copy.copy(a) => b = %s" % b)

	print("\n"+ "="*10 + "  id check  " + "="*10)
	print ("id(a) = %i" % id(a))
	print ("id(b) = %i" % id(b))

	print ("id(a[0]) = %i" % id(a[0])) # 追加行
	print ("id(b[0]) = %i" % id(b[0])) # 追加行

	print ("id(a[1]) = %i" % id(a[1])) # 追加行
	print ("id(b[1]) = %i" % id(b[1])) # 追加行

def deepcopy_ex():
	a = [[1, 2], [3, 4]]
	b = copy.deepcopy(a) #変更行
	print("\n\n"+"="*25 + "  deepcopy example  " + "="*25)
	print ("a = [[1, 2], [3, 4]] => a = %s" % a)
	print ("b = copy.deepcopy(a) => b = %s" % b)

	a[1].append(5)
	print("\n"+ "="*20 + "  a[1].append(5)  " + "="*20)
	print ("a = [[1, 2], [3, 4]] => a = %s" % a)
	print ("b = copy.deepcopy(a) => b = %s" % b)

	print("\n"+ "="*10 + "  id check  " + "="*10)
	print ("id(a) = %i" % id(a))
	print ("id(b) = %i" % id(b))

	print ("id(a[0]) = %i" % id(a[0]))
	print ("id(b[0]) = %i" % id(b[0]))

	print ("id(a[1]) = %i" % id(a[1]))
	print ("id(b[1]) = %i" % id(b[1]))

copy_ex()

deepcopy_ex()

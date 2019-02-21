class Restaurant(object):
	bankrupt = False
	def open_branch(self):
		if not self.bankrupt:
			print("branch opend")
		else:
			print("branch not opend")

x = Restaurant()
x.bankrupt
xxx = x.open_branch()
print ("1 : ",x.bankrupt)
print ("2 : ",xxx)


y = Restaurant()
y.bankrupt = True
yyy = y.open_branch()
print ("3 : ",y.bankrupt)
print ("4 : ",yyy)


z = Restaurant()
# zz = z.bankrupt
zzz = z.open_branch()
# print (zz)
print ("5 : ",zzz)

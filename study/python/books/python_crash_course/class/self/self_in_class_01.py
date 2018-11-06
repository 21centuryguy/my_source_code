class Restaurant(object):
	bankrupt = False
	def open_branch(self):
		if not self.bankrupt:
			print("branch opend")

x = Restaurant()
xx = x.bankrupt # ( = Restaurant().bankrupt )
print (xx)

y = Restaurant()
y.bankrupt = True
print (y.bankrupt)

print (x.bankrupt)
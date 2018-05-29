def main():

	p = [1,2,3,4]

	def proc1(p):
		print "========= proc 1 ========="
		print p[0]
		p[0] = p[1]
		print p[0]


	def proc2(p):
		print "========= proc 2 ========="
		print p
		p = p + [1]
		print p

	def proc3(p):
		print "========= proc 3 ========="		
		print p
		q = p
		p.append(3)
		q.pop()
		print p

	def proc4(p):
		print "========= proc 4 ========="		
		print p
		q = []
		while p:
			q.append(p.pop())
		while q:
			p.append(q.pop())
		print p


	proc1(p)
	proc2(p)
	proc3(p)
	proc4(p)


main()
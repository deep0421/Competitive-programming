def binn(n):
	a=[]
	for i in range(n+1):
		lo=bin(i)
		m1=0
		for j in range(len(lo)):
			if(lo[j]=='1'):
				m1+=1
		a.append(m1)
	print(a)
binn(15)
binn(16)
binn(1)
binn(25)
binn(5)
binn(6)		



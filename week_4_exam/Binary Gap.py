def binn(a):
	h=bin(a)
	max1=0
	m1=0
	# print(abc)
	for i in range(len(h)):
		if(h[i]=='1'):
			m1+=1
		else:
			if(max1<m1):
				max1=m1
				m1=0
	print(max1)

binn(22)
binn(0)
binn(55)
binn(-5)
binn(12354)
binn(6)
binn(256)





def com(a,b):
	a1=len(a)
	a2=len(b)
	j=0
	z=0
	zmax=0
	a=a.lower()
	b=b.lower()
	a="".join(sorted(a))
	b="".join(sorted(b))
	if(a1>a2):
		for i in range(a1-1):
			x=i
			if(a[i]==b[j]):
				i+=1
				j+=1
				z=1
				while(a[i]==b[j]):
					z+=1
					i+=1
					j+=1
					if(j>a2-1):
						break
			if(z>zmax):
				zmax=z
			i=x
			j=0
		if(zmax==a2):
			print('true')
		else:
			print('flase')
	else:
		for i in range(a2-1):
			x=i
			if(b[i]==a[j]):
				i+=1
				j+=1
				z=1
				while(b[i]==a[j]):
					z+=1
					i+=1
					j+=1
					if(j>a1-1):
						break
			if(z>zmax):
				zmax=z			
			i=x
			j=0
		if(zmax==a1):
			print('true')
		else:
			print('flase')


com('anagram','nagaram')
com('Keep','Peek')
com('Mother In Law','Hitler Woman')
com('School Master','The Classroom')
com('ASTRONOMERS','NO MORE STARS')
com('Toss','Shot')
com('joy','enjoy')
com('Debit Card','Bad Credit')
com('SiLeNt CAT','LisTen AcT')
com('Dormitory','Dirty Room')


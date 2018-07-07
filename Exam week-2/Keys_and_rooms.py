def key(l1):
	l=len(l1)
	d={}
	flag=1
	h=0
	for i in range(l):
		d[i]=0
	d[0]=1
	for i in range(l):
		if(d[i]==1):
			if(len(l1[i])>=1):
				for j in range(len(l1[i])):
					if(l1[i][j]<len(l1)):
						d[l1[i][j]]=1
			else:
				if(l1[i]==[]):
					h=0
				else:
					if(l1[i]<len(l1)):
						d[l1[i]]=1
				
	for i in range(l):
		if(d[i]==0):
			flag=0
	if(flag==0):
		print("False")
	else:
		print("True")

key([[1],[0,2],[3]])
key([[1,3],[3,0,1],[2],[0]]) 
key([[1,2,3],[0],[0], [0]])
key([[1],[0,2,4],[1,3,4],[2],[1,2]])
key([[1],[2,3],[1,2],[4],[1],[5]])
key([[1],[2],[3],[4],[2]])
key([[1],[1,3],[2],[2,4,6],[],[1,2,3],[1]])
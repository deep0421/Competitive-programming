def mors(y):
	x=""
	z=[]
	morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
	alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for aq in range(len(y)):
		x=""
		for i in range(len(y[aq])):
			for ye in range(len(alp)):
				if(y[aq][i]==alp[ye]):
					x=x+morse[ye]
		if x not in z:			
			z.append(x)
	print(len(z))

mors(["gin", "zen", "gig", "msg"])
mors(["a", "z", "g", "m"])
mors(["bhi", "vsv", "sgh", "vbi"])  
mors(["a", "b", "c", "d"])  
mors(["hig", "sip", "pot"])  
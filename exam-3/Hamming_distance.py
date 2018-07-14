def hamming(a,b):
	h=0
	y='{0:08b}'.format(a)
	z='{0:08b}'.format(b)
	for i in range(len(y)):
		if(y[i]!=z[i]):
			h+=1
	print(h)

hamming(25,30)
hamming(1,4)
hamming(25,30)
hamming(100,250)
hamming(1,30)
hamming(0,255)

from math import factorial


def combinatoria(n, k):
	return factorial(n) // (factorial(k) * factorial(n - k))

def punto1y2(a,b):
	vec = []
	vec1 = []
	for i in range(a,b+1):
		
		if (len(str(i))<=1):
			vec.append(i)
		if(len(str(i))>1):
			des = []
			st = str(i)
			k = 0 
			l = 0
			sw = True
			for j in range(0,len(st)):
				des.append(st[j:j+1])
			
			while(k<len(des)):
				while(l<len(des)):
					if(des[k]==des[l] and k!=l):
						sw = False
						break
					l+=1
				if(sw==False):
					break
				k+=1
				l=0
				
			if(sw==True):
				vec.append(i)
		st = str(i) 
		if(not("0" in st)):
			vec1.append(i)

	print("Numeros con digitos diferentes: ")    
	print(vec)
	print("Numeros distinto de 0: ")
	print(vec1)
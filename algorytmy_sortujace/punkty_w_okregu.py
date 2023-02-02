def bucket_sort(T, k):
	n = len(T)
	B = [ [] for _ in range(n+1) ]
	p_i = k*k/n

	for i in range(n):
		x,y = T[i]
		p = x*x + y*y
		ind = int(p/p_i)
		insertion(B[ind],T[i])
	
	x = 0
	for i in range(n+1):
		for j in range(len(B[i])):
			T[x] = B[i][j]
			x+=1

	return T



def insertion(T, el):
	n = len(T)
	
	if n > 0:
		x,y = el
		p1 = x*x + y*y
		T.append(T[n-1])
		
		for i in range(n, 0, -1):
			x,y = T[i]
			p2= x*x + y*y
			
			if p2 < p1:
				T[i] = el
				return T
			else:
				T[i-1] = T[i-2]
		
		T[0] = el
	else:
		T.append(el)

	return T

T = [(5,0),(0,5),(0,0),(2,2),(-5,0),(0,3),(1,3),(3,2),(0,-5),(-2,2),(1,2),(0,2),(-1,2)]
k = 5

print(bucket_sort(T,k))

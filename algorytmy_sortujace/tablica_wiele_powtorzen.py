def insertion(T, el):
	n = len(T)
	
	if T[n-1][0] < el:
		T.append([el, 1])	
	else:
		l = 0
		p = n -1
		flag = 1

		while p >= l:
			s = (p+l)//2
		
			if T[s][0] == el:
				T[s][1] +=1
				flag = 0
				break
		
			elif  T[s][0] > el:
				p = s-1
			else:
				l = s+1
		if flag:
			T.append([T[n-1][0],T[n-1][1]])
			for i in range(n, l, -1):
				T[i][0] = T[i-1][0]
				T[i][1] = T[i-1][1]
			T[l][0] = el
			T[l][1] = 1

def counting_sort(T):
	n = len(T)
	unikaty = [[T[0],1]]

	for i in range(1,n):
		insertion(unikaty, T[i])

	u = len(unikaty)
	x = 0
	for i in range(u):
		for j in range(unikaty[i][1]):
			T[x] = unikaty[i][0]
			x+=1
	return T

A = [0,0,0,0,0,5,2,1,1,5,3,3,1,5,1,2,5]

print(counting_sort(A))
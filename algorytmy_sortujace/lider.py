def lider(T):
	n = len(T)
	count = 1
	lider = 0
	
	for i in range(1,n):
		if count == 0:
			lider = i
			count = 1
		else:
			if T[i] != T[lider]:
				count-=1
			else:
				count+=1
	
	if count > 0:
		count = 0
	

		for i in range(n):
			if T[i] == T[lider]:
				count+=1

		if count > n//2:
			return T[lider]

	return None

A = [1,2,1]

print(lider(A))

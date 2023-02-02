def counting_sort(T, k):
	n = len(T)

	lower = []
	grater = []
	C = [ 0 for _ in range(k+1) ]
	B = [ 0 for _ in range(n) ]
	
	for i in range(n):
		if T[i] < 0:
			lower = insertion(lower, T[i])
		elif T[i] > k:
			grater = insertion(grater, T[i])
		else:
			C[T[i]] +=1
	
	for i in range(1, k+1):
		C[i] += C[i-1]

	l = len(lower)
	g = len(grater)

	for i in range(0, l):
		B[i] = lower[i]
	for i in range(0, g):
		B[n-g+i] = grater[i]
	for i in range(n-1,-1,-1):
		if T[i] >= 0 and T[i] <= k:
			C[T[i]] -= 1
			B[C[T[i]]+l] = T[i]

	return B

def insertion(T, el):
	n = len(T)

	if n > 0:
		T.append(T[n-1])
		
		for i in range(n, 0, -1):
			if T[i] < el:
				T[i] = el
				return T
			else:
				T[i-1] = T[i-2]
		
		T[0] = el
	
	else:
		T.append(el)

	return T

A = [ 1, -1, 2, 111, 3, -10, 4, 3, 6, 7, 9, -5, 10, 11, -2, 12, -9, -4, 14]

k = 10

print(counting_sort(A,k))



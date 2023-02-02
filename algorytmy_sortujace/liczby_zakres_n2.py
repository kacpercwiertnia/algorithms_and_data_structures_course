def counting_sort(T, f):
	
	n = len(T)
	
	C = [ 0 for _ in range(n) ]
	B = [ 0 for _ in range(n) ]

	if(f == 0):
		for i in range(n):
			C[T[i]%n]+=1
	
		for i in range(1,n):
			C[i] += C[i-1]

		for i in range(n-1, -1, -1):
			C[T[i]%n] -= 1
			B[C[T[i]%n]] = T[i]
		
	if(f == 1):
		for i in range(n):
			C[T[i]//n]+=1
	
		for i in range(1,n):
			C[i] += C[i-1]

		for i in range(n-1, -1, -1):
			C[T[i]//n] -= 1
			B[C[T[i]//n]] = T[i]
	
	return B

def radix_sort(T):
	T = counting_sort(T,0)
	T = counting_sort(T,1)
	
	return T


T = [1, 99, 56, 15, 25, 56, 41, 39, 2, 69]

print(radix_sort(T))
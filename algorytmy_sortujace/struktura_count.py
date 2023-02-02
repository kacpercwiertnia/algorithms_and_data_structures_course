def dystrybuanta(A,k):	

	C = [ 0 for _ in range(k+2) ]
	n = len(A)

	for i in range(n):
		C[A[i]+1] += 1
	
	for i in range(1, k+2):
		C[i] += C[i-1]

	return C

def count_num_in_range(A, a, b):
	return A[b+1] - A[a]

k = 10

A = [0, 1, 4, 6, 8, 9, 10, 4, 4, 5, 7, 2, 6]

D = dystrybuanta(A,k)

print(D)

print(count_num_in_range(D,0,10))


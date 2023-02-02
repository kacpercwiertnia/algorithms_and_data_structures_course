def counting_sort(A, k):
	n = len(A)
		
	C = [ 0 for _ in range(k) ]
	B = [ 0 for _ in range(n) ]

	for x in A:
		C[x] += 1
	
	for i in range(1, k):
		C[i] += C[i-1]
	
	for i in range(n-1, -1, -1):
		C[A[i]] -= 1
		B[C[A[i]]] = A[i]
	
	for i in range(n):
		A[i] = B[i]

A = [10, 1, 9, 6, 2, 3, 4, 8, 7, 5, 0]
k = 11

print(A)
counting_sort(A, k)
print(A)
		
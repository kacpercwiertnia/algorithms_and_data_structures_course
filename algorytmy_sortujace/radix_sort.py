def counting_sort(A, k, p):
	n = len(A)
	
	B = [ 0 for _ in range(n) ]
	C = [ 0 for _ in range(k) ]
	
	shift = ord('a')

	for X in A:
		C[ord(X[p])-shift]+=1
	
	for i in range(1, k):
		C[i] += C[i-1]
	
	for i in range(n-1, -1, -1):
		C[ord(A[i][p])-shift] -= 1
		B[C[ord(A[i][p])-shift]] = A[i]
	
	for i in range(n):
		A[i] = B[i]

def radix_sort(A, k):
	
	for i in range(k-1, -1, -1):
		counting_sort(A, 26, i)


A = ["adbac", "abbac", "aaaaa", "baabd", "dbaca", "acbad", "baaca", "bcaab", "baaaa", "ababa", "barca", "cabca", "ccccc", "aabaa", "cacac"]

print(A)
radix_sort(A,5)
print(A)
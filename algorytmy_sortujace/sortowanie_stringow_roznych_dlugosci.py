def bucket_sort(T,n):

	b = len(T)
	
	B = [ [] for _ in range(n) ]

	for i in range(b):
		B[len(T[i])-1].append(T[i])

	for i in range(n):
		if( len(B[i])>0):
			radix_sort(B,i,i)
	
	for i in range(n-1, 0, -1):
		B[i-1].extend(B[i])
		radix_sort(B,i-1,i-1)

	for i in range(len(B[0])):
		T[i] = B[0][i]
	
	return T

def radix_sort(T,ind,limit):
	
	for i in range(ind+1):
		counting_sort(T[ind],limit-i)


def counting_sort(T,ind):
	
	n = len(T)

	C = [ 0 for _ in range(26) ]
	B = [ None for _ in range(n) ]
	
	for i in range(n):
		C[ ord(T[i][ind]) - ord('a') ] += 1
	
	for i in range(1,26):
		C[i] += C[i-1]
	
	for i in range(n-1, -1, -1):
		x = ord(T[i][ind]) - ord('a')
		C[x] -= 1
		B[C[x]] = T[i]
	
	for i in range(n):
		T[i] = B[i]

	return T
n = 14
S = ["aca", "abd", "d", "eaaca", "ad"]

print(bucket_sort(S,n))
def partition(A, l, r):
	x = A[r]
	i = l-1
	
	for j in range(l, r):
		if A[j] <= x:
			i += 1
			A[i], A[j] = A[j], A[i]
	
	A[i+1], A[r] = A[r], A[i+1]
	return i+1
	
def select(A, p, k, r):
	if p == r:
		return A[p]
	
	if p < r:
		q = partition(A, p, r)
	
		if q == k:
			return A[q]
		elif q < k:
			return select(A, q+1, k, r)
		else:
			return select(A, p, k, q-1)


A = [14, 2, 12, 6, 5, 3, 15, 7, 8]
print(A)
print(select(A,0, (len(A)-1)//2, len(A)-1))











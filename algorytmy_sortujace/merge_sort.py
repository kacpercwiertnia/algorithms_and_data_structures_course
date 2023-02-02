def merge(A, l, s, p):
	k = l
	L = A[l:s]
	P = A[s:p+1]
	i = 0
	j = 0
	l_stop = s-l
	p_stop = p+1-s
	
	while i < l_stop and j < p_stop:
		if L[i] < P[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = P[j]
			j += 1
		k += 1
	
	while i < l_stop:
		A[k] = L[i]
		i += 1
		k += 1
	
	while j < p_stop:
		A[k] = P[j]
		j += 1
		k += 1

def sort(A, l, p):
	s = (l+p+1)//2
	
	if p-l == 1:
		merge(A, l, s, p)
	elif p-l > 1:
		sort(A, l, s)
		sort(A, s, p)
		merge(A, l, s, p)

A = [1, 20, 100, 3, 0, 21, 11, 15, 2, 4, 3]

print(A)
sort(A, 0, len(A)-1)
print(A)
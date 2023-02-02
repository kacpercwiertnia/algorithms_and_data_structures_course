A = [2, 1, 3, 2, 1, 0]

def zadanie(A):
	n = len(A)
	T = [ 0 for _ in range(n) ]
	
	T[0] = 1

	for i in range(n):
		for j in range(A[i]):
			T[i+1+j] += T[i]

	return T[n-1]

print(zadanie(A))
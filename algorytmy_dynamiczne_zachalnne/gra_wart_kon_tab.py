A = [9, 5, 1, 2, 3]


def f(A, F, i, j):
	
	if i > j:
		return 0

	if F[j-i] != -1:
		return F[j-i]
	
	F[j-i] =  max(A[i]+min(f(A,F,i+2,j),f(A,F,i+1,j-1)), A[j]+min(f(A,F,i+1,j-1),f(A,F,i,j-2)))

	print(F)

	return F[j-i]
	

def zadanie(A):
	n = len(A)
	F = [ -1 for _ in range(n) ]
	
	return f(A, F, 0, n-1)

print(zadanie(A))
from zad5ktesty import runtests

def f(A, a, b, D):
	if a > b:
		return 0
	
	if D[a][b] != -1:
		return D[a][b]

	if a == b:
		D[a][b] = (A[a], 0)
		return D[a][b]
	
	if a+1 == b:
		D[a][b] = (max(A[a], A[b]), min(A[a], A[b]))
		return D[a][b]
	
	w1 = f(A, a+1, b, D)
	w2 = f(A, a, b-1, D)
	
	if A[a] + w1[1] > A[b] + w2[1]:
		D[a][b] = (A[a]+w1[1], w1[0])
	else:
		D[a][b] = (A[b]+w2[1], w2[0])
	
	return D[a][b]
		
def garek ( A ):
	n = len(A)
	
	D = [ [-1 for _ in range(n) ] for _ in range(n) ]
	
	res = f(A, 0, n-1, D)

	return res[0]

runtests ( garek )
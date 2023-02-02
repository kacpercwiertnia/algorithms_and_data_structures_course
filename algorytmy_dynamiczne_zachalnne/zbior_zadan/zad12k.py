from zad12ktesty import runtests

def f(D, S, k, koniec):
	if koniec == -1:
		return 0
	
	if D[koniec][k] != -1:
		return D[koniec][k]

	if k == 1:
		D[koniec][k] = S[0][koniec]
		return D[koniec][k]

	if koniec == 0:
		D[koniec][k] = S[0][0]

	minn = float('inf')
	
	for j in range(koniec, -1, -1):
		val = max(S[j][koniec], f(D, S, k-1, j-1))
		
		if val < minn:
			minn = val
	D[koniec][k] = minn
	return D[koniec][k]
				

def autostrada( T, k ):
	n = len(T)

	S = [ [ 0 for _ in range(n) ] for _ in range(n) ]
	D = [ [ -1 for _ in range(k+1) ] for _ in range(n) ]
	
	for x in range(n):
		S[x][x] = T[x]
	
	for y in range(n):
		for x in range(y+1, n):
			S[y][x] = S[y][x-1] + T[x]

	return f(D, S, k, n-1)

runtests ( autostrada,all_tests=True )
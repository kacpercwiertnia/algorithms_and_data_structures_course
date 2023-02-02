from zad4ktesty import runtests

def f(A, DP, x, y):

	if DP[y][x] is not None:
		return DP[y][x]
	
	if y == 0 and x == 0:
		DP[y][x] = A[y][x]
		return DP[y][x]
	
	if y == 0:
		DP[y][x] = f(A, DP, x-1, y) + A[y][x]
		return DP[y][x]
	
	if x == 0:
		DP[y][x] = f(A, DP, x, y-1) + A[y][x]
		return DP[y][x]
	
	DP[y][x] = min(f(A, DP, x-1, y), f(A, DP, x, y-1))+A[y][x]
	return DP[y][x]

def falisz ( T ):
	n = len(T)	
	DP = [ [ None for _ in range(n) ] for _ in range(n) ]

	return f(T, DP, n-1, n-1)

runtests ( falisz )
from zad1ktesty import runtests

def val(S, k):
	if S[k] == '0':
		return 1
	
	return -1

def f(S, DP, p, k):
	if p > k:
		return 0
	
	if DP[p][k] is not None:
		return DP[p][k]
	
	DP[p][k] =  f(S, DP, p, k-1) + val(S,k)
	
	return DP[p][k]

def roznica( S ):
	n = len(S)
	max = -1
	res = 0
	DP = [ [ None for _ in range(n) ] for _ in range(n) ]

	for p in range(n):
		for k in range(p+1, n):
			res = f(S, DP, p, k)
			if res > max:
				max = res
	
	return max

runtests ( roznica )
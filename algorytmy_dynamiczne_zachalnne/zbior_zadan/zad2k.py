from zad2ktesty import runtests

def f(S, DP, p, k):	
	if DP[p][k] is not None:
		return DP[p][k]

	if p == k:
		DP[p][k] = 1
		return DP[p][k]

	if p+1 == k:
		if S[p] == S[k]:
			DP[p][k] = 2
		else:		
			DP[p][k] = 0
		
		return DP[p][k]

	if S[p] != S[k]:
		DP[p][k] =  0
	else:
		res = f(S, DP, p+1, k-1)
	
		if res == 0:
			DP[p][k] =  0
		else:
			DP[p][k] = res+2
	
	return DP[p][k]

def palindrom( S ):
	n = len(S)
	res = 0
	max = 0
	max_a = 0
	max_b = 0
	DP = [ [ None for _ in range(n) ] for _ in range(n) ]
	
	for a in range(n):
		for b in range(a+1, n):
			res = f(S, DP, a, b)
			if res > max:
				max = res
				max_a = a
				max_b = b
	
	return S[max_a:max_b+1]

runtests ( palindrom )
from zad3ktesty import runtests

def f(A, DP, i, k):
	if DP[i] is not None:
		return DP[i]

	if i < k:
		DP[i] =  A[i]
		return DP[i]
	
	minn = float('inf')

	for j in range(i-k, i):
		minn = min(minn, f(A, DP, j, k))
	
	DP[i] = minn + A[i]	
	
	return DP[i]

def ksuma( T, k ):
	n = len(T)
	res = 0
	minn = float('inf')
	DP = [ None for _ in range(n) ]

	for i in range(n-k,n):
		res = f(T, DP, i, k)
		if res < minn:
			minn = res
		
	return minn
    
runtests ( ksuma )
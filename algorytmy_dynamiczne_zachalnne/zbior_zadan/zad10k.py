from zad10ktesty import runtests

def f(N, D):
	if D[N] != 0:
		return D[N]

	if N == 0:
		return 0

	minn = float('inf')
	x = 1
	
	while x*x <= N:
		minn = min(minn, f(N-x*x, D))
		D[N] = minn+1
		x += 1
	
	return D[N]

def get_sol(N, D):
	x = 1
	val = D[N]-1
	sol = []
	ind = N
	
	while x*x <= ind:
		if D[ind -x*x] == val:
			sol.append(x)
			ind -= x*x
			x = 1
			val -= 1
		else:
			x+= 1
	
	return sorted(sol)

def dywany ( N ):
	
	D = [ 0 for _ in range(N+1) ]
	
	f(N, D)

	print(D)

	return get_sol(N, D)


runtests( dywany )


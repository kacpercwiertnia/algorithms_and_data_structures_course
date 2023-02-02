from zad6ktesty import runtests 

def f(S, D, i):
	if D[i] != -1:
		return D[i]
	
	if S[i-1] == '0' and S[i] == '0':
		D[i] = 0
		return D[i]

	if S[i-1] > '2':
		if S[i] == '0':
			return 0
		else:
			D[i] = f(S, D, i-1)
	elif S[i-1] == '2':
		if S[i] == '0':
			D[i] = f(S, D, i-2)
		elif S[i] > '6':
			D[i] = f(S, D, i-1)
		else:
			D[i] = f(S, D, i-1) + f(S, D, i-2)
	else:
		if S[i-1] == '0':
			D[i] = f(S, D, i-1)
		elif S[i] == '0':
			D[i] = f(S, D, i-2)
		else:
			D[i] = f(S, D, i-2) + f(S, D, i-1)
	return D[i]

def haslo ( S ):
	n = len(S)

	if S[0] == '0':
		return 0
	
	D = [ -1 for _ in range(n) ]
	
	D[0] = 1
	
	if S[0] > '2':
		if S[1] == '0':
			return 0
		else:
			D[1] = 1
	elif S[0] == '2':
		if S[1] > '6' or S[1] == '0':
			D[1] = 1
		else:
			D[1] = 2
	else:
		if S[1] == '0':
			D[1] = 1
		else:
			D[1] = 2

	return f(S, D, n-1)

runtests ( haslo )
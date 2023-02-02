from zad8ktesty import runtests

def f(s, t, D, a, b):
	if a < 0:
		return 0
	if b < 0:
		return 0
	
	if D[b][a] != -1:
		return D[b][a]
	
	if s[a] == t[b]:
		D[b][a] = f(s, t, D, a-1, b-1)
	else:
		D[b][a] = min(f(s, t, D, a-1, b-1), f(s, t, D, a-1, b), f(s, t, D, a, b-1))+1
	
	return D[b][a]

def napraw ( s, t ):
	n = len(s)
	m = len(t)
	
	D = [[ -1 for _ in range(n)] for _ in range(m) ]
	
	if s[0] == t[0]:
		D[0][0] = 0
	else:
		D[0][0] = 1
	
	for i in range(1, n):
		if s[i] == t[0]:
			D[0][i] = i
		else:
			D[0][i] = D[0][i-1] + 1
	
	for i in range(1, m):
		if s[0] == t[i]:
			D[i][0] = i
		else:
			D[i][0] = D[i-1][0] + 1

	return f(s, t, D, n-1, m-1)

runtests ( napraw )
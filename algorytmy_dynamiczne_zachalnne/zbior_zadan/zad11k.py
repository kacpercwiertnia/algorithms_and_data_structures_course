from zad11ktesty import runtests

def f(T, D, i, l, p):
	if i == len(T):
		return abs(l-p)

	if D[i][l] != -1:
		return D[i][l]
	
	D[i][l] = min(f(T, D, i+1, l+T[i], p), f(T, D, i+1, l, p+T[i]))
	return D[i][l]

def kontenerowiec(T):
	n = len(T)
	suma = 0
	
	for x in T:
		suma += x

	D = [[ -1 for _ in range(suma) ] for _ in range(n) ] 

	res = f(T, D, 0, 0, 0)

	return res

runtests ( kontenerowiec )
    
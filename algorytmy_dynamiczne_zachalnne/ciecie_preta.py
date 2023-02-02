T = [0, 1, 5, 8, 9, 10, 17, 17, 20]
n = 8

def f(T, i, F, D):
	if F[i] != -1:
		return F[i]
	
	if i == 0:
		F[i] = 0
		return 0
	
	maxx = 0
	
	for j in range(1, i+1):
		result = f(T, i-j, F, D) + T[j]
		if result > maxx:
			maxx = result
			D[i] = i-j
	
	F[i] = maxx
	return maxx

def wypisz(D, n):
	if n <= 0:
		return []

	return [n-D[n]] + wypisz(D, D[n])

def zadanie(T, n):
	F = [ -1 for _ in range(n+1) ]
	D = [ -1 for _ in range(n+1) ]
	f(T, n, F, D)

	return wypisz(D, n)

print(zadanie(T, n))


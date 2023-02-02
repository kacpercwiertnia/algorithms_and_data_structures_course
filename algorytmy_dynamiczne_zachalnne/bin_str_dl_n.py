def zadanie(n):
	
	F = [ -1 for _ in range(n+1)]
	F[1]=2
	F[2]=3

	return f(F, n)

def f(F, i):
	if F[i] != -1:
		return F[i]
	else:
		F[i] = f(F, i-1) + f(F, i-2)

	return F[i]

print(zadanie(5))
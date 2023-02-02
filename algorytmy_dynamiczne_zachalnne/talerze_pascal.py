def f(T, i , k, il):
	if i > (k+1)*il:
		return 0
	
	if i == 0:
		return 0
	
	if k == 0:
		suma = 0
		for x in range(i):
			suma += T[k][x]
		return suma

	maxi = 0
	for j in range(i+1):
		suma = 0
		for x in range(j):
			suma += T[k][x]
		print(suma)
		maxi = max(maxi, f(T, i-j, k-1, il) + suma)
		return maxi
	

def zadanie(T, P, k):

	print(f(T,P,len(T)-1,k))

T = [ [1, 10, 5], [2, 6, 9], [3, 6, 8] ]
P = 4
k = 3

zadanie(T, P, k)
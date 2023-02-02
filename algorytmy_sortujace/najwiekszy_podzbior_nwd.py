def czynniki_pierwsze(C, a):
	i = 2
	while i*i <= a:
		if a%i == 0:
			C[i]+=1
			while a%i == 0:
				a = a//i

		i+=1
	
	if a != 1:
		C[a]+=1

def counting_sort(T):
	n = len(T)
	
	C = [ 0 for _ in range(n) ]

	for i in range(n):
		czynniki_pierwsze(C, T[i])
		print(T[i],C)

	max = 0

	for i in range(n):
		if C[i] > C[max]:
			max = i

	return max

A = [3,4,6,3,3,2]

print(counting_sort(A))
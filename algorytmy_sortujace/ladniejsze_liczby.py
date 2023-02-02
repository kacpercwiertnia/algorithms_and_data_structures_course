def counting_sort(T, f):
	n = len(T)

	S = [ 0 for _ in range(11)]
	B = [ 0 for _ in range(n)]

	for i in range(n):
		S[T[i][f]]+=1		

	for i in range(1,11):
		S[i] += S[i-1]

	for i in range(n-1,-1,-1):
		S[T[i][f]] -=1
		B[S[T[i][f]]] = T[i]
	
	return B

def parameters(T):
	n = len(T)
	A = [ 0 for _ in range(n)]
	
	for i in range(n):
		C = [0,0,0,0,0,0,0,0,0,0]
		
		a = T[i]
		
		while a > 0:
			C[a%10]+=1
			a//=10
		
		w = 0
		s = 0
		
		for j in range(10):
			if C[j] == 1:
				s+=1
			elif C[j] > 1:
				w+=1
		A[i] = (T[i], 10-s, w)

	return A
	

def radix(T):
	T = parameters(T)
	T = counting_sort(T,2)
	T = counting_sort(T,1)

	for i in range(len(T)):
		T[i] = T[i][0]
	
	return T

T = [1266, 123, 455, 67333, 114577, 2344]

print(radix(T))
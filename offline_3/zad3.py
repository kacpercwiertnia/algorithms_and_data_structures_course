#Kacper Ćwiertnia
#
#Poniższy algorytm wykorzystuję tablicę P do wygenerowania dystrybuanty dla każdej z liczb od 1 do N.
#Wygenerowana dystrybuanta pozwala dobrać odpowiedni bucket dla każdej liczby.
#Ilość bucketów (po optymalizacji) wynosi n//8 + 1, 
#W przypadku gdy do jednego bucketa trafią dwie liczby, układanę są one liniowym algorytmem insertion
#Po rozłożeniu liczb na buckety, łączone są one w jedną tablice.
#
#Szacowna złożoność algorytmu wynosi O(n)

from zad3testy import runtests

def dystrybuanta(T, P):
	n = len(T)
	C = [ 0 for _ in range(n+2) ]
	
	for i in range(len(P)):
		s, k, p = P[i]
		r = k - s + 1
		C[s] += p/r
		C[k+1] -= p/r

	for i in range(1,n+2):
		C[i] += C[i-1]

	for i in range(1,n+2):
		C[i] += C[i-1]
	
	return C

def insertion(T, el):
	n = len(T)
	
	if n > 0:
		T.append(T[n-1])
		
		for i in range(n, 0, -1):
			if T[i] < el:
				T[i] = el
				return T
			else:
				T[i-1] = T[i-2]
		
		T[0] = el
	else:
		T.append(el)
	
	return

def SortTab(T,P):
	n = len(T)
	k = n//8 + 1
	B = [ [] for _ in range(k+1) ]
	C = [ 0 for _ in range(n) ]
	D = dystrybuanta(T,P)
	
	for i in range(n):
		dziesietna = (T[i]-int(T[i]))
		dostepne_kubelki = int(k*(D[int(T[i])] - D[int(T[i])-1]))
		przesuniecie = int(D[int(T[i])-1]*k)
		a = przesuniecie + int(dziesietna* dostepne_kubelki)
		insertion(B[a],T[i])
	
	x = 0
	
	for i in range(k+1):
		for j in range(len(B[i])):
			C[x] = B[i][j]
			x+=1

	return C

runtests( SortTab )
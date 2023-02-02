#Kacper Ćwiertnia
#
#Poniższy algorytm wpierw wykorzystuje implementacje quick sorta aby ułożyć przedziały rosnąco
#względem początków przedziałów oraz malejąco względem ich końców. Tym sposobem przedziały o tym
#samym początku bedą coraz mniejsze i bedą zawierały się w pierwszym z nich.
#Następnie algorytm rozpoczyna sprawdzanie zawierania dla pierwszego przedziału. Gdy podczas
#poszukiwań natknie się na przedział o większym końcu odznaczy go jako potencjalnie większy.
#Dla każdego rozpatrywanego przedziału odznaczany jest jeden nowy kandydat.
#Sprawdzanie zawierania przerywane jest gdy przedziały są już rozłączne.
#Rozpatrywanie nowych kandydatów jest przerywane gdy nie ma nowego kandydata lub następny
#kandydat ma przed sobą mniej lub tyle samo przedziałów co maksymalne zawieranie.
#
#Algorytm działa ponieważ dzięki sortowaniu nie pomija żadnych przedziałów i przy sprawdzaniu
#zawierania odpowiednio dobiera potencjalnych kandydatów. 
#
#Szacowna złożoność to O(nlogn + nlogn)

from zad2testy import runtests

def quick_sort(A, p, r):
	while p < r:
		q = partition(A, p, r)
		quick_sort(A, p, q-1)
		p = q + 1

def partition(A, p, r):
	a = A[r][0]
	b = A[r][1]
	i = p - 1
	
	for j in range(p, r):
		if A[j][0] < a or ( A[j][0] == a and A[j][1] >= b ):
			i += 1
			A[i],A[j] = A[j],A[i]
		
	A[i+1],A[r] = A[r],A[i+1]

	return i+1

def depth(L):
	n = len(L)
	quick_sort(L, 0, n-1)
	max_zawieranie = 0
	start = 0
	flaga = True
	
	while flaga:
		zawieranie = 0
		flaga = False
	
		for y in range(start+1, n):
			if L[start][1] < L[y][1]:
				if not flaga:
					new_start = y
					flaga = True
				
				if L[start][1] < L[y][0]:
					break
			else:
				zawieranie += 1
		
		if flaga:
			start = new_start
		
		if zawieranie > max_zawieranie:
			max_zawieranie = zawieranie
	
		if max_zawieranie >= n-start-1:
			break
	
	return max_zawieranie


runtests( depth )
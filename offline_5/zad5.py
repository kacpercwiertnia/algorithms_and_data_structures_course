#Kacper Ćwiertnia
#
#Poniższy algorytm w pierwszej kolejności uzupełnia kolejkę priorytetową krotkami
#które zawierają wartości pól ropy( ze znakiem - tak aby te największe na plusie były 
#otrzymywane przy zdejmowaniu ich z kolejki ) oraz indeksy pól, które znajdują się w naszym zasięgu.
#Z kolejki zdejmujemy kolejne pola i dodajemy ich wartość do zmiennej stop, która sprawdza
#gdzie możemy dojechać, a indeksy pól dodajemy do tablicy zawierającej nasza drogę.
#Jeżeli stop jest większy od indeksu n-1 to program sortuje tablice indeksów i kończy działanie
#Jeżeli stop jest wciąż mniejszy od n-1 to dodajemy do kolejki kolejne krotki ponieważ nasz zakres
#się powiększył
#
#Szacowana złożoność to O(n*logn)

from zad5testy import runtests
import queue

def plan(T):
	n = len(T)
	droga = [0]
	stop = T[0]
	
	if stop < n-1:
		przystanki = queue.PriorityQueue()
		
		for i in range(1, stop+1):
			przystanki.put((-T[i],i))
	
		while stop < n-1:
		
			p, ind = przystanki.get()
			droga.append(ind)	
		
			if stop-p+1 >= n:
				break
			
			for i in range(stop+1, stop-p+1):
				przystanki.put((-T[i],i))
	
			stop -=p		
	
		droga.sort()

	return droga

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )

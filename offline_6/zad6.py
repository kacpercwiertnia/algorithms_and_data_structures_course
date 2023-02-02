#Kacper Ćwiertnia
#
#Poniższy algorytm w pierwszej kolejności wywołuję BFS dla wierzchołka s dzięki czemu w tablicy
#d1 znajdują się odległości od kolejnych wierzchołków, w szczególności od wierzchołka t.
#Gdy po pierwszy wywołaniu BFS, wartości d1[t] jest Nonem, to znaczy ze ścieżka z s do t nie istnieje 
#i algorytm zwraca None. Gdy jednak wartość ta istnieje to algorytm drugi raz wywołuję BFS, lecz tym
#razem dla wierzchołka t i zapisuje odległości od kolejnych wierzchołków w tablicy d2.
#Następnie algorytm wywołuję funkcje find, która rozpoczyna szukanie "wąskiego gardła", czyli 
#krawędzi, która jako jedyna jest początkiem najkrótszej ścieżki z t do s. Dzięki wartościom w
#d2 wiemy dla kolejno których krawędzi sąsiadujących z wierzchołkiem t musimy sprawdzić ich 
#wartość w tablicy d1 tak aby określić ich dystans do s. Gdy w przeszukiwanych wierzchołkach znajdzie
#się jeden taki, którego wartość w d1 jest najmniejsza i jedyna to oznacz ze znaleźliśmy krawędź,
#która zawiera najkrótszą ścieżkę i algorytm zwraca znaleziona krawędź.
#Gdy jednak w poszukiwaniu takiego wierzchołka dotrzemy do wierzchołka s to oznacz, że najkrótszych
#ścieżek było więcej niż jedna i zwracamy None.
#
#Szacowana złożoność obliczeniowa to O(V + E)

from zad6testy import runtests
from collections import deque

def BFS(G, s, d):
	V = len(G)
	Q = deque()
	visited = [0 for _ in range(V)]
	d[s] = 0
	visited[s] = 1
	Q.append(s)
	
	while Q:
		s = Q.popleft()
		for i in G[s]:
			if visited[i] == 0:
				Q.append(i)
				visited[i] = 1
				d[i] = d[s] + 1
	
def find(G, s, t, d1, d2):
	V = len(G)
	Q = deque()
	Q.append(t)
	minn = (d1[t], t, t)
	flag = False
	prev = t

	while Q:
		t = Q.popleft()
		if d2[t] != d2[prev] and flag:
			return (minn[1],minn[2])	

		if t == s:
			return None

		for i in G[t]:
			if d2[i] > d2[t]:
				Q.append(i)
				if d1[i] < minn[0]:
					minn = (d1[i], i, t)
					flag = True
				elif d1[i] == minn[0] and ( minn[2] != t or minn[1] != i ):
					flag = False
		prev = t
	
	return None

def longer( G, s, t ):

	d1 = [ None for _ in range(len(G))]
	d2 = [ None for _ in range(len(G))]
	BFS(G, s, d1)
	
	if d1[t] is None:
		return None

	BFS(G, t, d2)

	return find(G, s, t, d1, d2)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )
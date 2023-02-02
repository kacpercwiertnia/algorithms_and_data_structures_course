#Kacper Ćwiertnia
#
#Poniższy algorytm tworzy graf pełny ważony z podanych danych, następnie znajduje przy
#pomocy algorytmu kruscala MST i zapisuje różnicę skrajnych wag. Potem algorytm szuka MST
#pomijając wszystkie krawędzie, których wagi są mniejsze od różnicy najmniejszego wyniku i poprzedniego.
#W taki sposób algorytm znajdzie najmniejszą różnicę między wagami.
#
#Szacowana złożoność O(n^4*logn)

from zad8testy import runtests

from math import ceil 
from math import sqrt
from math import inf

from collections import deque

from queue import PriorityQueue

def find(parent, x):
	while x != parent[x]:
		x = parent[x]

	return x

def union(parent, x, y):
	tmp = parent[y]
	tmp2 = parent[x]
	
	for i in range(len(parent)):
		if parent[i] == tmp:
			parent[i] = tmp2

def highway( A ):
	V = len(A)
	all_ed = PriorityQueue()
	
	for i in range(V):
		for j in range(i+1, V):
			all_ed.put((ceil(sqrt((A[i][0]-A[j][0])**2+(A[i][1]-A[j][1])**2)), (i, j)))

	res = inf
	klusek = PriorityQueue()
	tmp = deque()
	parent = [ i for i in range(V) ]
	count = 0
	minn = inf
	maxx = 0

	while count < V-1:
		if all_ed.empty():
			return 0
	
		ed = all_ed.get()
		x = ed[1][0]
		y = ed[1][1]
		val = ed[0]		

		if find(parent, x) != find(parent, y):
			count +=1
			if val > maxx:
				maxx = val
			if val < minn:
				minn = val

			union(parent, x, y)
			klusek.put(ed)
		else:
			tmp.append(ed) 
		
	if maxx-minn < res:
		res = maxx-minn	
	
	lastmaxx = maxx

	while True:
		while tmp:
			all_ed.put(tmp.pop())
		
		del1 = klusek.get()
		
		while not klusek.empty():
			del2 = klusek.get()
			if lastmaxx-del2[0] < res:
				klusek.put(del2)
				break		

		parent = [ i for i in range(V) ]
		count = 0
		minn = inf
		maxx = 0
		tmp2 = deque()

		while not klusek.empty():
			ed = klusek.get()
			x = ed[1][0]
			y = ed[1][1]
			val = ed[0]	
			
			if find(parent, x) == find(parent, y):
				return res
			
			count +=1
			
			if val > maxx:
				maxx = val
			if val < minn:
				minn = val

			union(parent, x, y)
			tmp2.append(ed)
		
		while tmp2:
			klusek.put(tmp2.pop())

		while count < V-1:
			if all_ed.empty():
				if res == inf:
					return 0	
			
				return res
	
			ed = all_ed.get()
			x = ed[1][0]
			y = ed[1][1]
			val = ed[0]
			
			if find(parent, x) != find(parent, y):
				count +=1
				
				if val > maxx:
					maxx = val
				if val < minn:
					minn = val

				union(parent, x, y)
				klusek.put(ed)
			else:
				tmp.append(ed) 

		if maxx-minn < res:
			res = maxx-minn	
		
		lastmaxx = maxx
	
	return res
	
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True)
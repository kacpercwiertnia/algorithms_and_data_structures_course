#Kacper Ćwiertnia
#
#Poniższy algorytm to dostosowany do warunków zadania DFS.
#Algorytm rozpoczyna poszukiwanie cyklu z miasta 0 i bramy północnej, wybór 
#miasta rozpoczynającego i bramy nie wpływa na rozwiązanie zadania.
#Z miasta 0 algorytm uruchamia funkcje DFSVisit dla pierwszego miasta z
#bramy północnej, po wejściu do danego miasta sprawdza, którą bramą wszedł 
#i wychodzi do następnego nieodwiedzonego miasta drugą brama.
#Algorytm rekurencyjnie wchodzi do kolejnych nieodwiedzonych miast do
#do momentu gdzie nie będzie mógł już nigdzie wyjść.
#W tej sytuacji algorytm sprawdza czy ilość odwiedzonych miast jest równa
#ogólnej ilości miast, jeżeli tak to kończy działanie i zwraca tablice miast
#w przeciwnych przypadku backtracking cofa zaznaczenie miasta na nieodwiedzone
#i sprawdza następne miasta.
#Gdy rekurencja wycofa się do po sprawdzeniu wszystkich miast z bramy północnej
#miasta 0 to szukany cykl nie istnieje.
#
#Złożoność poniższego algorytmu wynosi O(n^2)

from zad7testy import runtests

def DFS(G):
	V = len(G)
	visited = [ False for _ in range(V)]
	sol = [ None for _ in range(V)]
	count = 1
	visited[0] = True

	def DFSVisit(G, u, k, visited, sol):
		nonlocal count
		
		p = 0

		if k in G[u][0]:
			p = 1
		
		for v in G[u][p]:
			if not visited[v]:
				sol[count] = v
				visited[v] = True
				count += 1

				if DFSVisit(G, v, u, visited, sol):
					return True
				else:
					visited[v] = False
					count -= 1
					sol[count] = None
		
		if count == len(G) and 0 in G[u][p] and u in G[0][1]:
			sol[0] = 0
			return True

		return False

	for v in G[0][0]:
		sol[count] = v
		visited[v] = True
		count += 1

		if DFSVisit(G, v, 0, visited, sol):
			return sol
		else:
			visited[v] = False
			sol[count] = None
			count -= 1
	
	return None

def droga( G ):

	return DFS(G)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )
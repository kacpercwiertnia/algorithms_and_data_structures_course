from zad7ktesty import runtests 
from collections import deque

def BFS(G, visited, s):
	Q = deque()
	Q.append((s,0))
	suma = G[0][s]
	visited[0][s] = True
	
	while Q:
		x, y = Q.popleft()
		
		if x-1 > -1 and not visited[y][x-1] and G[y][x-1] > 0:
			suma += G[y][x-1]
			visited[y][x-1] = True
			Q.append((x-1, y))
		
		if x+1 < len(G[0]) and not visited[y][x+1] and G[y][x+1] > 0:
			suma += G[y][x+1]
			visited[y][x+1] = True
			Q.append((x+1, y))
		
		if y-1 > -1 and not visited[y-1][x] and G[y-1][x] > 0:
			suma += G[y-1][x]
			visited[y-1][x] = True
			Q.append((x, y-1))
		
		if y+1 < len(G) and not visited[y+1][x] and G[y+1][x] > 0:
			suma += G[y+1][x]
			visited[y+1][x] = True
			Q.append((x, y+1))
	
	return suma
		
			
def ogrodnik (T, D, Z, l):
	a = len(T)
	b = len(T[0])
	n = len(Z)
		
	visited = [ [False for _ in range(b) ] for _ in range(a) ]
	W = [ 0 for _ in range(len(D)) ]
		
	for x in range(len(D)):
		W[x] = BFS(T, visited, D[x])
	
	D = [ [ 0 for _ in range(l+1) ] for _ in range(n) ]
	
	for i in range(W[0], l+1):
		D[0][i] = Z[0]
	
	for i in range(l+1):
		for j in range(1, n):
			D[j][i] = D[j-1][i]
			
			if i-W[j] >= 0:
				if D[j][i] < D[j-1][i-W[j]] + Z[j]:
					D[j][i] = D[j-1][i-W[j]] + Z[j]
	
	return D[n-1][l]

runtests( ogrodnik, all_tests=True )

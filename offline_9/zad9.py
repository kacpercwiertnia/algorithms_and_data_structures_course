from zad9testy import runtests
from queue import Queue

def make_graphs(G):
	size = 0

	for u,v,w in G:
		if u > size:
			size = u
		
		if v > size:
			size = v
		
	size += 2

	G3 = [ [ 0 for _ in range(size) ] for _ in range(size) ]
	G2 = [ [] for _ in range(size) ]
	
	for u,v,w in G:
		G3[u][v] = w
		G2[u].append(v)

	return size, G2, G3

def BFS(G, G2, parent, s, t):
	V = len(G)
	visited = [ False for _ in range(V) ]
	Q = Queue()
	
	Q.put(s)
	visited[s] = True

	while not Q.empty():
		u = Q.get()
	
		for v in G[u]:
			if v != -1 and not visited[v] and G2[u][v] != 0:
				visited[v] = True
				parent[v] = u
				Q.put(v)
	
	return visited[t]

def edmons_karp(G, G2, parent, s, t):
	max_flow = 0

	while BFS(G, G2, parent, s, t):
		min_flow = float('inf')
		a = t
					
		while a != s:
			min_flow = min( min_flow, G2[parent[a]][a] )
			a = parent[a]
			
		max_flow += min_flow
		b = t
				
		while b != s:
			a = parent[b]
			G2[a][b] -= min_flow
			G2[b][a] += min_flow
			b = a

	return max_flow

def fix_graph(G, G2):
	for u,v,w in G:
		G2[u][v] = w
		G2[v][u] = 0

def maxflow( G, s ):

	V, G2, G3 = make_graphs(G)
	parent = [ None for _ in range(V) ]
	res = 0
	
	for u in range(V-1):
		for v in range(u+1, V):
			if v != s and u != s:
				G3[u][V-1] = float('inf')
				G3[v][V-1] = float('inf')
				G2[u].append(V-1)
				G2[v].append(V-1)
				
				max_flow = edmons_karp(G2, G3, parent, s, V-1)
				
				if res < max_flow:
					res = max_flow
			
				fix_graph(G, G3)
				G3[u][V-1] = 0
				G3[v][V-1] = 0
				G2[u][len(G2[u])-1] = -1
				G2[v][len(G2[v])-1] = -1

	return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxflow, all_tests = True )
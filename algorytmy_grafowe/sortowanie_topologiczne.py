def DFS(G):
	V = len(G)
	visited = [False for _ in range(V)]
	tpg = [None for _ in range(V)]
	pos = V-1

	def DFSVisit(G, u):
		nonlocal pos
		visited[u] = True
		
		for v in G[u]:
			if not visited[v]:
				DFSVisit(G, v)
	
		tpg[pos] = u
		pos -= 1
	
	for u in range(V):
		if not visited[u]:
			DFSVisit(G, u)

	return tpg	

G = [[1,2],
     [2],
     [],
     [],
     [1,3,6],
     [4],
     []]

print(DFS(G))
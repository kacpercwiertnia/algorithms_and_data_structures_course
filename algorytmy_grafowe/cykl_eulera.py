def is_eulerCycle(G):
	for i in range(len(G)):
		if len(G[i])%2 != 0:
			return False
	return True

def remove(G, u, v):
	for i in range(len(G[v])):
		if G[v][i] == u:
			G[v][i] = None
			break
				
	for i in range(len(G[u])):
		if G[u][i] == v:
			G[u][i] = None
			break	

def DFS(G, M, u):
	for v in G[u]:
		if v is not None:
			remove(G, u, v)
			DFS(G, M, v)
		
	M.append(u)
	
def eulerCycle(G):
	M = []
	DFS(G, M, 0)
	return M

G = [[1, 2],
     [0, 2, 3, 5],
     [0, 1, 3, 5],
     [1, 2, 4, 5],
     [3, 5],
     [1, 2, 3, 4]]

if is_eulerCycle(G):
	print(eulerCycle(G))
else:
	print(None)
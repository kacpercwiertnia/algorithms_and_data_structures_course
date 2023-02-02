def floyd_marshall(G):
	V = len(G)
	D = [[float('inf') for i in range(V) ]	for i in range(V) ]
	parent = [[None for i in range(V) ] for i in range(V) ]
	
	for u in range(V):
		for v in range(V):
			if u == v:
				D[u][v] = 0
			elif G[u][v] != 0:
				D[u][v] = G[u][v]
				parent[u][v] = u

	for i in range(V):
		for u in range(V):
			for v in range(V):
				if D[u][v] > D[u][i] + D[i][v]:
					D[u][v] = D[u][i] + D[i][v]
					parent[u][v] = parent[i][v]
	for line in parent:
		print(line)
	
	
	return D



G = [[0,1,0,2,0,0,0,0,0],
     [0,0,-1,0,2,0,0,0,0],
     [0,0,0,0,0,-1,0,0,0],
     [0,0,-1,0,0,0,5,0,0],
     [0,0,0,0,0,0,0,5,0],
     [0,0,0,0,0,0,-2,0,4],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,7],
     [0,0,0,0,0,0,2,0,0]]

D = floyd_marshall(G)

for line in D:
	print(line)
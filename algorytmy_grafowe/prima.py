from queue import PriorityQueue

def Prima(G):
	V = len(G)
	DQ = PriorityQueue()
	W = [ float('inf') for _ in range(V) ]
	visited = [ False for _ in range(V) ]
	parent = [ None for _ in range(V) ]

	W[0] = 0
	DQ.put((W[0],0))

	while not DQ.empty():
		
		_, u = DQ.get()

		if visited[u]:
			continue
		
		visited[u] = True
		
		for v, w in G[u]:
			if W[v] > w and parent[u] != v:
				parent[v] = u
				W[v] = w
				DQ.put((W[v],v))

	MST = []

	for u in range(1, V):
		MST.append((parent[u],u))

	return MST

G = [[(1,1),(2,2)],
     [(0,1),(3,1),(4,3)],
     [(0,2),(3,3)],
     [(1,1),(2,3),(4,1),(5,2)],
     [(1,3),(3,1),(5,4)],
     [(3,2),(4,4),(6,1),(7,4)],
     [(5,1),(7,2),(8,100)],
     [(5,4),(6,2)],
     [(6,100)]]


print(Prima(G))
from queue import PriorityQueue

def w(G, u, v):
	for a, b in G[u]:
		if a == v:
			return b
	
def relax(PQ, d, G, parent, u, v):
	if d[v] > d[u] + w(G, u, v):
		d[v] = d[u] + w(G, u, v)
		parent[v] = u
		PQ.put((d[v],v))

def dijkstra(G, s):
	V = len(G)
	d = [ float('inf') for _ in range(V) ]
	parent = [ None for _ in range(V) ]
	visited = [ False for _ in range(V) ]
	d[s] = 0
	PQ = PriorityQueue()
	PQ.put((d[s], s))

	while not PQ.empty():
		dl, u = PQ.get()
		
		for p in G[u]:
			if not visited[p[0]]:
				relax(PQ, d, G, parent, u, p[0])
		
		visited[u] = True

	return d, parent

G = [[(1,1),(2,2)],
     [(0,1),(3,1),(4,3)],
     [(0,2),(3,3)],
     [(1,1),(2,3),(4,1),(5,2)],
     [(1,3),(3,1),(5,4)],
     [(3,2),(4,4),(6,1),(7,4)],
     [(5,1),(7,2),(8,100)],
     [(5,4),(6,2)],
     [(6,100)]]

print(dijkstra(G,0))
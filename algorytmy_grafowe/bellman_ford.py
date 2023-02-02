def make_graph(G):
	V = len(G)
	E = []

	for u in range(V):
		for v,w in G[u]:
			E.append((u,v,w))

	return E

def relax(d, parent, u, v, w):
	if d[v] > d[u] + w:
		d[v] = d[u] + w
		parent[v] = u

def verify(d, u, v, w):
	if d[v] <= d[u] + w:
		return True
	
	return False

def bellman_ford(G, s):
	V = len(G)

	E = make_graph(G)
	
	parent = [ None for _ in range(V) ]
	d = [ float('inf') for _ in range(V) ]

	d[s] = 0

	for i in range( V-1 ):
		for j in range(len(E)):
			u, v, w = E[j]
			relax(d, parent, u, v, w)
	
	for i in range(len(E)):
		u, v, w = E[i]
		if not verify(d, u, v, w):
			return "Cykl ujemny"
	
	return d			


G = [[(1,1),(3,2)],
     [(2,-1),(4,2)],
     [(5,-1)],
     [(2,-1),(6,3)],
     [(7,5)],
     [(6,-2),(8,4)],
     [],
     [(8,7)],
     [(6,2)]]

print(bellman_ford(G, 0))
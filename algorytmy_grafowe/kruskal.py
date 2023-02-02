class Node:
	def __init__(self, value):
		self.value = value
		self.parent = self
		self.rank = 0

def find(x):
	if x.parent != x:
		x.parent = find(x.parent)
	
	return x.parent

def union(x,y):
	x = find(x)
	y = find(y)
	
	if x == y:
		return False

	if x.rank > y.rank:
		y.parent = x
	
	else:
		x.parent = y
		if x.rank == y.rank:
			y.rank += 1
	return True

def makeset(x):
	return Node(x)


def kruskal(G):
	V = len(G)
	E = []
	A = [ None for _ in range(V) ]
	

	for u in range(V):
		for v,w in G[u]:
			if v > u:
				E.append((u,v,w))

	E = sorted(E, key=lambda x: x[2])
	
	for i in range(V):
		A[i] = makeset(i)
	
	count = 0
	MST = []
	
	for u,v,w in E:
		if union(A[u], A[v]):
			count += 1
			MST.append((u,v))
		if count == V-1:
			break
	
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

print(kruskal(G))

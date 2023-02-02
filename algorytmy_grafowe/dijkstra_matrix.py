def dijkstra_matrix(G, s):
	V = len(G)
	d = [ float('inf') for _ in range(V) ]
	parent = [ None for _ in range(V) ]
	tmp = [ (float('inf'), None) for _ in range(V) ]
	
	d[s] = 0
	u = s

	for _ in range(V-1):
		minn = float('inf')
		minn_index = 0

		for i in range(V):
			if d[i] == float('inf') and G[u][i] != 0 and tmp[i][0] > d[u]+G[u][i]:
				tmp[i] = (d[u]+G[u][i], u)	

		for i in range(V):
			if tmp[i][0] < minn:
				minn = tmp[i][0]
				minn_index = i		

		d[minn_index] = minn
		parent[minn_index] = tmp[minn_index][1]
		tmp[minn_index] = ( float('inf'), None )
		u = minn_index

	return d, parent
				
G = [[ 0, 7, 5,  2, 0, 0 ],
     [ 7, 0, 0,  0, 3, 8 ],
     [ 5, 0, 0, 10, 4, 0 ],
     [ 2, 0, 10, 0, 0, 2 ],
     [ 0, 3, 4,  0, 0, 6 ],
     [ 0, 8, 0,  2, 6, 0 ]]

print(dijkstra_matrix(G, 0))
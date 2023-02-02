def f(W,P,D,DP,i,p):
	if i < 0:
		return 0
	
	if D[i][p] != -1:
		return D[i][p]
	
	if p-W[i] >= 0:
		w1 = f(W,P,D,DP,i-1,p-W[i])+P[i]
		w2 = f(W,P,D,DP,i-1,p)
		
		if w1 > w2:
			D[i][p] = w1
			DP[i][p] = True
		else:
			D[i][p] = w2
	else:
		D[i][p] = f(W,P,D,DP,i-1,p)
	
	return D[i][p]

def knapsack(W, P, p):
	W.append(0)
	P.append(0)
	n = len(W)

	D = [ [ -1 for _ in range(p+1) ] for _ in range(n) ]
	DP = [ [ False for _ in range(p+1) ] for _ in range(n) ]
	
	f(W,P,D,DP,n-1,p)
	
	res = []
	j = p
	i = n-1
	
	while i >= 0 and j > 0:
		if DP[i][j] == True:
			res.append(P[i])
			j -= W[i]
		i -= 1
	
	return res
	
	
W = [95, 4, 60, 32, 23, 72, 80, 62, 65, 46]
P = [55, 10, 47, 5, 4, 50, 8, 61, 85, 87]
p = 269
	
print(knapsack(W, P, p))
from zad9ktesty import runtests
from math import inf
def f(P, D, g, d, i):
	if i >= len(P):
		return 0
	
	if D[i][d][g] != -1:
		return D[i][d][g]
	
	if g <= 0 and d <= 0:
		return 0
	
	if P[i] <= g and P[i] <= d:
		D[i][d][g] = max(f(P, D, g-P[i], d, i+1), f(P, D, g, d-P[i], i+1))+1
		return D[i][d][g]
	elif P[i] <= g:
		D[i][d][g] = f(P, D, g-P[i], d, i+1)+1
		return D[i][d][g]
	elif P[i] <= d:
		D[i][d][g] = f(P, D, g, d-P[i], i+1)+1
		return D[i][d][g]
	else:
		return 0

def prom(P, g, d):
	n = len(P)
	D = [[[ -1 for _ in range(g+1) ] for _ in range(d+1) ] for _ in range(n) ]
	
	sol1 = []
	sol2 = []
	i = 0
	l1 = g
	l2 = d
	w1 = 0
	w2 = 0
	
	while not((i == n) or (l1-P[i] < 0 and l2-P[i] < 0)):
		if P[i] <= l1 and P[i] <= l2:
			w1 = f(P, D, l1-P[i], l2, i+1)
			w2 = f(P, D, l1, l2-P[i], i+1)

			if w1 >= w2:
				l1 -= P[i]
				sol1.append(i)
				i += 1
			else:
				l2 -= P[i]
				sol2.append(i)
				i += 1
		
		elif P[i] <= l1:
			l1 -= P[i]
			sol1.append(i)
			i += 1
		
		elif P[i] <= l2:
			l2 -= P[i]
			sol2.append(i)
			i += 1

	i -= 1
	
	if i in sol1:
		return sol1
	else:
		return sol2

runtests ( prom )
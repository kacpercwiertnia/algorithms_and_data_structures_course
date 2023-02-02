def najdl(A):
	n = len(A)
	
	DP = [ 1 for _ in range(n) ]
	DD = [ -1 for _ in range(n) ]
	
	DP[0] = 1
	
	for i in range(n):
		for j in range(i):
			if DP[i] <= DP[j] and A[i] > A[j]:
				DP[i] = DP[j]+1
				DD[i] = j

	maxx = 0		
	maxx_ind = 0
	
	for i in range(n):
		if maxx < DP[i]:
			maxx = DP[i]
			maxx_ind = i

	res = []
	
	while DD[maxx_ind] != -1:
		res.append(A[maxx_ind])
		maxx_ind = DD[maxx_ind]
	
	res.append(A[maxx_ind])
	
	return res
	

A = [2, 1, 4, 3, 4, 8, 5, 7]

print(najdl(A))
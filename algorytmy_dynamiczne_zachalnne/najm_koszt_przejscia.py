A = [[1,13],
     [6,1]]

def zadanie(A):
	m = len(A)
	n = len(A[0])
	dl = n

	if m < n:
		dl = m

	B = [ [ 0 for j in range(n) ] for i in range(m) ]
	
	B[0][0] = A[0][0]	

	for i in range(1,n):
		B[0][i] = A[0][i] + B[0][i-1]

	for i in range(1,m):
		B[i][0] = A[i][0] + B[i-1][0]


	for j in range(1,dl):
		for i in range(j,n):
			B[j][i] = A[j][i] + min(B[j-1][i], B[j][i-1])

		for i in range(j,m):
			B[i][j] = A[i][j] + min(B[i][j-1], B[i-1][j])
	
	return B[m-1][n-1]


print(zadanie(A))
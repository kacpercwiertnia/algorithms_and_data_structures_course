A = [[5,4,3,6],
     [-1,1,2,5],
     [3,2,3,4]]

def f(A, F, x, y, i):
	
	if x < 0 or x >= len(A[0]) or y < 0 or y >= len(A):
		return 0
	
	if i >= A[y][x]:
		return 0

	if F[y][x] != -1:
		return F[y][x]
	
	F[y][x] =  max( f(A, F, x+1, y, A[y][x]), f(A, F, x-1, y, A[y][x]), 
			f(A, F, x, y+1, A[y][x]),f(A, F, x, y-1, A[y][x]) )+1

	return F[y][x]

def zadanie(A, x, y):
	m = len(A)
	n = len(A[0])

	F = [[-1 for _ in range(n)] for i in range(m)]
	
	return f(A, F, x, y, 0)

print(zadanie(A, 1, 1))

	

		
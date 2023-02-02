def binarySearch(S, l, r, val):
	while( r - l > 1 ):
		m = l + (r-l)//2
	
		if S[m] >= val:
			r = m
		else:
			l = m
	
	return r
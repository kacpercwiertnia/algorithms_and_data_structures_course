#Kacper Ćwiertnia
#
#Poniższy skrypt jest implementacją heap sorta z ograniczeniem zakresu do k+1 elementowej tablicy #nodów oraz dla k == 1 jest prostą implementacją bubble_sorta
#
#W przypadku gdy k = n, tablica jest odrazu sortowana przez funkcje heap_sort
#Gdy jednak k < n, z tablicy budowany jest kopiec, a następnie jest on naprawiany.
#Element najmniejszy zawsze będzie w A[0] więc gdy już kopiec zostanie naprawiony, element #najmniejszy jest przypisywany do wskaźnika, a za jego miejsce w tablicy wchodzi następny
#element z prawej. Kopiec jest naprawiany do momentu aż nie będzie zawierał k+1 ostatnich
#elementów. W ostatecznej fazie kopiec znów jest naprawiany, ale już tylko w coraz mniejszym zakresie
#tak aby najmniejszy element nie wracał na miejsce A[0].
#
#Dla k = 1 złożoność wynosi n, k = logn złożoność wynosi nlog(logn+1), k = n złożoność wynosi #nlog(n+1)

from zad1testy import Node, runtests

def left(i):
	return 2*i+1

def right(i):
	return 2*i+2

def parent(i):
	return (i-1)//2

def heapify(A, n, i):
	l = left(i)
	r = right(i)
	max_ind = i
	
	if l < n and A[l].val < A[max_ind].val:
		max_ind = l

	if r < n and A[r].val < A[max_ind].val:
		max_ind = r

	if max_ind != i:
		A[i], A[max_ind] = A[max_ind],A[i]
		heapify(A, n, max_ind)

def build_heap(A):
	n = len(A)
	
	for i in range(parent(n-1), -1, -1):
		heapify(A, n, i)

def heap_sort(A):
	n = len(A)
	build_heap(A)
	for i in range(n-1,0,-1):
		A[0],A[i] = A[i],A[0]
		heapify(A, i, 0)


def SortH(p,k):

	if k == 0:
		return p

	elif k == 1:
		r = p.next
		q = p
		q_prev = None
		
		if r is not None:
			if r.val < q.val:
				p = r
				q.next = r.next
				r.next = q
				r,q = q,r
			
			q_prev = q
			r = r.next
			q = q.next
			
			while r is not None:
				if r.val < q.val:
					q_prev.next = r
					q.next = r.next
					r.next = q
					r,q = q,r
				
				q_prev = q
				r = r.next
				q = q.next
			
		return p		
		
		

	else:

		A = []
		flaga = False			
	

		for i in range(k+1):
			if p is not None:
				A.append(p)
				p = p.next
			else:
				k = i
				flaga = True
				break

		if flaga:
			
			heap_sort(A)

			first = A[k-1]
			
			for i in range(k-1, 0, -1):
				A[i].next = A[i-1]
			
			A[0].next = None
		else:

			build_heap(A)
			
			first = A[0]

			while p is not None:
				sorted = A[0]
				A[0] = p
				heapify(A, k+1, 0)
				sorted.next = A[0]
				p = p.next
		
			for i in range(k+1):
				sorted.next = A[0]
				A[0],A[k-i] = A[k-i],A[0]
				heapify(A,k-i,0)
				sorted = sorted.next
		
			A[0].next = None
				
		return first

runtests( SortH ) 
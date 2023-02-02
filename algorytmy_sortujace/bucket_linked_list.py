class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

def make_linked_list(tab):
	first = None
	n = len(tab)
	
	for i in range(n - 1, -1, -1):
		tmp = Node(tab[i])
		tmp.next = first
		first = tmp
	
	return first

def print_linked_list(first):
	p = first

	while p is not None:
		print(' -->', p.val, end = '')
		p = p.next

	print()

def bucket_sort(first, a, b):
	p = first
	n = 0

	while p is not None:
		n += 1
		p = p.next

	B = [ Node(None) for i in range(n) ]
	b = (b-a+1)/n
	p = first

	while p is not None:
		index = int(p.val // b)-1
		r = B[index]

		while B[index].next is not None and B[index].next.val < p.val:
			B[index] = B[index].next

		if B[index].next is None:
			B[index].next = p
			B[index] = B[index].next
			p = p.next
			B[index].next = None

		else:
			a = p
			p = p.next
			a.next = B[index].next
			B[index].next = a
      
		B[index] = r

	sorted = None
	start = 0

	for i in range(n-1):
		B[i] = B[i].next
		if B[i] is not None:
			sorted = B[i]
			start = i
			break

	for i in range(start, n-1):
		while B[i].next is not None:	
			B[i] = B[i].next
		r = i
		i+1
		while i < n-1 and B[i].next is None:
			i+=1
		B[r].next = B[i].next

	return sorted

A = [5,1,4.5,5.5,7.5,4,3,8.5,9.5,9,7,10,2,6,8,1.5,3.5,6.5,2.5]

first = make_linked_list(A)
print_linked_list(first)
first = bucket_sort(first,1,19)
print_linked_list(first)
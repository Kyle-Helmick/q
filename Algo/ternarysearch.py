def ternarySearch(a,k):
	#a is a sorted list of integers
	#k is the integer searching for
	n = len(a)
	print "The array searching in is:", a
	print "The number of items are:", n
	print "The item searching for is:", k
	print " "

	#empty list
	if n == 0:
		return False
	
	#lists of size 1
	if n == 1:
		if k in a:
			return True
		else:
			return False
	
	#lists of size 2	
	if n == 2:
		if k in a:
			return True
		else:
			return False
	
	#lists of size 3 and greater
	if n >= 3:
	
		if k < a[n/3]:
			ternarySearch(a[0:n/3],k)
			if k in a:
				print "the number", k, "was found"
				return True
			else:
				return False
				
		if k >= a[n/3] and k < a[(2*n)/3]:
			ternarySearch(a[n/3:(2*n)/3],k)
			if k in a:
				print "the number", k, "was found"
				return True
			else:
				return False
				
		if k >= a[(2*n)/3] and k < a[n-1]:
			ternarySearch(a[((2*n)/3):n],k)
			if k in a:
				print "the number", k, "was found"
				return True
			else:
				return False
				
b = [1]
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
c = [1,3,5,10,12,15,32,91,125,132]
ternarySearch(a,22)


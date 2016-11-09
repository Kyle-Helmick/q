	#leftside = mergeSort(lst[:middle])
	#rightside = mergeSort(lst[middle:])
	
'''
	n = len(lst)
	
	if n <= 1:
		return lst
	if n > 1:
		middle = n/2
		leftside = lst[:middle]
		rightside = lst[middle:]
		
		leftside = mergeSort(leftside)
		rightside = mergeSort(rightside)
		
		return mergeItems(leftside,rightside,lst)
		
def mergeItems(leftside,rightside,lst):
	mergedlist = []
	
	i = 0
	j = 0
	
	a = len(leftside)
	b = len(rightside)





	while i < a and j < b:
		if lst[leftside] <= lst[rightside]:
			mergedlist.append(leftside[i])
			i += 1
		else:
			mergedlist.append(rightside[j])
			j += 1
			
	if i < a:
		for c in range(i,a):
			mergedlist.append(leftside[c])
		
	if j < b:
		for d in range(j,b):
			mergedlist.append(rightside[d])
'''

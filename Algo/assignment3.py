#a = [1,2,3,4,5,6,7,8,9,10]
#b = [5,6,7,8,9,10,11,12,13,14,15]

a = [3,7,4,1,6,11,14,2,9,15]
b = [11,15,4,17,13,2,1,5,8,9]
c = []

m = len(a)
n = len(b)

Hash = {}



**** a and b are not sorted ****

create empty hash table

for each element in a:
	set each key in hash table to value of each element in a
	
for each element in b:
	if each element in b is not in hash table:
		print elements not in hash table 


**** both are sorted ****

for each element in array1:
	for each element in array2:
		if element in array1 != element in array2:
			print element in array1
			

**** a is sorted but b is not ****

create empty hash table

for each element in b:
	set each key in hash table to value of each element in b
	
for each element in a:
	if each element in a is not in hash table:
		print elements not in hash table 







for j in range(0,n):
	Hash[j] = b[j]

	for i in range(0,m):
		if a[i] == Hash[j]:
			c.append(a[i])
			print(c)
				

			

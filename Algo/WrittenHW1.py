def ternarySearch(a,k):
	#a: list of sorted integers
	#k: is an integer 
	
	n = len(a)

	if n == 0:
		return False

	if n == 1:
		if k in a:
			return True
		else:
			return False

	if n == 2:
		for element in a:
			if element == k:
				return True
			else:
				return False

	if n >= 3:
		if k >= a[n/3] and k <= a[(2*n)/3]:
			for element in a[n/3:(2*n)/3]:
				if element == k:
					return True
				else:	
					if k < a[n/3]:
						for element in a[0:n/3]:
							if element == k:
								return True
							else:
								return False
	
					if k > a[(2*n)/3]:
						for element in a[n/3:n]:
							if element == k:
								return True
							else:
								return False
				

def main():
	array = [1]
	ternarySearch([1],5)
	
	











'''
---
length = len(seq)
left = 0
right = length
index = 0
x = True
while x and left <= right:
	#focal = (high + low) //3

	if left == right:
		#check similarity between values and key
		return index
        else:
            if right - left > 0:
                index1 = ((right+2*(left))//3)
                index2 = ((2*(right)+left)//3)
                if left == right:
                    x = False
                    return (index1+index2)
                if seq[index1] == key:
                    x = False
                    return index1
                if seq[index2]== key:
                    x = False
                    return index2
                if key<seq[index1]:
                        right = index1 - 1
                else:
                    if key > seq[index1] and key <seq[index2]:
                        right = index2 - 1
                        left = index1 - 1
                    if key > seq[index2]:
                        left = index2+1

    return index
'''

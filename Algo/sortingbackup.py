# Name: Bryan O'Hagan
# Email: bryan.ohagan@colorado.edu
# SUID: 102-897-464
#

import sys
import random
import time
import plotly.plotly as py
from plotly.graph_objs import *

# --------- Insertion Sort -------------
# Implementation of getPosition
# Helper function for insertionSort
def getPosition(rList, elt):
    # Find the position where element occurs in the list
    #
    for (i,e) in enumerate(rList):
        if (e >= elt):
            return i
    return len(rList)

# Implementation of Insertion Sort 
def insertionSort(lst):
    n = len(lst)
    retList = []
    for i in lst:
        pos = getPosition(retList,i)
        retList.insert(pos,i)    
    return retList

#------ Merge Sort --------------
def mergeSort(lst):
    # TODO: Implement mergesort here
    # You can add additional utility functions to help you out.
    # But the function to do mergesort should be called mergeSort

	n = len(lst)
	midelement = n/2
	result = []
	
	if n <= 1:
		return lst
		
	leftside = mergeSort(lst[:midelement])
	rightside = mergeSort(lst[midelement:])
	
	return mergedat(leftside, rightside)
	
def mergedat(leftside, rightside):
	sortedarray = []
	i = 0
	j = 0
	a = len(leftside)
	b = len(rightside)
	
	while i < a and j < b:
		if leftside[i] <= rightside[j]:
			sortedarray.append(leftside[i])
			i += 1
		else:
			sortedarray.append(rightside[j])
			j += 1
			
			
	while i < a:
		sortedarray.append(leftside[i])
		i += 1
	while j < b:
		sortedarray.append(rightside[j])
		j += 1
		
	return sortedarray


#    return lst # TODO: change this

#------ Quick Sort --------------
def quickSort(lst):
    # TODO: Implement quicksort here
    # You may add additional utility functions to help you out.
    # But the function to do quicksort should be called quickSort
	
    lowerelements = []
    higherelements = []    
    pivotelements = []
    
    n = len(lst)
    
    if n <= 1:
        return lst
    else:
		
        pivot = lst[n/2]
        
        for i in lst:
            if i < pivot:
                lowerelements.append(i)
            elif i > pivot:
                higherelements.append(i)
            else:
                pivotelements.append(i)
                
        lowerelements = quickSort(lowerelements)
        higherelements = quickSort(higherelements)
        
        returnelements = lowerelements + pivotelements + higherelements
        
        return returnelements


    return lst # TODO: change this
    


# ------ Timing Utility Functions ---------

# Function: generateRandomList
# Generate a list of n elements from 0 to n-1
# Shuffle these elements at random

def generateRandomList(n):
   # Generate a random shuffle of n elements
   lst = list(range(0,n))
   random.shuffle(lst)
   return lst


def measureRunningTimeComplexity(sortFunction,lst):
    t0 = time.clock()
    sortFunction(lst)
    t1 = time.clock() # A rather crude way to time the process.
    return (t1 - t0)


# --- TODO

# Write code to extract average/worst-case time complexity

if __name__ == '__main__':
	
	n = 20 #number of times runned
	m = 500 #number of elements 
	i = 0
	temp = 0
	arr = []
	arr1 = [1,2,3,4,5,6,7,8,9,10]

	for j in range(0,m):

		if j % 5 == 0:
#			print("the number of items is: " + str(j))

			for i in range(0,n):
#				print(n)	
				lst = generateRandomList(j)
#				lst = [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
				temp += measureRunningTimeComplexity(quickSort,lst) 
	
			a = temp/n
#			print ("*** The average running time for: " + str(j) + " elements is " + str(a) + " secs") #average 
			print (str(a))
#			print ( "(" + str(j) + "," + str(a) + ")")
	#		for i in range(0,10):
	#			arr1[i] = a
	#		print(arr1)
		
#	


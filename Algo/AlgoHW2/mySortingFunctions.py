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
		
        pivot = lst[n-1]
        
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
#   print(lst)
   return lst

def generateReverseSortedList(n):
   lst = list(range(0,n))
   lst2 = lst[::-1]
#   print lst2
   return lst2

def generateOrderedList(n):
	lst = list(range(0,n))
#	print lst
	return lst

def generateWorstMergeList(n):
	lst = list(range(0,n))
	b = [i for i in lst if i%2 == 0]
#	print b
	c = [i for i in lst if i%2 == 1]
#	print c
	d = b + c
#	print d
	return d
	

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
	temp = 0

	
	for j in range(0,m):

		if j % 5 == 0:
			lst = generateRandomList(j)
#			lst = generateOrderedList(j) 
				#for worst case quicksort. I set the largest element of array to
				#the pivot which produces worst case
#			lst = generateWorstMergeList(j) 
				#creates an array where all even elements are left of mid and all odd
				#are on the right side. This forces mergeSort to do the most comparisons 
#			lst = generateReverseSortedList(j)
				#For insertion sort the worst case is when the array is reversed sorted.
				#This function does produce reversed sorted arrays but for some reason
				#the running time is way faster than random. I tried running with
				# generateOrderedList and produced a result that I would expect from it
				# so I used that instead.
			
			for i in range(0,n):
								
#				temp += measureRunningTimeComplexity(insertionSort,lst)
#				temp += measureRunningTimeComplexity(mergeSort,lst)
				temp += measureRunningTimeComplexity(quickSort,lst)
								
			a = (temp)/n
#			print ("*** The average running time for: " + str(j) + " elements is " + str(a) + " secs") #average 
			print ( "(" + str(j) + "," + str(a) + ")")



#LastName: O'Hagan
#FirstName: Bryan
#Email: bryan.ohagan@colorado.edu
#Comments:

from __future__ import print_function
import sys

# We will use a class called my trie node
class MyTrieNode:
    # Initialize some fields 
  
    def __init__(self, isRootNode):
        #The initialization below is just a suggestion.
        #Change it as you will.
        # But do not change the signature of the constructor.
        self.isRoot = isRootNode
        self.isWordEnd = False # is this node a word ending node
        self.isRoot = False # is this a root node
        self.count = 0 # frequency count
        self.word = ""
        self.next = {} # Dictionary mappng each character from a-z to the child node


    def addWord(self,w):
		
        current_node = self
        
        for i in w:
			if i in (current_node.next):
				current_node = (current_node.next).get(i)
			else:
				(current_node.next)[i] = MyTrieNode(False)
				current_node = (current_node.next).get(i)
				
	current_node.count += 1
	current_node.word = w
	current_node.isWordEnd = True
			
        return



    def lookupWord(self,w):
        # Return frequency of occurrence of the word w in the trie
        # returns a number for the frequency and 0 if the word w does not occur.

		current_node = self
        
		for i in range(len(w)):
			if w[i] in (current_node.next):
				current_node = (current_node.next).get(w[i])
			else:
				return 0
		return current_node.count



    def lookupWordPrefix(self,w):
		
		current_node = self
			
		for i in range(len(w)):
			if w[i] in (current_node.next):
				current_node = (current_node.next).get(w[i])
			else:
				current_node.next = {}
		return current_node    



    def helper(self,prefix,lst):
		
		if (self.isWordEnd == True):
			lst.append((prefix, self.count))
			
		for i in (self.next):
			current_node = (self.next).get(i)
			current_node.helper(prefix + i, lst)
		

    def autoComplete(self,w):
        #Returns possible list of autocompletions of the word w
        #Returns a list of pairs (s,j) denoting that
        #         word s occurs with frequency j

        lst = []
        temp = self.lookupWordPrefix(w)
        temp.helper(w,lst)
        return lst
  
    
            

if (__name__ == '__main__'):
    t= MyTrieNode(True)
    lst1=['test','testament','testing','ping','pin','pink','pine','pint','testing','pinetree']

    for w in lst1:
        t.addWord(w)

    j = t.lookupWord('testy') # should return 0
    j2 = t.lookupWord('telltale') # should return 0
    j3 = t.lookupWord ('testing') # should return 2
    lst3 = t.autoComplete('pi')
    print(j,j2,j3)
    
    print('Completions for \"pi\" are : ')
    print(lst3)
    
    lst4 = t.autoComplete('tes')
    print('Completions for \"tes\" are : ')
    print(lst4)
 
    
    
     

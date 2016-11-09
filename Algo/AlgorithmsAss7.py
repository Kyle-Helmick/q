def NumHops(x, lives):
	turns = 0
    def min_hops(i, num_lives):

    	num_lives = lives
    	x = x + i
    	turns = turns + 1

    	#base case for if out of lives
        if num_lives == 0:
        	print("Out of lives: you lose")
            return 0
        #base case if hop pass 101
        elif x > 101:
        	print("Hopped pass 101: you lose")
        	return 0
        #base case if land on perfect square
        elif x = 1,4,9,16,25,36,49,64,81,100:
        	lives = lives - 1
        #base case if land on 42
 	    elif x = 42:
 	    	lives = lives + 1
 	    #base case if land on 101
 	    elif x = 101:
 	    	print("You made it to posisition 101: You Win!!!")
 	    	print("The amount of turns took: " + turns)
 	    	return 1
        else:
            return min(min_hops(i-1, num_lives), 1 + min_hops(i, num_lives-lives[i]))
    return min_hops(x, lives)




def min_change(listofcoins, target):
    def min_coins(i, target2):
        if aC == 0:
            return 0
        elif i == -1 or aC < 0:
            return float('inf')
        else:
            return min(min_coins(i-1, target2), 1 + min_coins(i, target2-listofcoins[i]))
    return min_coins(len(listofco)-1, C)
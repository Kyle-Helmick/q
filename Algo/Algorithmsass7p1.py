from __future__ import print_function
import sys

## Calculate cost[j] 
def rodCutRecursive(j,priceList):
    # j is the starting position
    # priceList is a list of prices by rod lengths
    
    n = len(priceList)
    # IF we are cutting at the last position
    if (j == n):
        return (0,[]) # Cost is 0 and no cuts

    maxCost = 0 # Keep a running accumulator for maximum cost
    cutList = [] # A list of cuts
    cutAt = j
    # Run through all the possible "next" cutting positions
    for k in range(j+1,n+1):
        #  Compute optimal solution assuming
        #         ( first cut from j to k ) ++ 
        #         ( optimal cut from k to end)
        (tmpCost,tmpCutList) = rodCutRecursive(k,priceList) # RECURSIVE call happens here.

        # Compute the cumulative price
        c = priceList[k-j-1] + tmpCost
        
        # This is the best we have seen so far.
        if ( c >= maxCost):
            maxCost = c          # Record the new maximum cost
            cutList = list(tmpCutList) # Store a list of cuts associated with getting this cost.
            cutAt = k
    
    cutList.append(cutAt-j) # Append the cut at j to the best list of cuts
    return maxCost,cutList # Return this back

def rodCutMemoize(j,priceList,memoTable):
    # This is almost same as the recursive
    # We add the memo table
    n = len(priceList)
    
    if (j == n):
        return (0,[])
    
    # Before we launch into the computation,
    # First lookup the memotable
    if (j in memoTable): # If it is already in the memotable, then 
        (c,cList) = memoTable[j] # just read the answer off the memotable
        return (c,cList) # return

    # Not in the memo table, we will now compute.
    maxCost = 0
    cutList = []
    cutAt = j
    for k in range(j+1,n+1):
        (tmpCost,tmpCutList) = rodCutMemoize(k,priceList,memoTable)

        c = priceList[k-j-1] + tmpCost
        if ( c >= maxCost):
            maxCost = c
            cutAt = k
            cutList = list(tmpCutList)

    cutList.append(cutAt - j)
    
    # Add the answer back to the memotable for the future.
    memoTable[j] = (maxCost,cutList)

    # return
    return maxCost,cutList




# v = list of item values or profit
# w = list of item weight or cost
# W = max weight or max cost for the knapsack
public int maxProfit(int[] prices) {
  if (prices.length == 0) return 0;
  int minPrice = prices[0];
  int max = 0;
  for (int i = 1; i < prices.length; i++) {
    if (prices[i] < minPrice) {
      minPrice = prices[i];
    }
    if (prices[i] - minPrice > max) {
      max = prices[i] - minPrice;
    }
  }
  return max;
}


def payoff(B,R,j):
    # B is budget
    # R is risk score
    # j is investments ID in the range of 1 to j

    #given values
    cost = [20,10,40,50,50,70,80]
    pay = [5,2,4,10,20,25,35]
    risk_score = [1,3,2,3,2,1,4]

    #base case if there are no investments
    if j == 0:
        print("There are no available investments")
        return 0

    #base case 2
    if B < 0 or R < 0:
        payoff(B,R,j) = ('-inf')

    #hash table of investment
    payout = {}
    should_invest = False

    for i in range(0,j-1):
        for j in range(0,len(cost)-1):
            for k in range(0,len(pay)-1):

                if (max(k) and min(B-cost[i])):
                    should_invest = True

                 payout[k,j,i] = (min(B-cost[i]),should_invest)

                 if should_invest == True:
                    return payout[k,j,i]




def payoffMemoize(B,R,j,memotable):
    # B is budget
    # R is risk score
    # j is investments ID in the range of 1 to j

    #given values
    cost = [20,10,40,50,50,70,80]
    pay = [5,2,4,10,20,25,35]
    risk_score = [1,3,2,3,2,1,4]

    #base case if there are no investments
    if j == 0:
        print("There are no available investments")
        return 0

    #base case 2
    if B < 0 or R < 0:
        payoff(B,R,j) = ('-inf')

    #hash table of investment
    payout = {}
    should_invest = False

    for j in memotable:
        (B,R,j) = memoTable[j]
        return (i,B) 

    for i in range(0,j-1):
        for j in range(0,len(cost)-1):
            for k in range(0,len(pay)-1):

                if (max(k) and min(B-cost[i])):
                    should_invest = True

                 payout[k,j,i] = (min(B-cost[i]),should_invest)
             
                 if should_invest == True:
                    return payout[k,j,i]
   
     memoTable[j] = (B,R,j)

    return payoffMemoize(B,R,i,memoTable)

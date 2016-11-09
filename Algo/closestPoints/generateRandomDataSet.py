from __future__ import print_function

import sys
import random

if (len(sys.argv) <= 1):
    fName = 'test'
    n = 500
else:
    fName = sys.argv[1]

if (len(sys.argv) <= 2):
    n = 500
else:
    n = int(sys.argv[2])
    
f = open(fName,'wt')
xMin = -40
xMax = 40
yMin = -40
yMax = 40

for i in range (0,n):
    x = random.uniform(xMin,xMax)
    y = random.uniform(yMin,yMax)
    print(x,',',y,file=f)
    
f.close()

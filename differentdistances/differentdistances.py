"""
INPUT: The input file contains up to 1000 test cases, each of which contains five real numbers, x1 y1 x2 y2 p, each of which have at most 10 digits past the decimal point. 
        All coordinates are in the range (0,100] and p is in the range [0.1,10]. The last test case is followed by a line containing a single zero.

OUTPUT: For each test case output the p-norm distance between the two points (x1,y1) and (x2,y2). Your answer may have absolute or relative error of at most 0.0001.
"""

# import module
import sys
import math

# read input
for a in range(1000):
    i = input().split()
    # last line break
    if float(i[0]) == 0:
        break
    else:
        x1 = float(i[0])
        y1 = float(i[1])
        x2 = float(i[2])
        y2 = float(i[3])
        p = float(i[4])

    x = float(abs(x1 - x2) ** p)
    y = float(abs(y1 - y2) ** p)
    q = float(p ** -1)
    dist = float((x + y) ** q)
    print(dist)
    

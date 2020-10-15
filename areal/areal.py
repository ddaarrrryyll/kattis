"""
INPUT: The input consists of a single integer a (1≤a≤1018), the area in square meters of Old MacDonald’s pasture.
OUTPUT: Output the total length of fence needed for the pasture, in meters. The length should be accurate to an absolute or relative error of at most 10−6.
"""
# import module
import sys
import math

# read stdin
i = int(sys.stdin.readline())

# length of fence j
j = round(math.sqrt(i) * 4, 7)

print(j)
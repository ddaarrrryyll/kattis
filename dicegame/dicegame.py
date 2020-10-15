"""
INPUT: The first line contains four integers a1,b1,a2,b2 that describe Gunnar’s dice. Die number i contains numbers ai,ai+1,…,bi on its sides. You may assume that 1≤ai≤bi≤100. 
        You can further assume that each die has at least four sides, so ai+3≤bi. The second line contains the description of Emma’s dice in the same format.
OUTPUT: Output the name of the player that has higher probability of winning. Output “Tie” if both players have same probability of winning.
"""

# import module
import sys
import math

# read stdin
# Gunnar's dice
g = input().split()
gunnar = [int(i) for i in g]
gunnar = sum(gunnar)

# Emma's dice
e = input().split()
emma = [int(i) for i in e]
emma = sum(emma)

if gunnar == emma:
    print("Tie")
elif gunnar > emma:
    print("Gunnar")
else:
    print("Emma")
# INPUT: The first line of input contains an integer N (1≤N≤50), the number of matches on the floor, and two integers W and H, the dimensions of the box (1≤W≤100, 1≤H≤100).
#        Each of the following N lines contains a single integer between 1 and 1000 (inclusive), the length of one match.
# OUTPUT: For each match, in the order they were given in the input, output on a separate line “DA” if the match fits in the box or “NE” if it does not.

# import module
import sys
import math

# read stdin
i = sys.stdin.readline().split()
n = int(i[0])
w = int(i[1])
h = int(i[2])

hyp = math.sqrt(w * w + h * h)
for x in range(n):
    if int(sys.stdin.readline()) <= hyp:
        print("DA")
    else:
        print("NE")
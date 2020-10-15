# INPUT: Input consists of a single integer N (1≤N≤100).
# OUTPUT: Output the entire wizard’s spell by counting from 1 to N, giving one number and “Abracadabra” per line.

# import module
import sys

# read stdin
i = int(sys.stdin.readline())

for j in range(i):
    k = j + 1
    print(k, " " + "Abracadabra")
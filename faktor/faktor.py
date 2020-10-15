"""
INPUT: First and only line of input will contain 2 integers, A (1≤A≤100), the number of articles you plan to publish and I (1≤I≤100), the impact factor the owners require.
OUTPUT: The first and only line of output should contain one integer, the minimal number of scientists you need to bribe.
"""
# import module
import sys

# read stdin
i = sys.stdin.readline().split()
x = int(i[0])
y = int(i[1])

faktor = (x * y) - x + 1
print(faktor)
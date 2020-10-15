"""
INPUT: The input contains an integer N (1≤N≤10000000), the number of stones.
OUTPUT: Output the winner, “Alice” or “Bob” (without the quotes), on a line.

"""
# import module
import sys

# read stdin
i = int(sys.stdin.readline())

if i % 2 == 0:
    print("Bob")

else:
    print("Alice")

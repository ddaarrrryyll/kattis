# INPUT: Input starts with two integers 1≤N,P≤1000 on a single line, denoting the number of contestants in the contest and the number of huffle-puff problems solved in total.
# Then follow N lines, each consisting of a single non-empty line in which the contestant describes him or herself. You may assume that the contestants are good at describing themselves, 
# in a way such that an arbitrary 5-year-old with hearing problems could understand it.
# OUTPUT: Output should consist of a single integer: the number of carrots that will be handed out during the contest.

# import module
import sys

# read stdin
i = sys.stdin.readline().split()
n = int(i[0])
p = int(i[1])

print(p)
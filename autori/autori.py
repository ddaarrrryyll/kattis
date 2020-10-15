# import module
import sys

# read stdin
name = str(sys.stdin.readline())
short = str('')

for i in range(len(name)):
    if name[i].isupper():
        short += name[i]

print(short)
    


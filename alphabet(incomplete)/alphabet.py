"""
INPUT:  Each input will consist of a single test case. Note that your program may be run multiple times on different inputs. 
        The only line of input contains a string s (1≤|s|≤50) which contains only lowercase letters.
OUTPUT: Output a single integer, which is the smallest number of letters needed to add to s to make it alphabetical
"""
s = ""
while not len(s) >= 1 and not len(s) <= 50 and not s.islower():
    s = input()

alphabets = [i for i in "abcdefghijklmnopqrstuvwxyz"]
start = s.index("a")
"""
INPUT: Three non-negative integers e,f,c, where e<1000 equals the number of empty soda bottles in Tim’s possession at the start of the day,
       f<1000 the number of empty soda bottles found during the day, and 2≤c<2000 the number of empty bottles required to buy a new soda.
OUTPUT: How many sodas did Tim drink on his extra thirsty day?
* he can exchange the new soda bottles that he drank
"""
info = input().split(" ")
e,f,c = (int(i) for i in info)
start = e + f
drank = start / c
leftover = start % c + drank

while leftover >= c:
    new = (leftover // c)
    if new == 0:
        break
    else:
        drank += new
        leftover %= c
        leftover += new
print(int(drank))
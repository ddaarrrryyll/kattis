"""
INPUT: The first line of the input contains an integer N and t (3≤N≤200000; 1≤t≤5). The second line of the input contains N non-negative 32-bit signed integers.
OUTPUT: For each test case, output the required answer based on the value of t.
"""
from collections import defaultdict

info = input().split(" ")
n, t = int(info[0]), int(info[1])
arr = input().split(" ")
for i in range(len(arr)):
    arr[i] = int(arr[i])

# If t=1, "Yes" if two integers add up to 7777
if t == 1:
    count = 0
    s = set(arr)
    for i in arr:
        to_find = 7777 - i
        if to_find in s:
            print("Yes")
            count += 1
            break
    if count == 0:
        print("No")

# If t=2, check dupes
elif t == 2:
    check = set(arr)
    if len(check) != len(arr):
        print("Contains duplicate")
    else:
        print("Unique")

# If t=3, find integer that appears more than half
elif t == 3:
    half = n/2
    hashmap = defaultdict(int)
    for i in arr:
        hashmap[i] += 1
    check = 0
    for num, count in hashmap.items():
        if count > half:
            print(num)
            check += 1
            break
    if check == 0:
        print(-1)

# If t=4, print out median
elif t == 4:
    arr.sort()
    if n % 2 == 1:
        print(arr[int(n/2)])
    else:
        print(arr[int(n/2 - 1)], arr[int(n/2)])

# If t=5, print numbers between 100-999 sorted
elif t == 5:
    arr.sort()
    for i in arr:
        if i >= 100 and i <= 999:
            print(i,end=" ")
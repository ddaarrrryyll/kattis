"""
INPUT: The first line of the input contains an integer N and t (3≤N≤200000; 1≤t≤7). The second line of the input contains N non-negative 32-bit signed integers.
OUTPUT: For each test case, output the required answer based on the value of t.
"""
info = input().split(" ")
n, t = int(info[0]), int(info[1])
arr = input().split(" ")
for i in range(len(arr)):
    arr[i] = int(arr[i])

# If t = 1, Print 7
if t == 1:
    print(7)

# If t = 2, compare first and second ints in arr
elif t == 2:
    if arr[0] > arr[1]:
        print("Bigger")
    elif arr[0] == arr[1]:
        print("Equal")
    else:
        print("Smaller")

# If t = 3, print the median of 3 integers
elif t == 3:
    med = []
    for i in range(3):
        med.append(arr[i])
    med.sort()
    print(med[1])

# If t = 4, print the sum of all integers in arr
elif t == 4:
    count = 0
    for i in arr:
        count += i
    print(count)

# If t = 5, print the sum of all even integers in arr
elif t == 5:
    count = 0
    for i in arr:
        if i % 2 == 0:
            count += i
        else:
            count += 0
    print(count)

# If t = 6, % 26 to each int, map alphabet to int, print arr as string
elif t == 6:
    for i in range(len(arr)):
        num = (arr[i] % 26) + 1
        arr[i] = chr(ord('`')+num)
    print("".join(arr))

# cyclic
elif t == 7:
    ind = arr[0]
    check = set([])
    while True:
        if ind in check:
            print("Cyclic")
            break
        elif ind == n-1:
            print("Done")
            break
        elif ind < 0 or ind >= n:
            print("Out")
            break
        else:
            check.add(ind)
            ind = arr[ind]
        
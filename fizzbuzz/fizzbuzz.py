#INPUT: Input contains a single test case. Each test case contains three integers on a single line, X, Y and N (1≤X<Y≤N≤100).

#OUTPUT: Print integers from 1 to N in order, each on its own line, replacing the ones divisible by X with Fizz, 
#        the ones divisible by Y with Buzz and ones divisible by both X and Y with FizzBuzz.

# import module
import sys

# read stdin
i = sys.stdin.readline().split()
x = int(i[0])
y = int(i[1])
n = int(i[2])

for fizzbuzz in range(1, n+1):
    if fizzbuzz % x == 0 and fizzbuzz % y == 0:
        print("FizzBuzz")
        continue
    elif fizzbuzz % x == 0:
        print("Fizz")
        continue
    elif fizzbuzz % y == 0:
        print("Buzz")
        continue
    else:
        print(fizzbuzz)
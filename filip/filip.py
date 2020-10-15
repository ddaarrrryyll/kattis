#INPUT: The first and only line of input contains two three-digit numbers, A and B. A and B will not be equal and will not contain any zeroes.

#OUTPUT: The first and only line of output should contain the larger of the numbers in the input, compared as described in the task. 
#        The number should be written reversed, to display to Filip how he should read it.

i = input()
nums = i[::-1].split(" ")
biggest = 0
for num in nums:
    if int(num) > int(biggest):
        biggest = num
print(biggest)
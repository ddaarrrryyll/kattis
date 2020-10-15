# INPUT: Input consists of a sequence of lines, each containing five nonnegative integers separated by whitespace. The five numbers are: a, b, s, m, and n, respectively. 
#        All numbers are positive integers not greater than 10000.
# OUTPUT: For each input line except the last, output a line containing two real numbers (rounded to exactly two decimal places) separated by a single space. 
#         The first number is the measure of the angle A in degrees and the second is the velocity of the ball measured in inches per second, according to the description above
# a = inches (horizontal)
# b = inches (vertical)
# s = time
# m = number of bounces (vertical)
# n = number of bounces (horizontal)
import math

while True:
    info = input().split(" ")
    if info == ['0', '0', '0', '0', '0']:
        break
    a,b,s,m,n = (int(x) for x in info)
    horizontal = a * m
    vertical = b * n
    total_distance = math.hypot(horizontal, vertical)
    velocity = total_distance / s
    if horizontal == 0:
        angle = 90
    else:
        angle = math.degrees(math.atan(vertical / horizontal))
    print('{:0.2f} {:0.2f}'.format(angle,velocity))
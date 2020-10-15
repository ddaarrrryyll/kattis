"""
INPUT: The input has three lines. Each line has three non-zero digits separated by a single space. The digits describe the order in which the pivots are visited. Every digit from 1 to 9 
    appears exactly once. 
OUTPUT: Output the total length of the unlock pattern. Your answer is considered correct if it has an absolute or relative error of at most 10−6 from the correct answer.
"""

current_num = 1
dist = 0

grid = []
for i in range(3):
    # Add sequence of move into a matrix
    grid.append([int(i) for i in input().split()])

def find_num(current_num):
    # Find and return positions of each move starting from 1
    for x in range(3):
        for y in range(3):
            if (grid[y][x] == current_num):
                return (y, x)

while(current_num < 9):
    start_place = find_num(current_num)
    next_place = find_num(current_num + 1)
    # Distance between two points = sqrt[(y2 - y1)^2 + (x2 - x1)^2]
    dist += (((next_place[1] - start_place[1]) ** 2) + (next_place[0] - start_place[0]) ** 2) ** 0.5
    current_num += 1
print(dist)
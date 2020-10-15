"""
INPUT: A single line containing a string of at least 1 and at most 1000000 characters, consisting of the letters ‘R’, ‘B’ and ‘L’.
OUTPUT: a single string consisting of the letters denoting the moves that are to be made in succession by the mech in order to defeat the monster.
"""

moves = input()

counter = 0
while counter < len(moves):
    if counter < len(moves) - 2:
        first = moves[counter]
        second = moves[counter + 1]
        third = moves[counter + 2]
        if first != second and first != third and second != third:
            print("C", end="")
            counter += 3
            continue
    move = moves[counter]
    if move == "R":
        print("S", end="")
    elif move == "B":
        print("K", end="")
    elif move == "L":
        print("H", end="")
    counter += 1
    
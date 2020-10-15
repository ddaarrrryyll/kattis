"""
INPUT:  Provided on multiple lines with up to 10 cases
        Begin with a float d (0 < d < 1000), followed by integer N (1 ≤ N ≤ 100), the number of hives.
        Next N lines contain 2 floats x,y seperated by single space (−1000≤x,y≤1000), position of each hive on plane
        Termination occurs at 0.0 0
OUTPUT: For each case output a line of the following form: a sour, b sweet where a and b are the number of hives producing sour and sweet honey, respectively.
"""
import math
from collections import defaultdict

printouts = []
while True:
    info = input().split(" ")
    if info[0] == "0.0" and info[1] == "0":
        break
    coords = []
    # distances = []
    beehives = defaultdict(lambda: "Sweet")
    for hive in range(0, int(info[1])):
        x_pos,y_pos = input().split(" ")
        x_pos = float(x_pos)
        y_pos = float(y_pos)
        coords.append((x_pos, y_pos))
        beehives[hive]

        if hive > 0:
            for i in coords:
                if (x_pos, y_pos) != i:
                    x = x_pos - i[0]
                    y = y_pos - i[1]
                    distance = math.sqrt(x ** 2 + y ** 2)
                    # distances.append(distance)
                    if distance < float(info[0]):
                        beehives[hive] = "Sour"
                        beehives[coords.index(i)] = "Sour"
                        break
                else:
                    continue           
    sour = 0
    sweet = 0
    for taste in beehives.values():
        if taste == "Sour":
            sour += 1
        else:
            sweet += 1
    printout = str(sour) + " sour, " + str(sweet) + " sweet"
    printouts.append(printout)
    # print(coords)
    # print(distances)
    # print(beehives)
for printout in printouts:
    print(printout)
    
    
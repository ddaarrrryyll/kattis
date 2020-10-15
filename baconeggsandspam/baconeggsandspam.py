"""
INPUT: Input consists of descriptions of up to 100 days’ worth of diner orders. The description of each day starts with a line containing an integer, 1≤n≤20, giving the number of customers 
    who visit the diner. This is followed by n lines, each starting with the name of an individual. The remainder of the line is a non-empty, space-separated list of up to 10 unique menu 
    items ordered by the individual. Each individual’s name is unique and appears at most once on a given day. Each name has at most 15 characters (all A–Z) beginning with an uppercase 
    letter (lowercase characters may follow). All menu items have up to 15 characters using only a–z (lowercase) and ‘-’ (dash). Input terminates with a value of zero for n.
OUTPUT: For each day, print out a report of who ordered each menu item, one line per menu item. The line should give the name of the menu item, followed by a space-separated list of all 
    the people who ordered it. The list of menu items for a given day should be sorted lexicographically, and the list of names reported for an item should also be sorted lexicographically.
    Print a blank line after the report for each day.
"""
from collections import defaultdict

while True:
    n = int(input())
    if n == 0:
        break
    
    # Initialise dictionary to store name + meal
    d = defaultdict(list)
    for i in range(n):
        # Split name + meals
        name_meals = input().split()
        # Add meals as values to name (key)
        for meal in name_meals[1:]:
            name = name_meals[0]
            d[meal].append(name)
    # Sort names(keys) alphabetically
    for k in sorted(d.keys()):
        # Sort meals(values) alphabetically
        print(k, " ".join(sorted(d[k])))
    print()
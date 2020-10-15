"""
INPUT:  The input consists of a single line containing three positive integers s v1 v2, where s≤10^6 is the volume of 
        the shipment, and v1,v2≤10^6 are the volumes of the two types of bottles, with v1>v2.
OUTPUT: Output the number of bottles of size v1 and the number of bottles of size v2 which satisfy Peter’s two conditions. If the conditions cannot be met, output Impossible.
"""
def main():
    total, big, small = input().split(" ")
    total = int(total)
    big = int(big)
    small = int(small)

    return bottledup(total, big, small)

def bottledup(total,big,small):
    no_big = total // big
    remainder = total % big
    i = no_big
    for i in range(no_big, -1, -1):
        if remainder % small == 0 and remainder <= total:
            no_small = remainder // small
            return print(f"{i} {no_small}")
        else:
            remainder += big
    return print("Impossible")


if __name__ == "__main__":
    main()
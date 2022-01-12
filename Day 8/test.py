import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

lst = ["GA", "BU", "ZO", "MEU"]
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

lst1 = []
def ten(a):
    if a < 4:
        lst1.insert(0,lst[a])
        return 0
    ten(a//4)
    lst1.append(lst[a%4])
    return lst1

print("".join(ten(n)))



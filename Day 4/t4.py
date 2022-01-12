import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
x = 0
for i in range(n-2,1,-1):
    for j in range(n-3,0,-1):
        if j == 1:
            x = i
            break
        if i%j == 0 and n%j == 0:
            break
    if x > 0:
        break

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(str(x))

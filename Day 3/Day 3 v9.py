import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
max = 0
count = 0
r, c = [int(i) for i in input().split()]
for i in range(1,r):
    for j in range(1,c):
        k = int(input().split()[j])
        if max < k:
            count += 1
            max = k
if count == 0:
    max = -666


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(max)
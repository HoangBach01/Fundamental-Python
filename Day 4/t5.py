import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
t = ""
s = input().split()
for j in range(len(s)):
    if j == len(s)-1:
        for i in range(len(s[j])-1,-1,-1):
            t += str(s[j][i])
    else: 
        for i in range(len(s[j])-1,-1,-1):
            t += str(s[j][i])
        t+= " "


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(str(t))

print(" ".join([word[::-1] for word in s]))

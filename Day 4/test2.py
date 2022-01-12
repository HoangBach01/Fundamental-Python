import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = input()
mark = 0
valid = True
number = 0
uper = 0
space = 0
lower = 0
special = 0

for char in l:
    if char.isdigit():
        number += 1
    elif char.isupper():
        uper += 1
    elif char.islower():
        lower += 1
    elif char.isspace():
        space += 1
    elif char == "!" or char == "." or char == "," or char == "&" or char == "-" or char == "@":
        special += 1

if len(l) < 8 or len(l) > 15 or space >0 or number == 0 or uper == 0:
    valid = False
else:
    valid = True

mark = space*0 + uper*10 + lower*5 + number*1 + special*25
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(str(valid) +', '+ str(mark))

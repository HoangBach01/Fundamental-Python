import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

sentence = input()
v = list("a e i o u A E I O U".split())
r = []
for i in sentence:
    r.append(i)
    if i in v:
        r.append("p")
        r.append(i)
result = "".join(map(str,r))
print(result)
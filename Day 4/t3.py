import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
scentence = []
check = False
y = []
for i in range(n):
    x = input().split()
    for j in range(len(x)):
        if x[j] in scentence:
            check = True
            for k in range(j+1,len(x)):
                if k not in scentence:
                    check = False
            if check == True:
                break
        scentence.append(x[j])
        

# c = ' '.join(word for word in scentence)
print(scentence)


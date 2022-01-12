import math

# Create number input
while True:
    try:
        number = int(input("Number: "))
        break
    except ValueError:
        print("Please type in number only.")

# Convert number into list
# i = 0
# r = number
# lis = []
# while (r>0):
#     lis.append(r%10)
#     r = int(r/10)
#     i += 1
lis = list(map(int,str(number)))
lis.reverse()

# Check valid algorithm
sum_prod = 0
valid = True
for j in range(1, len(lis), 2):
    if lis[j] * 2 >= 10:
        sum_prod += lis[j] * 2 - 10 + 1
    else:
        sum_prod += lis[j] * 2
for k in range(0, len(lis), 2):
    sum_prod += lis[k]
if sum_prod % 10 == 0:
    valid = True
else:
    valid = False

# Check name when valid algorithm
start_num = lis[len(lis)-1] * 10 + lis[len(lis)-2]
if valid == True:
    if (len(lis) == 15 and (start_num == 34 or start_num == 37)):
        print("AMEX")
    elif (len(lis) == 16 and (start_num == 51 or start_num == 52 or start_num == 53 or start_num == 54 or start_num == 55)):
        print("MASTERCARD")
    elif ((len(lis) == 13 or len(lis) == 16) and start_num//10 == 4):
        print("VISA")
    else:
        print("INVALID")
else:
    print("INVALID")
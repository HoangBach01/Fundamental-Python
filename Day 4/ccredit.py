import math
import random

# Create input option cards
list_card = ['VISA', 'MASTERCARD', 'AMEX']
card = str(input("Which Credit card number you want to fake (VISA, MASTERCARD, AMEX): ")).upper()
while card not in list_card:
    card = str(input("VISA or MASTERCARD or AMEX?: "))
len_card = [16, 16, 15]

# Create function add random intergers to card
def add_int(lis,n):
    for i in range(n-3):
        lis.append(random.randint(0,9))
    return

# Create function calculate the end number
def end_number(lis):
    sum_prod = 0
    x = 0
    for i in range(len(lis)-1,-1,-2):
        if lis[i]*2 >= 10:
            sum_prod += lis[i]*2 - 10 + 1
        else:
            sum_prod += lis[i]*2
    for j in range(len(lis)-2,-1,-2):
        sum_prod += lis[j]
    x = 10 - sum_prod%10
    lis.append(x)
    return

# Add random valid second number to card number & calculate end number
if card == "VISA":
    visa = [4]
    visa.append(random.randint(0,9))
    add_int(visa,len_card[0])
    end_number(visa)
    visa_str = ''.join(map(str, visa))
    print(visa_str)
elif card == "MASTERCARD":
    master = [5]
    master.append(random.randint(1,5))
    add_int(master,len_card[1])
    end_number(master)
    master_str = ''.join(map(str, master))
    print(master_str)
else:
    amex = [3]
    amex.append(random.randrange(4,8,3))
    add_int(amex,len_card[2])
    end_number(amex)
    amex_str = ''.join(map(str, amex))
    print(amex_str)



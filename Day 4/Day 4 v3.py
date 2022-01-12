# Xây dựng chương trình giải phương trình bậc 2:      ax^2 + bx + c = 0 
# - Người dùng nhập vào a, b, c (Input)
# - Dựa vào quy tắc xử lý trong file đính kèm, chương trình sẽ giải phương trình bậc 2 
# và in ra nghiệm x1, x2 (Output)

import math

a = eval(input("a: "))
b = eval(input("b: "))
c = eval(input("c: "))

kl1 = "Phương trình vô nghiệm!"
kl2 = "Phương trình có vô số nghiệm"
kl3 = "Phương trình có nghiệm: "
if a == 0:
    if b == 0: 
        if c != 0:
            print(kl1)
        else:
            print(kl2)
    else:
        print(kl3 + " x = " + str(-c/b))
else:
    deta = math.pow(b,2) - 4*a*c
    if deta < 0:
        print(kl1)
    elif deta == 0:
        print(kl3 + " kép x1 = x2 = " + str(-b/(2*a)))
    else:
        print(kl3 + " x1 = " + str(round((-b + math.sqrt(deta))/(2*a),2)))
        print(kl3 + " x2 = " + str(round((-b - math.sqrt(deta))/(2*a),2)))
        print("Note: Kết quả được làm tròn đến chữ số thập phân thứ 2.")

    


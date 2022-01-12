# Viết chương trình Tính tổng các số nguyên tố trong list có n phần tử, mỗi phần tử có giá trị ngẫu nhiên.
#      - Sử dụng console
#      - Hãy viết chương trình cho phép người dùng nhập vào số nguyên n là số phần tử cho list. 
# => Chương trình tự động phát sinh giá trị (giá trị trong khoảng 0 - 100) cho các phần tử trong list => Xuất list
#      - Tính tổng các số nguyên tố trong list 
#      - Gợi ý: Dùng hàm randrange ([start,] stop [,step]) để tạo số ngẫu nhiên

from random import randrange

# Hãy viết chương trình cho phép người dùng nhập vào số nguyên n là số phần tử cho list. 
while True:
    try:
        n = int(input("Nhập số nguyên n: "))
        if n > 0:
            break
    except ValueError:
        pass

# => Chương trình tự động phát sinh giá trị (giá trị trong khoảng 0 - 100) cho các phần tử trong list => Xuất list
lst = []
for i in range(n):
    lst.append(randrange(0,100))
print("List: ", lst)

# Tính tổng các số nguyên tố trong list 
prime_lst = []
for i in lst:
    if i == 1 or i == 2:
        prime_lst.append(i)
    elif i > 2:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            prime_lst.append(i)
    else:
        pass

print("Các số nguyên tố trong list là: ", prime_lst)
s_prime_lst = sum(map(int, prime_lst))
print("Tổng các số nguyên tố trong list là: ", s_prime_lst)
# Học viên viết lại các bài tập của Bài 5 (Tính S, Tính A, và Kiểm tra số nguyên tố) bằng cách xây dựng phương thức/ hàm.

# Hướng dẫn:
# -  Bài Tính S:
# Xây dựng phương thức tinh_S(n, x): với n và x là tham số truyền vào, phương thức có giá trị trả về là  S =  (x^2+ 1)^n

n = 3
x = 5
def s(n, x): return (x**2 + 1)**n


print("S= {:3,d}".format(s(n, x)))

# -  Bài Tính A:
# Xây dựng phương thức tinh_A(n, x): với n và x là tham số truyền vào, phương thức có giá trị trả về là  A = (x^2 + x + 1)^n + (x^2 - x + 1)^n


def a(n, x): return (x**2 + x + 1)**n + (x**2 - x + 1)**n


print("A= {:3,d}".format(a(n, x)))
# -  Bài Kiểm tra số nguyên tố:
# Xây dựng phương thức kiem_tra_so_nguyen_to(x): x là tham số truyền vào, phương thức có giá trị trả về là True nếu x là số nguyên tố, có giá trị trả về là False nếu x không là số nguyên tố


def check_prime(x):
    if x == 1 or x == 2:
        return True
    elif x > 2:
        for i in range(2, x):
            if x % i == 0:
                return False
                break
        return True
    else:
        return False


x = int(input("x: "))
print("Prime number or not? ", check_prime(x))

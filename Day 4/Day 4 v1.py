# Học viên viết lại bài tìm giá trị lớn nhất, nhỏ nhất (Bài 4.1) bằng cách sử dụng hàm max, min của thư viện Numbers.
# Xây dựng chương trình Python cho giải thuật Tìm số lớn nhất - nhỏ nhất như sau:
# 1. Nhập vào bốn số: a, b, c, d

# #Tìm giá trị lớn nhất
# 2. Giả sử gtln là a
# 3. Nếu gtln < b thì gtln là b
# 4. Nếu gtln < c thì gtln là c
# 5. Nếu gtln < d thì  gtln là d
# 6. In ra kết quả giá trị lớn nhất

# #Tìm giá trị nhỏ nhất, tương tự như tìm giá trị lớn nhất, 
# # In ra kết quả giá trị nhỏ nhất
import math

a = input("Nhập a: ")
b = input("Nhập b: ")
c = input("Nhập c: ")
d = input("Nhập d: ")

e = max(a, b, c, d)
print("Giá trị lớn nhất là: ", e)


n = eval(input("Nhập số n: "))
a = abs(n)
print("Trị tuyệt đối của n là: ", a)




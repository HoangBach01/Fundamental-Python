# Xây dựng chương trình tính và in ra kết quả của biểu thức S =  (x^2 + 1)^n
# - Người dùng nhập vào một số nguyên n và một số thực x (Input). 
# - Chương trình sẽ tính S =  (x^2 + 1)^n 
# và in ra Tổng S (Output).

x = eval(input("So thuc x la: "))
n = int(input("So nguyen n la: "))
i = 1
s = 1
s1 = x**2 + 1
while i <= n:
    s *= s1
    i += 1
print(s)
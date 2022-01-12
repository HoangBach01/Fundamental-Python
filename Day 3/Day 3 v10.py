# Xây dựng chương trình tính và in ra kết quả của biểu thức A = (x^2 + x + 1)^n + (x^2 - x + 1)^n
# - Người dùng nhập vào một số nguyên n và một số thực x (input)
# - Chương trình sẽ tính A = (x^2 + x + 1)^n + (x^2 - x + 1)^n 
# và in ra kết quả A (output)

n = int(input("n: "))
x = int(input("x: "))

b = x**2 + x + 1
c = x**2 - x + 1

i = 1
while i <= n:
    b *= b
    c *= c
    i += 1

A = b + c
print(f'{A:,.0f}')
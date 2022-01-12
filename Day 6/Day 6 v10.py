# Xây dựng chương trình tính và in ra kết quả của biểu thức A = (x^2 + x + 1)^n + (x^2 - x + 1)^n
# - Người dùng nhập vào một số nguyên n và một số thực x (input)
# - Chương trình sẽ tính A = (x^2 + x + 1)^n + (x^2 - x + 1)^n 
# và in ra kết quả A (output)

n = int(input("n: "))
x = eval(input("x: "))
a = lambda n,x: (x**2 + x + 1)**n + (x**2 - x + 1)**n
print("A= {:3,d}".format(a(n,x)))
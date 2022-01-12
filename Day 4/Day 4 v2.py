# Viết lại bài tính S =  (x^2 + 1)^n trong bài trước bằng cách sử dụng hàm thư viện Numbers.
import math

x = eval(input("x: "))
n = eval(input("n: "))

s = math.pow((math.pow(x,2) + 1),n)

print(s)

# Viết lại bài 5.3, tính : A = (x^2 + x + 1)^n + (x^2 - x + 1)^n bằng cách sử dụng hàm thư viện Numbers.

t = math.pow(math.pow(x,2) + x + 1,n) + math.pow(math.pow(x,2) - x + 1,n)

print(t)
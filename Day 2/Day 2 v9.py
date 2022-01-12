a = eval(input("Nhap a: "))
b = eval(input("Nhap b: "))
c = eval(input("Nhap c: "))
d = eval(input("Nhap d: "))
max = 0
if a>b and a>c and a>d:
    max = a
elif b>a and b>c and b > d:
    max = b
elif c>a and c>b and c > d:
    max = c
else:
    max = d
print(max)


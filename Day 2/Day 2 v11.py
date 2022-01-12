# Tim gia tri tuyet doi cua mot so
x = eval(input("Nhap so nguyen: "))
while type(x) != int:
    x = eval(input("Nhap so nguyen: "))
if x >0:
    sqrtx = x
else:
    sqrtx = -x
print(sqrtx)
x = eval(input("Nhap so nguyen co 3 chu so: "))
while x <100 or x >999 or type(x) is not int:
    x = eval(input("Nhap so nguyen co 3 chu so: "))
x1 = x//100
x2 = (x-x1*100)//10
x3 = (x-x1*100-x2*10)
y = x3*100 + x2*10 + x1
print("So nghich dao la %03d" %y)
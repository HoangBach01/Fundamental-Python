# Tinh tien dien

# Nhap loai hinh thanh toan
print("Ban dang su dung dien loai nao?")
method = eval(input("Nhap 1 neu la tra sau, 2 neu la tra truoc: "))
while method != 1 and method !=2:
    print("Loai hinh su dung khong hop le.")
    method = eval(input("Nhap 1 neu la tra sau, 2 neu la tra truoc: "))

# Nhap tong cong suat dien tieu thu
x = eval(input("Nhap tong so dien tieu thu (#kWh): "))
while x <=0 or type(x) is not int:
    print("So dien tieu thu khong hop le.")
    x = eval(input("Nhap tong so dien tieu thu (#kWh): "))

# Bac thang
y1 = 50
y2 = 100
y3 = 200
y4 = 300
y5 = 400

# Tien dien theo tung bac, tra sau
p1 = 1678
p2 = 1734
p3 = 2014
p4 = 2536
p5 = 2834
p6 = 2927

# Xu ly tien dien tra sau theo bac thang
count = 0
if x > y5:
    count = 6
    price1 = y1*p1 + y2*p2 + y3*p3 + y4*p4 + y5*p5 + (x-y5)*p6
elif x > y4:
    count = 5
    price1 = y1*p1 + y2*p2 + y3*p3 + y4*p4 + (x-y4)*p5
elif x > y3:
    count = 4
    price1 = y1*p1 + y2*p2 + y3*p3 + (x-y3)*p4
elif x > y2:
    count = 3
    price1 = y1*p1 + y2*p2 + (x-y2)*p3
elif x > y1:
    count = 2
    price1 = y1*p1 + (x-y1)*p2
else:
    count = 1
    price1 = x*p1


# Tien dien tra truoc
ptt = 2461

price2 = ptt*x

# Xuat ket qua
if method == 1:
    print("Tien dien cua ban la (tra sau): %i" %price1)
else:
    print("Tien dien cua ban la (tra truoc): %i" %price2)
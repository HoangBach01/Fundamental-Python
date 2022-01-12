# Nhap loai xe
x = eval(input("Nhap loai xe ma ban muon di (4 or 7 cho): "))
while x != 4 and x != 7:
    print("Loai xe cua ban khong hop le.")
    x = eval(input("Nhap loai xe ma ban muon di (4 or 7 cho): "))

# Nhap so km
s = eval(input("Nhap quang duong di chuyen (#km): "))
while s<0:
    print("Quang duong khong hop le.")
    s = eval(input("Nhap quang duong di chuyen (#km): "))
if s < 0.8:
    s_less_31km = 0
    s_more_31km = 0
elif s < 31:
    s_less_31km = s - 0.8
    s_more_31km = 0
else:
    s_less_31km = 31 - 0.8
    s_more_31km = s-31

# Nhap thoi gian di chuyen
time = eval(input("Nhap thoi gian di chuyen (#phut): "))
while time<0:
    print("Quang duong khong hop le.")
    time = eval(input("Nhap thoi gian di chuyen (#phut): "))

# Thong so xe 4 cho
price4_open = 11000
price4_less_31km = 15300
price4_more_31km = 12100

# Tien time di chuyen xe 4 cho
price_taxi4 = price4_open + s_less_31km * price4_less_31km + s_more_31km * price4_more_31km 

# Thong so xe 7 cho
price7_open = 12000
price7_less_31km = 16100
price7_more_31km = 13800

# Tien time di chuyen xe 7 cho
price_taxi7 = price7_open + s_less_31km * price7_less_31km + s_more_31km * price7_more_31km 

# Tien time di chuyen
if time >5:
    price_time = (time - 5)*750
else:
    price_time = 0

# Tinh tien taxi
if x == 4:
    taxi = price_taxi4 + price_time
    print("Tong so tien cho taxi la: %i" %price_time)
    print("Tong so tien di chuyen taxi la: %i" %price_taxi4)
    print("Tong so tien taxi la: %i" %taxi)
else:
    taxi = price_taxi7 + price_time
    print("Tong so tien cho taxi la: %i" %price_time)
    print("Tong so tien di chuyen taxi la: %i" %price_taxi7)
    print("Tong so tien taxi la: %i" %taxi)  


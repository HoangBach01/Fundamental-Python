# Tao chuong trinh tinh thue thu nhap ca nhan
# Nhap du lieu
tax_id = eval(input("Ma so thue cua ban la: "))
name = input("Ho va ten cua ban la: ")
salary = eval(input("Tong thu nhap trong thang cua ban la: "))
dependent = eval(input("So nguoi phu thuoc cua ban la: "))

# Xu ly so lieu, (s = thu nhap chiu thue)
s_million = salary / 1000000
d1 = 9
d2 = 3.6
s = s_million - d1 - dependent * d2

# Nhap cac bac thue
tax_step = [0,5,10,18,32,52,80]
tax_rate = [0.05,0.1,0.15,0.2,0.25,0.3,0.35]

# Tim bac thue dang chiu
steps = 0
for i in range(6,-1,-1):
    if s > tax_step[i]:
        steps = i + 1
        break

# Tien thue phai dong
tax_payment = (s - tax_step[steps-1]) * tax_rate[steps-1]
for j in range(steps -1,0,-1):
    tax_payment = tax_payment + (tax_step[j] - tax_step[j-1])*tax_rate[j-1]

# Tien luong sau thue
real_salary = s_million - tax_payment
# Print ket qua
print("")
print("******************************************")
print("Tinh Thue thu nhap ca nhan")
print("******************************************")
print("")
print("Ma so thue                   : %i" %tax_id)
print("Ho va ten doi tuong nop thue : %s" %name)
print("Tong thu nhap trong nam      : " f'{salary:,.0f}')
print("So nguoi phu thuoc           : %i" %dependent)
print("")
print("******************************************")
print("So tien giam tru             : " f'{(d1 + dependent * d2)*1000000:,.0f}')
print("So tien chiu thue            : " f'{s*1000000:,.0f}')
print("Bac luong chiu thue cao nhat : %i" %steps)
print("So tien thue phai nop        : " f'{tax_payment*1000000:,.0f}')
print("So tien nhan duoc sau thue   : " f'{real_salary*1000000:,.0f}')

print("CHƯƠNG TRÌNH CHUYỂN ĐỔI GIỮA 3 ĐƠN VỊ cm, inch, foot")
print("\t 1- Từ cm sang inch")
print("\t 2- Từ cm sang foot")
print("\t 3- Từ inch sang cm")
print("\t 4- Từ inch sang foot")
print("\t 5- Từ foot sang cm")
print("\t 6- Từ foot sang inch")
print("\t 0- Kết thúc chương trình")

n = 7
while True:
    try:
        n = int(input("Bạn chọn chức năng (0-6): "))
        if n >=0 and n <=6:
            x = float(input("Nhập số đơn vị: "))
            break
    except Exception:
        print("Vui lòng nhập số nguyên (0-6")
inch_cm = 2.54
inch_foot = 12
cm_inch = 0.3937008
cm_foot = cm_inch * inch_foot

def inch_to_cm(x):
    print("Số cm là: %.2f" %(inch_cm * x))
def inch_to_foot(x):
    print("Số foot là: %.2f" %(inch_foot * x))
def cm_to_inch(x):
    print("Số inch là: %.2f" %(cm_inch * x))
def cm_to_foot(x):
    print("Số foot là: %.2f" %(cm_inch * inch_foot * x))
def foot_to_cm(x):
    print("Số cm là: %.2f" %(1/cm_foot * x))
def foot_to_inch(x):
    print("Số inch là: %.2f" %(1/inch_foot * x))

if n == 0:
    print("Kết thúc chương trình!")
elif n == 1:
    cm_to_inch(x)
elif n == 2:
    cm_to_foot(x)
elif n == 3:
    inch_to_cm(x)
elif n == 4:
    inch_to_foot(x)
elif n == 5:
    foot_to_cm(x)
else:
    foot_to_inch(x)
    


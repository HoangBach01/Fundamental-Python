# Kiem tra ngay thang nam nhap vao

# Cau truc dd/mm/yyyy

date = input("Moi ban nhap ngay thang nam theo dd/mm/yyyy: ")

# Function check interger
def isint(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

# Check cau truc
while isint(date[0:2]) == False or isint(date[3:5]) == False or isint(date[6:]) == False or date[2] != "/" or date[5] != "/":
    print("Cau truc nhap khong hop le.")
    date = input("Moi ban nhap ngay thang nam theo dd/mm/yyyy: ")

day = int(date[0:2])
month = int(date[3:5])
year = int(date[6:])

# list max month and max day in each month
maxmonth = 12
maxday = [31,29,31,30,31,30,31,31,30,31,30,31]

check_day = 0
check_month = 0

if month <= 12 and month >= 1:
    check_month = 1
    print("Month check: ok!")
    if day <= maxday[month-1] and day >= 1:
        check_day = 1
        print("Day check: ok!")
    else:
        check_day = 0
        print("Day check: error!")
else:
    check_month = 0
    print("Month check: error!")



if check_day == 1 and check_month == 1:
    print("Ngay thang nam %s la hop le" %date)
else:
    print("Ngay thang nam %s la khong hop le" %date)
print("Nhập thông tin danh sách nhân viên ")
dic = {}
n = -1
while True:
    key = str(input("Nhập mã nhân viên: "))
    value = []
    value.append(str(input("Nhập tên nhân viên: ")))
    value.append(str(input("Nhập số điện thoại: ")))
    while True:
        try:
            value.append(int(input("Nhập lương: ")))
            break
        except Exception:
            pass
    dic[key] = value
    while True:
        try:
            n = int(input("Nhập giá trị tiếp không? 1: Có, 0: Không: "))
        except Exception:
            pass
        if n == 1 or n == 0:
            break
    if n == 0:
        break
dsnv = "DANH SÁCH NHÂN VIÊN"
print(dsnv.center(50,"*"))
print("Mã NV \t Họ tên \t Số điện thoại \t Lương")
for key, value in dic.items():
    print(key, "\t", value[0], "\t", value[1], "\t", value[2])
m = -1
count = 0
while True:    
    x = str(input("Nhập mã nhân viên cần tìm: "))
    for key in dic.keys():
        if x == key:
            print("Thông tin nhân viên: ")
            lst3 = dic[key]
            lst3.insert(0,key)
            print(lst3)
            count = 1
    if count == 0:
        print("Không tìm thấy nhân viên với mã trên.")
    while True:
        try:
            m = int(input("Bạn muốn tìm tiếp không? 1: Có, 0: Không: "))
        except Exception:
            pass
        if m == 1 or m == 0:
            break
    if m == 0:
        break


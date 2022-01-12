# Học viên bổ sung xử lý ngoại lệ cho xử lý của bài tập Kiểm tra số nguyên tố.

# Ví dụ: Người dùng nhập vào chuỗi, hoặc số thực => lỗi ?

'''
Created on October 24, 2019

@author: Trung Tâm Tin Học - Trường Đại học Khoa học Tự nhiên TP.HCM
'''


def kiem_tra_so_nguyen_to(so):
    if so < 2:
        return False
    else:
        for i in range(2, so):
            if so % i == 0:
                return False
                break
        else:
            return True


while True:
    try:
        x = int(input("Nhập x: "))
        break
    except Exception:
        print("Giá trị vừa nhập không hợp lệ.")

kq = kiem_tra_so_nguyen_to(x)
if kq:
    print("%i là số nguyên tố." % x)
else:
    print("%i không là số nguyên tố." % x)

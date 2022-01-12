# Học viên bổ sung xử lý ngoại lệ cho xử lý của bài tập Giải phương trình bậc 1.
'''
Created on October 24, 2019

@author: Trung Tâm Tin Học - Trường Đại học Khoa học Tự nhiên TP.HCM
'''

def giai_pt_bac_1(a, b):
    if a != 0:
        x = -b / a
        print("Phương trình có 1 nghiệm x =", x)
    else:
        if b == 0:
            print("Phương trình có vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")

try:
    a = 0
    b = 3
    giai_pt_bac_1(a, b)
except Exception:
    print("Giá trị a,b không hợp lệ.")
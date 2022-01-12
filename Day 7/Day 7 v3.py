# Học viên bổ sung xử lý ngoại lệ cho xử lý của bài tập Tìm giá trị tuyệt đối của một số.

# Ví dụ:  input x = abc  => lỗi ?

'''
Created on October 24, 2019

@author: Trung Tâm Tin Học - Trường Đại học Khoa học Tự nhiên TP.HCM
'''

while True:
    try:
        x = int(input('Nhập x:\n'))
        break
    except ValueError:
        print("Vui lòng nhập số nguyên!")

abs_x = x
if abs_x < 0:
    abs_x = - abs_x
    print('|%d| = %d'%(x, abs_x))
else:
    print('|%d| = %d'%(x, abs_x))
    
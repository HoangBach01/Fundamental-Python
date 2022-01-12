# Xây dựng chương trình tính và in ra kết quả của biểu thức (Hình 10.1)
# - Người dùng nhập x, y từ bàn phím.
# - Chương trình sẽ tính và in ra kết quả của biểu thức A.
# Học viên bổ sung ngoại lệ cho phần xử lý
'''
Created on October 23, 2019

@author: Trung Tâm Tin Học - Trường Đại học Khoa học Tự nhiên TP.HCM
'''

import math

# Bổ sung ngoại lệ cho phần xử lý

def tinh_gtbt_A(x,y):
    A = math.sqrt((5*x - y)/(2*x + 7*y))
    return A

try:
    x = eval(input('Nhập x:\n'))
    y = eval(input('Nhập y:\n'))
    tinh_gtbt_A(x,y)
except (SyntaxError,NameError):
    print("Số vừa nhập không hợp lệ, Vui lòng nhập lại.") 
except ZeroDivisionError:
    print("Lỗi chia cho 0 trong mẫu số của A, vui lòng nhập lại giá trị x, y khác.")
except ValueError:
    print("Lỗi không có căn bậc 2 cho số âm, vui lòng nhập lại giá trị x,y khác.")
else:
    print('A =', tinh_gtbt_A(x,y))
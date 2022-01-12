import sys
sys.path.append('./')
import modules.ham_list_7 as md

'''
Created on October 22, 2019

@author: Trung Tâm Tin Học - Trường Đại học Khoa học Tự nhiên TP.HCM
'''

# Tạo list số và in ra list các số vừa nhập
lst = []
md.tao_list(lst)
print("List hiện có là: ", lst)

# Tính tổng các phần tử trong list
print("Tổng các phần tử trong list là:", md.tinh_tong(lst))

# Tìm và in ra tất cả các số nguyên tố có trong list
lst_nguyen_to = []
for i in lst:
    if md.kiem_tra_so_nguyen_to(i) == True:
        lst_nguyen_to.append(i)

print("Các số nguyên tố trong list là: ", lst_nguyen_to)

# Tính trung bình cộng của các phần tử âm trong list
lst_negative = md.tao_list_am(lst)
print("Trung bình cộng của các phần tử âm trong list là: ", md.tinh_tong(lst_negative)/len(lst_negative))

# Tính trung bình cộng của các phần tử dương trong list
lst_positive = md.tao_list_duong(lst)
print("Trung bình cộng của các phần tử dương trong list là: ", md.tinh_tong(lst_positive)/len(lst_positive))

# Tìm giá trị chẵn lớn nhất trong list 
lst_even = md.tao_list_chan(lst)
print("Giá trị chẵn lớn nhất trong list là ", max(lst_even))

# Tìm giá trị lẻ nhỏ nhất trong list 
lst_odd = md.tao_list_le(lst)
print("Giá trị lẻ nhỏ nhất trong list là ", min(lst_odd))

'''
Created on October 22, 2019

@author: Trung Tâm Tin Học - Trường Đại học Khoa học Tự nhiên TP.HCM
'''

# Phương thức tạo list số, Cho phép người dùng lần lượt nhập các phần tử số cho list cho đến khi không muốn nhập nữa
def tao_list(list_create):
    i = 1
    while i==1:
        number = eval(input('Nhập giá trị:\t'))
        list_create.append(number)    
        i = int(input('Tiếp tục nhập giá trị? 1: Có, 0: không\t'))
    return list_create

# Phương thức tính tổng các phần tử trong list
def tinh_tong(list_create):
    tong = 0
    for item in list_create:
        tong += item
    return tong

# Phương thức kiểm tra số nguyên tố
def kiem_tra_so_nguyen_to(so):
    if so <= 1:
        return False
    count = 0;
    for i in range(1, so+1, 1):
        if so % i == 0:
            count += 1
    return count == 2

# Phương thức tạo list số âm 
def tao_list_am(list_create):
    list_negative = []
    for item in list_create:
        if item < 0:
            list_negative.append(item)
    return list_negative

# Phương thức tạo list số dương
def tao_list_duong(list_create):
    list_positive = []
    for item in list_create:
        if item > 0:
            list_positive.append(item)
    return list_positive

# Phương thức tạo list số chẵn
def tao_list_chan(list_create):
    list_even = []
    for item in list_create:
        if item % 2 == 0:
            list_even.append(item)
    return list_even

# Phương thức tạo list số lẻ
def tao_list_le(list_create):
    list_odd = []
    for item in list_create:
        if item % 2 != 0:
            list_odd.append(item)
    return list_odd

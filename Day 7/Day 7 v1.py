import modules.ham_bai_5 as md

'''
Created on October 22, 2019

@author: Trung Tâm Tin Học - Trường Đại học Khoa học Tự nhiên TP.HCM
'''
n = int(input("Nhập n: "))

# Bài 5 - Kiểm tra số nguyên tố
print("n có phải số nguyên tố không?")
print(md.KiemTraSoNguyenTo(n))

# Bài 5 - In dãy Fibonacci
print("In dãy Fibonacci.")
print(md.fib(n))

# Bài 5 - Tính giá trị biểu thức S
x = int(input("Nhập x: "))
print("Giá trị biểu thức S: ")
print("{:3,d}".format(md.tinh_S(n, x)))

# Bài 5 - Tính giá trị biểu thức A
print("Giá trị biểu thức A: ")
print("{:3,d}".format(md.tinh_A(n, x)))
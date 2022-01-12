'''
Created on October 22, 2019

@author: Trung Tâm Tin Học - Trường Đại học Khoa học Tự nhiên TP.HCM
'''

# Hàm kiểm tra số nguyên tố
def KiemTraSoNguyenTo(so):
    if so<=1:
        return False
    kt=True
    for i in range(2,so):
        if so%i==0:
            kt=False
            break
    return kt


# Hàm về dãy Fibonacci
def fib(n):
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else: 
        return fib(n-1)+fib(n-2)


# Hàm tính  S = (x^2+ 1)^n
def tinh_S(n, x):
    if n == 0:
        return 1
    else:
        S = 1
        for i in range(0,n):
            S = S * (x * x + 1)
        return S


# Hàm tính  A = (x^2 + x + 1)^n + (x^2 - x + 1)^n
def tinh_A(n, x):
    if n==0:
        return 2
    else:
        A1 = 1
        A2 = 1
        for i in range(0,n):
            A1 = A1 * (x * x + x + 1)
            A2 = A2 * (x * x - x + 1)
        return (A1 + A2)

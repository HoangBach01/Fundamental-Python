# Viết chương trình thực hiện việc xử lý trên set như sau: 

# - Khai báo và khởi tạo set1, set2 
#      +  Cho phép người dùng lần lượt nhập các phần tử số cho set1 cho đến khi không muốn nhập nữa 
#      +  Cho phép người dùng lần lượt nhập các phần tử số cho set2 cho đến khi không muốn nhập nữa 

# - Chương trình sẽ thực hiện những công việc sau: 
#      +  In set1, set2 
#      +  Cho biết mỗi set có bao nhiêu phần tử, tổng giá trị các phần tử của mỗi set 
#      +  Tìm giá trị lớn nhất, nhỏ nhất của mỗi set 
#      +  Lấy ra một phần tử ở set1 và in ra phần tử này 
#      +  Thực hiện set union của set1 và set2 và in kết quả 
#      +  Thực hiện set intersection của set1 và set2 và in kết quả 
#      +  Thực hiện set difference của set1 với set2 và in kết quả 
#      +  Thực hiện set symmetric difference của set1 với set2 và in kết quả
#      +  Sắp xếp set1 tăng dần và set2 giảm dần

'''
Created on October 10, 2019

@author: Trung Tâm Tin Học - Trường Đại học Khoa học Tự nhiên TP.HCM
'''


# Khai báo và khởi tạo set1, set2 
# Cho phép người dùng lần lượt nhập các phần tử số cho set1 cho đến khi không muốn nhập nữa
set1=set()
gt="1"
while gt!="":
    gt=input('Nhap gia tri cho set 1 (enter ket thuc): ')
    if gt!="":
        set1.add(int(gt))

# Cho phép người dùng lần lượt nhập các phần tử số cho set2 cho đến khi không muốn nhập nữa
set2=set()
gt="1"
while gt!="":
    gt=input('Nhap gia tri cho set 2 (enter ket thuc): ')
    if gt!="":
        set2.add(int(gt))

# In set1, set2
print("Set 1: ", set1)
print("Set 2: ", set2)

# Cho biết mỗi set có bao nhiêu phần tử 

print("Set 1 có: ", len(set1), "phần tử")
print("Set 2 có: ", len(set2), "phần tử")


# Tổng giá trị các phần tử của mỗi set
sum1 = 0
for i in set1:
    sum1 += i

sum2 = 0
for i in set2:
    sum2 += i

print("Tổng giá trị Set 1 là: ", sum1)
print("Tổng giá trị Set 2 là: ", sum2)


# Tìm giá trị lớn nhất, nhỏ nhất của set1

print("Giá trị nhỏ nhất Set 1 là: ", min(set1))
print("Giá trị lớn nhất Set 1 là: ", max(set1))


# Tìm giá trị lớn nhất, nhỏ nhất của set2

print("Giá trị nhỏ nhất Set 2 là: ", min(set2))
print("Giá trị lớn nhất Set 2 là: ", max(set2))


# Lấy ra một phần tử ở set1 và in ra phần tử này

list1 = list(set1)
print("Một phần tử của Set 1 là: ", list1[len(list1)-1])

# Thực hiện set union của set1 và set2 và in kết quả

set3 = set1 | set2
print("Union của Set 1 và Set 2: ", set3)

# Thực hiện set intersection của set1 và set2 và in kết quả
set4 = set1 & set2
print("Intersection của Set 1 và Set 2: ", set4)

# Thực hiện set difference của set1 với set2 và in kết quả
set5 = set1 - set2
print("Difference của Set 1 và Set 2: ", set5)

# Thực hiện set symmetric difference của set1 với set2 và in kết quả
set6 = set1 ^ set2
print("Symmetric difference của Set 1 và Set 2: ", set6)

# Sắp xếp set1 tăng dần và set2 giảm dần

print("Sắp xếp Set 1 tăng dần:", sorted(set1))
print("Sắp xếp Set 2 giảm dần:", sorted(set2, reverse=True))

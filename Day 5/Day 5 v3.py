# Viết chương trình thực hiện xử lý list số như sau: 

# - Tạo list số:  Cho phép người dùng lần lượt nhập các phần tử số cho list cho đến khi không muốn nhập nữa.
# - Chương trình sẽ thực hiện những công việc sau:
# +  In ra list các số vừa nhập.
# +  Tìm và in ra tất cả các số nguyên tố có trong list.
# +  Tính trung bình cộng của các phần tử âm/ phần tử dương trong list 
# +  Tìm giá trị chẵn lớn nhất/ giá trị lẻ nhỏ nhất trong list 
# +  Sắp xếp list theo giá trị tăng dần 

lst =[]
bool_tuples = ("y","n",1,0,"yes","no")

# +  In ra list các số vừa nhập.
while True:
    while True:
        try:
            lst.append(int(input("Please type your input:\n")))
            break
        except ValueError:
            print("Please enter number only!")
    while True:
        cont = str(input("Do you finish you list? (y/n):\n")).lower()
        if cont in bool_tuples:
            break
    if cont == "y":
        break

print("YOUR LIST NUMBER IS: ", lst)

# +  Tìm và in ra tất cả các số nguyên tố có trong list.

lst_nguyen_to = []
for i in lst:
    nguyen_to = True
    if i < 1:
        continue
    if i == 1 or i == 2:
        lst_nguyen_to.append(i)
    else:
        for j in range(2,i):
            if i % j == 0:
                nguyen_to = False
                break
        if nguyen_to == True:
            lst_nguyen_to.append(i)

print("Prime list number is: ",lst_nguyen_to)
        
# +  Tính trung bình cộng của các phần tử âm/ phần tử dương trong list 
sum_plus = 0
count_plus = 0
sum_minus = 0
for i in lst:
    if i > 0:
        sum_plus += i
        count_plus += 1
    else:
        sum_minus += i

avg_positve = sum_plus/count_plus
avg_negative = sum_minus/(len(lst)-count_plus-lst.count(0))

print("Average positive number is: %.2f" %avg_positve)
print("Average negative number is: %.2f" %avg_negative)

# +  Tìm giá trị chẵn lớn nhất/ giá trị lẻ nhỏ nhất trong list 
lst_temp = lst[:]
max_odd = 0
max_even = 0
if max(lst_temp) % 2 == 0:
    max_odd = max(lst_temp)
    while max(lst_temp) % 2 == 0:
        lst_temp.remove(max(lst_temp))
    max_even = max(lst_temp)
else:
    max_even = max(lst_temp)
    while max(lst_temp) % 2 != 0:
        lst_temp.remove(max(lst_temp))
    max_odd = max(lst_temp)

print("Highest odd value is: ", max_odd)
print("Highest even value is: ", max_even)

# +  Sắp xếp list theo giá trị tăng dần 
lst.sort()
print("Sorted list: ", lst)


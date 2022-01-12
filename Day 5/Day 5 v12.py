# Viết chương trình:
#      - Tạo list1 có số lượng phần tử tùy ý, giá trị mỗi phần tử kiểu số
#      - Tạo list2 có số lượng phần tử tùy ý, giá trị mỗi phần tử kiểu số 
#      - In list1, list2 
#      - Tạo list3 từ list1 và list2 với những phần tử trong list3 được tạo thành từ những phần tử vừa có trong list1 vừa có trong list2 
#      - Tạo list4 từ list1 và list2 với những phần tử trong list4 được tạo thành từ những phần tử chỉ có trong list1 và chỉ có trong list2 
#      - Gợi ý:
#                +  list1 = [1, 2, 3, 4] 
#                +  list2 = [1, 2, 5] 
#                +  print(list(set(list1) - set(list2)) + list(set(list2) - set(list1)))

# Tạo list 1 và list 2 từ random function
from random import randrange
list1 = [randrange(0,10) for i in range(int(input("Nhập số phần tử List 1: ")))]
print("List 1 = ", list1)

list2 = [randrange(0,10) for i in range(int(input("Nhập số phần tử List 2: ")))]
print("List 2 = ", list2)

list3 = list(set(list1)&set(list2))
list4 = list(set(list1)^set(list2))
print("List 3 = ", list3)
print("List 4 = ", list4)

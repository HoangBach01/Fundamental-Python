# Viết chương trình thực hiện việc xử lý tuple như sau: 

# Yêu cầu 1:
# - Tạo 1 tuple có 10 phần tử chuỗi bất kỳ
# - Chương trình sẽ in tuple vừa tạo

lst = []
print("Import value to tuple")
for i in range(10):
    x = input(str("\t Item "+ str(i+1)+ ": "))
    lst.append(x)
tup = tuple(lst)
print(tup)


# Yêu cầu 2:
# - Nhập index dương (0 <= index < 10), index âm (-1 >= index >= -10)  
# - Chương trình sẽ in giá trị của phần tử trong tuple có index dương và index âm đã nhập
# index dương (0 <= index < 10)
while True:
    try:
        x_plus = int(input("Positive index (0 <= index < 10): "))
        if x_plus >= 0 and x_plus < 10:
            break
    except ValueError:
        print("Please enter a positive interger number")

print("\t Output["+ str(x_plus) + "]: ", tup[x_plus])

# index âm (-1 >= index >= -10)  

while True:
    try:
        x_minus = int(input("Negative index (-1 >= index >= -10): "))
        if x_minus >= -10 and x_minus <= -1:
            break
    except ValueError:
        print("Please enter a negative interger number")

print("\t Output["+ str(x_minus) + "]: ", tup[x_minus])


# Yêu cầu 3:
# - Nhập chuỗi cần tìm s_find 
# - Chương trình sẽ tìm và đếm số lần xuất hiện của s_find trong tuple 

s_find = input("String to search: ")
if s_find in tup:
    print("String search in tuple ", tup.count(s_find), "times.")
else:
    print("String search NOT in tuple")


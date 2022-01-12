# Viết chương trình xử lý list số theo các yêu cầu sau: 

# Yêu cầu 1:  
# - Tạo list số:  Cho phép người dùng lần lượt nhập các phần tử số cho list cho đến khi không muốn nhập nữa.
# - Chương trình sẽ :
# +  In ra list các số vừa nhập.
# +  Tính tổng các phần tử trong list.


lst =[]
bool_tuples = ("y","n",1,0,"yes","no")

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

s = sum(map(int, lst))
print("YOUR LIST IS:",lst)
print("Sum all variables in your list = ",s)

# Yêu cầu 2:
# - Người dùng nhập vào một số x cần tìm
# - Chương trình sẽ cho biết : 
# +  x có xuất hiện trong list hay không? Nếu có thì cho biết x xuất hiện bao nhiêu lần? 
# +  x có lớn hơn tất cả các số trong list không?  
# +  Nếu không thì x nhỏ hơn những số nào trong list? (In ra tất cả các số lớn hơn x) 

while True:
    try:
        x = (int(input("Please type your number wanna find:\n")))
        break
    except ValueError:
        print("Please enter number only!")

if x in lst:
    print(x, "is in your list, they show up " + str(lst.count(x))+ " times")
else:
    print(x, "is not in your list")

larger_x = []
if x > max(lst):
    print(x, "is larger than all number in list")
else:
    for i in lst:
        if i > x:
            larger_x.append(i)
    print("List have number larger than ", x, " from your list is: ", larger_x)

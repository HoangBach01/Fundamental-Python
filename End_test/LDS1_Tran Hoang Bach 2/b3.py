lst = []
n = -1
while True:
    x = str(input("Nhập giá trị: "))
    lst.append(x)
    while True:
        try:
            n = int(input("Tiếp tục nhập giá trị? 1: Có, 0: Không: "))
        except Exception:
            pass
        if n == 1 or n == 0:
            break
    if n == 0:
        break

print("List: ", lst)
print("Giá trị chiều dài từng phần tử: ")
ma = 0
for i in range(len(lst)):
    print("(",lst[i],":",len(lst[i]),")")
    if ma < len(lst[i]):
        ma = len(lst[i])

print("Các phần tử dài nhất: ")
for i in range(len(lst)):
    if len(lst[i]) == ma:
        print(i, ":", lst[i], ":", len(lst[i]))

string = str(input("Nhập giá trị cần tìm: "))
lst2 = []
for i in range(len(lst)):
    if lst[i] == string:
        lst2.append(i)
print("Các vị trí có giá trị giống", string, "là: ", sum(map(int,lst2)))
lst.sort()
print("List sau khi sắp xếp các vị trí: ", lst)

        





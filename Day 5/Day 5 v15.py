# Viết chương trình đếm số ký tự hoa và số ký tự thường trong chuỗi.
#      - Người dùng nhập vào một chuỗi (input) 
#      - Chương trình sẽ đếm và in ra số lượng ký tự hoa và số lượng ký tự thường có trong chuỗi (output)

string = str(input("Nhập chuỗi: "))
lower = ""
upper = ""
for i in string:
    if i.islower():
        lower += i
    elif i.isupper():
        upper += i
    else:
        pass

print("Số ký tự hoa trong chuỗi là: ",len(upper))
print("Chuỗi ký tự hoa là: ", upper)

print("Số ký tự thường trong chuỗi là: ",len(lower))
print("Chuỗi ký tự thường là: ", lower)

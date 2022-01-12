# Viết chương trình xử lý chuỗi theo yêu cầu sau:
# - Người dùng nhập vào một chuỗi từ bàn phím, phân tách nhau bởi dấu phẩy (input)
# - Chương trình sẽ xử lý và in chuỗi vừa nhập thành chuỗi theo thứ tự bảng chữ cái, phân tách nhau bằng dấu phẩy (output)

# Ví dụ:
# - Chuỗi ban đầu vào được nhập là: without,hello,bag,world
# - Chuỗi theo thứ tự bảng chữ cái là: bag,hello,without,world

s = str(input("Nhập chuỗi của bạn: ")).split(",")
lower = 0
temp = ""
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if ord(s[j][0]) < ord(s[i][0]):
            lower = j
            temp = s[lower]
            s[lower] = s[i]
            s[i] = temp
s_new = ""
for k in range(len(s)):
    if k == len(s)-1:
        s_new += str(s[k])
    else:
        s_new = s_new + str(s[k]) + ","
print("Chuỗi theo thứ tự bảng chữ cái là: ",s_new)

    
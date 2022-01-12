# Một website yêu cầu người dùng nhập tên người dùng và mật khẩu để đăng ký. Tuy nhiên để bảo mật, hệ thống yêu cầu cần phải kiểm tra xem mật khẩu người dùng nhập vào có đủ an toàn hay không. Các tiêu chí kiểm tra mật khẩu người dùng tạo bao gồm:
# 1. Ít nhất 1 chữ cái viết thường
# 2. Ít nhất có 1 ký số từ [0-9]
# 3. Ít nhất 1 kí tự viết HOA
# 4. Ít nhất có 1 ký tự đặc biệt trong các giá trị [$ # @]
# 5. Độ dài mật khẩu tối thiểu: 6
# 6. Độ dài mật khẩu tối đa: 12
# Chương trình như sau:
# - Người dùng sẽ nhập vào mật khẩu (Input)
# - Chương trình sẽ kiểm tra mật khẩu đó có đáp ứng những tiêu chí trên hay không?
# và in ra Mật khẩu bạn nhập là an toàn / không an toàn (Output)

# Ví dụ:
# + Input:  ABd1234@1
# + Output: Mật khẩu bạn nhập là an toàn

s = input("Mật khẩu của bạn là: ")
t1,t2,t3,t4 = 0,0,0,0

for char in s:
    if char.isalpha():
        if char.islower():
            t1 += 1
        if char.isupper():
            t3 += 1
    elif char.isdigit():
        t2 += 1
    elif char == "$" or char == "#" or char == "@":
        t4 += 1

ad1, ad2, ad3, ad4 = "","","",""
if t1 < 1:
    ad1 = "Ít nhất 1 chữ cái viết thường"
if t2 < 1:    
    ad2 = "Ít nhất có 1 ký số từ [0-9]"
if t3 < 1:    
    ad3 = "Ít nhất 1 kí tự viết HOA"
if t4 < 1:    
    ad4 = "Ít nhất có 1 ký tự đặc biệt trong các giá trị [$ # @]"

if len(s) < 6:
    print("Mật khẩu không phù hợp, Độ dài mật khẩu tối thiểu 6 ký tự.")
elif len(s) > 12:
    print("Mật khẩu không phù hợp, Độ dài mật khẩu tối đa 12 ký tự.")
elif t1 < 1 or t2 < 1 or t3 < 1 or t4 < 1:
    print("Mật khẩu bạn nhập là không an toàn. Mật khẩu cần có " + str(ad1)+ ", "+ str(ad2)+ ", "+ str(ad3)+ ", "+ str(ad4))
else:
    print("Mật khẩu bạn nhập là an toàn.")
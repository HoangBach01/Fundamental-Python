# Học viên viết chương trình xử lý chuỗi bằng cách sử dụng hàm thư viện Strings.

# - Người dùng nhập vào chuỗi s, chuỗi s_sub, chuỗi s_find, chuỗi s_replace.
# - Chương trình sẽ xử lý chuỗi và in ra các kết quả sau:
#              +  In chuỗi s 
#              +  Loại bỏ khoảng trắng ở đầu và cuối chuỗi 
#              +  In chuỗi với ký tự đầu chuỗi viết hoa 
#              +  Đếm và in ra số lần chuỗi con s_sub xuất hiện trong chuỗi s 
#              +  Tìm kiếm s_find trong s và thay thế bằng s_replace, in chuỗi sau khi tìm kiếm và thay thế.

s = str(input("Nhap chuoi s: "))
s_sub = str(input("Nhap chuoi s_sub: "))
s_find = str(input("Nhap chuoi s_find: "))
s_replace = str(input("Nhap chuoi s_replace: "))

print(s)
print(s.strip())
print(s.strip().capitalize())
print(s.count(s_sub))
print(s.replace(s_find, s_replace))
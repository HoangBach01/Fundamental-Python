# Viết chương trình đếm số ký tự văn bản và số ký tự là số (0-9) trong chuỗi.
# Yêu cầu:
# - Người dùng nhập vào một chuỗi bao gồm ký tự và số (Input)
# - Chương trình sẽ đếm số ký tự và số chữ số trong chuỗi, không tính khoảng trắng
# và in ra kết quả (Output)

# Ví dụ:
# - input:  Happy Teacher Day 20-11
# - output: 
#      + Số chữ cái là: 16
#      + Số chữ số là: 4
# Học viên có thể mở rộng thêm: đếm số chữ cái, số chữ số và số ký tự đặc biệt.

s = input("Nhap vao 1 chuoi: ")
count_num = 0
count_abc = 0
count_space = 0
for char in s:
    if char.isdigit():
        count_num += 1
    if char == " ":
        count_space += 1
count_abc = len(s) - count_num - count_space

print("So chu cai la: " + str(count_abc))
print("So chu so la: " + str(count_num))


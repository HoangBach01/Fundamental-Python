# Viết chương trình xử lý chuỗi với yêu cầu sau:
# - Người dùng nhập vào một chuỗi các từ tách biệt bởi khoảng trắng (input)
# - Chương trình xử lý chuỗi: loại bỏ các từ trùng lặp, sắp xếp theo thứ tự bảng chữ cái, 
# và in kết quả (output)

# Ví dụ:
# - input:  hello world and practice makes perfect and hello world again
# - output:  again and hello makes perfect practice world

'''
Created on October 10, 2019

@author: Trung Tâm Tin Học - Trường Đại học Khoa học Tự nhiên TP.HCM
'''

# Nhập vào một chuỗi các từ tách biệt bởi khoảng trắng
s = input("Nhập chuỗi của bạn: ")
words = [word for word in s.split(" ")]

# Loại bỏ các từ trùng lặp, sắp xếp theo thứ tự bảng chữ cái, và in kết quả

set_words = set(words)
lst_output = sorted(list(set_words))
output = " ".join(lst_output)
print("\t Output: ", output)
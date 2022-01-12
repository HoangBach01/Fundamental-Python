# Viết chương trình mở và đọc nội dung tập tin.
# - Người dùng nhập tên tập tin cần đọc.
# - Chương trình sẽ đọc và in ra nội dung của tập tin vừa nhập.
'''
Created on October 24, 2019

@author: Trung Tâm Tin Học - Trường Đại học Khoa học Tự nhiên TP.HCM
'''

# Xây dựng phương thức đọc nội dung tập tin
def read_file(filename):
    f = open(filename,"r+")
    content = f.read();
    f.close()
    return content

filename = input('Nhập tên tập tin:\n')
print('\nNội dung tập tin:')
print(read_file(filename))



# In kết quả
'''
Nhập tên tập tin:
Johny.txt

Nội dung tập tin:
Johny, Johny
Yes, Papa?
Eating sugar?
No, papa!
Telling lies?
No, papa!
Open your mouth
Ha, ha, ha!

'''
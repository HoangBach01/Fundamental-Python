# Viết chương trình ghi nội dung vào tập tin.
#      - Người dùng nhập tên tập tin và nội dung của tập tin
#      - Chương trình sẽ thực hiện:
#              + Nếu chưa tồn tại tập tin: tạo tập tin và ghi nội dung vào 
#              + Nếu đã tồn tại tập tin: xóa nội dung cũ, ghi nội dung mới 

# ---------------------------------
# Nội dung tập tin  <if.txt>
# If water were kisses, I'd send you the sea\n If leaves were hugs, I'd send you a tree\n If nite was love ,I'd send you the stars\n But I can't send u my heart cause that where you are.

'''
Created on October 24, 2019

@author: Trung Tâm Tin Học - Trường Đại học Khoa học Tự nhiên TP.HCM
'''

# Phương thức ghi nội dung vào tập tin
def write_file(filename, content):
    f = open(filename, 'w')
    for i in content:
        f.write(i)
        f.write("\n")
    f.close()
    return


# Phương thức đọc nội dung tập tin
def read_file(filename):
    f = open(filename, 'r')
    content = f.read()
    return content
    

filename = input('Nhập tên tập tin:\n')
content = input('\nNhập nội dung:\n').split("\\n")
print(content)
write_file(filename, content)
print('\nNội dung tập tin:\n',read_file(filename))
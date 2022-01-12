# Viết chương trình mở - đọc – thống kê nội dung tập tin.
# - Người dùng nhập tên tập tin.
# - Chương trình sẽ hiển thị nội dung tập tin, và thống kê số dòng, số từ, số ký tự trong tập tin.

'''
Created on October 24, 2019

@author: Trung Tâm Tin Học - Trường Đại học Khoa học Tự nhiên TP.HCM
'''

# Xây dựng phương thức đọc và thống kê nội dung tập tin
def read_report_file(filename):
    file_in = open(filename,'r')
    print('\nNội dung tập tin: ')
    count_lines = 0
    count_words = 0
    count_chars = 0
    string = file_in.readlines()
    print("".join(string))    
    # Học viên viết code để thống kê (số dòng, số từ, số ký tự)
    file_in.close()
    for i in string:
        count_lines += 1
        count_words += len(i.split())
        count_chars += len(i)
    print("\n----- Thống kê: Số dòng/ Số từ/ Số ký tự -----")
    print('Lines:', count_lines, ', Words:', count_words, ', Chars:', count_chars)


filename = input('Nhập tên tập tin:\n')
read_report_file(filename)



# In kết quả
'''
Nhập tên tập tin:
Hope.txt

Nội dung tập tin:
I hoped that he would love me,
And he has kissed my mouth,
But I am like a stricken bird
That cannot reach the south.
For though I know he loves me,
To-night my heart is sad;
His kiss was not so wonderful
As all the dreams I had.

----- Thống kê: Số dòng/ Số từ/ Số ký tự -----
Lines: 8 , Words: 49 , Chars: 232

'''
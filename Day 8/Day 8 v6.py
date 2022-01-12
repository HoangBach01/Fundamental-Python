# Viết chương trình ghi danh sách số điện thoại vào cuối file csv như sau: 
# - Người dùng nhập tên tập tin csv (ví dụ: danhba.csv), danh sách số điện thoại (Tên – Số điện thoại)
# - Chương trình sẽ ghi danh sách số điện thoại vào tập tin.
'''
Created on October 24, 2019

@author: Trung Tâm Tin Học - Trường Đại học Khoa học Tự nhiên TP.HCM
'''
import csv

# Học viên xây dựng phương thức ghi nội dung vào tập tin .csv
def write_csv_file(filename, listContent):  
    f = open(filename,"a+",encoding='utf-8',newline="")
    for item in listContent:
        csv.writer(f).writerow(item)
    f.close()

# Học viên xây dựng phương thức đọc nội dung tập tin .csv
def read_csv_file_column(filename):
    f = open(filename,"r",encoding='utf-8')    
    for row in csv.reader(f):
        print("{:<50} \t {:<50}".format(row[0],row[1]))
    f.close()

filename = input('Nhập tên tập tin .csv:\n')
listContent = [['Johnny Lee', '0913 753852'], ['Peter Son', '0989 753951'], ['Johnnathan','0903 123456']]
write_csv_file(filename, listContent)
print('\nNội dung tập tin sau khi ghi: ')
read_csv_file_column(filename)

# In kết quả
'''
Nhập tên tập tin .csv:
danhba.csv

Nội dung tập tin sau khi ghi:
Name     Fone
Sarah	0989 788951
Daisy	0973 329496
Owthen	0773 700951
Lee	    0383 900852
Johnny Lee       0913 753852
Peter Son        0989 753951
Johnnathan       0903 123456

'''
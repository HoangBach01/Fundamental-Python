'''
Created on October 10, 2019

@author: Trung Tâm Tin Học - Trường Đại học Khoa học Tự nhiên TP.HCM
'''

# Viết chương trình thực hiện việc xử lý danh bạ điện thoại như sau: 

#      - Tạo một danh bạ kiểu dictionary để lưu trữ danh bạ điện thoại với các cặp key-value (ví dụ như hình 7.8)
#      - Nhập tên cần tìm search_name 
#      - Nhập tên, số điện thoại 

#   => Chương trình sẽ thực hiện những công việc sau: 
#      - Tìm search_name trong danh bạ. Nếu không tìm thấy thì in thông tin tên – số điện thoại. Nếu không tìm thấy thì thông báo là không tìm thấy. 
#      - Thêm một liên hệ mới với thông tin:  tên – số điện thoại đã nhập 
#      - In danh bạ 

# Tạo một danh bạ kiểu dictionary để lưu trữ danh bạ điện thoại với các cặp key-value
danh_ba = {'Johnny': '0989741258', 'Katherine':'0903852147', 'Misu': '0913753951', 'Jack' : '0933753654'}

i = 1
while i == 1:    
    cv = int(input('Bạn muốn làm gì? 1: Xem danh bạ; 2: Tìm kiếm, 3: Thêm mới\t'))
    
    # In danh bạ điện thoại
    if cv == 1:
        print('Danh bạ điện thoại:')
        for name, number in danh_ba.items():
            print('Tên ',name ,'\t  Số điện thoại ',number)


    # Tìm search_name trong danh bạ.
    # Nếu không tìm thấy thì in thông tin tên – số điện thoại. Nếu không tìm thấy thì thông báo là không tìm thấy.   
    elif cv == 2:   
        name_search = input('Nhập tên cần tìm:\n')
        if danh_ba.get(name_search) == None:
            print("Không tìm thấy số điện thoại của",name_search,"trong danh bạ.")
        else:
            print('Tên ',name_search ,'\t  Số điện thoại ',danh_ba.get(name_search))


    # Thêm một liên hệ mới với thông tin:  tên – số điện thoại đã nhập
    elif cv == 3:
        ten = input('Nhập tên:\n')
        fone = input('Nhập số điện thoại:\n')
        danh_ba[ten] = fone
        print('Danh bạ điện thoại:')
        for name, number in danh_ba.items():
            print('Tên ',name ,'\t  Số điện thoại ',number)


    i = int(input('Tiếp tục lựa chọn? 1: Có; 0: Không\t'))
        
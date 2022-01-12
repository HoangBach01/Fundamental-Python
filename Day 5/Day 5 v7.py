'''
Created on October 10, 2019

@author: Trung Tâm Tin Học - Trường Đại học Khoa học Tự nhiên TP.HCM
'''
# Viết chương trình thực hiện việc xử lý từ điển Anh – Việt như sau:  

#      -  Tạo một từ điển (key: từ tiếng Anh, value: list nhiều nghĩa Tiếng Việt)
#         ví dụ:  check: tờ séc, hóa đơn, kiểm tra, chiếu cờ tướng

#    => Chương trình sẽ thực hiện những công việc sau: 
#      -  Hiển thị từ điển, cho biết trong từ điển hiện tại có bao nhiêu từ 
#      -  Thêm từ vào từ điển, và hiển thị từ điển sau khi thêm
#      -  Tìm kiếm từ tiếng Anh => nếu tìm thấy thì hiển thị key và value. Nếu không tìm thấy thì thông báo không tìm thấy 
#  -  Tìm kiếm từ tiếng Viet=> nếu tìm thấy thì hiển thị key và value. Nếu không tìm thấy thì thông báo không tìm thấy 
#      -  Xóa một từ trong từ điển, dựa trên key cung cấp ,  và hiển thị từ điển sau khi xóa

# Tạo một từ điển ((key: từ tiếng Anh, value: list nghĩa Tiếng Việt))
dictionary = {'work': ['công việc', 'việc làm', 'tác phẩm'], 'bark': ['vỏ cây', 'tiếng sủa', 'thuyền ba cột buồm'], 'bat':['con dơi', 'gậy', 'đánh bóng'], 'board': ['bảng', 'ban quản lý', 'lên tàu'], 'bowl' : ['cái bát', 'khán đài', 'quả bóng quần'], 'stamp' : ['con tem', 'phiếu mua hàng', 'con dấu'], 'club' : ['câu lạc bộ', 'gậy đánh golf', 'dùi cui']}

# Chương trình thực hiện các công việc:
i = 1
while i == 1:    
    cv = int(input('Bạn muốn làm gì? 1: Hiển thị từ điển; 2: Tra từ tiếng Anh; 3 Tra từ tiếng Việt; 4: Thêm từ, 5: Xóa từ\t'))

    # Hiển thị từ điển, và cho biết trong từ điển hiện tại có bao nhiêu từ?
    if cv == 1:
        print('Dictionary:')
        for word, definition in dictionary.items():
            print('Từ Tiếng Anh:',word,'\t Nghĩa Tiếng Việt:',definition)


    # Tìm kiếm từ tiếng Anh => nếu tìm thấy thì hiển thị key và value. Nếu không tìm thấy thì thông báo không tìm thấy
    elif cv == 2:    
        name_search = input('Nhập từ cần tra (Tiếng Anh):\t')
        if dictionary.get(name_search) == None:
            print("Không tìm thấy từ Tiếng Anh trong từ điển.")
        else:
            print('Từ Tiếng Anh:',name_search,'\t Nghĩa Tiếng Việt:',dictionary.get(name_search))
                
    # Tìm kiếm từ tiếng Viet=> nếu tìm thấy thì hiển thị key và value. Nếu không tìm thấy thì thông báo không tìm thấy 
    elif cv == 3:    
        name_search_vi = input('Nhập từ cần tra (Tiếng Việt):\t')
        word_eng = list(dictionary.keys())
        def_vi = list(dictionary.values())
        x = []
        for i in range(len(def_vi)):
            if name_search_vi in def_vi[i]:
                x.append(i)
        if x == []:
            print("Không tìm thấy dịch nghĩa sang tiếng anh của từ cần tìm.")
        else:
            for i in x:
                print('Nghĩa Tiếng Việt:',name_search_vi,'\t Từ Tiếng Anh:',word_eng[i])


    # Thêm từ vào từ điển, Hiển thị từ điển sau khi thêm 
    elif cv == 4:
        word = input('Nhập từ Anh:\t')
        meaning = list(input('Nhập nghĩa Việt:\t').split(','))
        dictionary[word] = meaning
        print('Dictionary:')
        for word, definition in dictionary.items():
            print('Từ Tiếng Anh:',word,'\t Nghĩa Tiếng Việt:',definition)


    # Xóa một từ trong từ điển, dựa trên key cung cấp , và Hiển thị từ điển sau khi xóa
    elif cv == 5:
        word_delete = input('Nhập từ cần xóa:\t')
        x = int(input('Bạn có thật sự muốn xóa hay không? 1: Xóa, 0: Không\t'))
        if x == 1:
            del dictionary[word_delete]
        else:
            pass
        print('Dictionary:')
        for word, definition in dictionary.items():
            print('Từ Tiếng Anh:',word,'\t Nghĩa Tiếng Việt:',definition)
             


    i = int(input('Tiếp tục lựa chọn? 1: Có; 0: Không\t'))
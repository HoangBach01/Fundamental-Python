# Yêu cầu: Hãy viết lại các bài 7.2, 7.4, 7.6 trong bài 7 bằng cách xây dựng phương thức/ hàm.

# Hướng dẫn:
#      - Bài 7.2:  
#               + Xây dựng phương thức tao_list(list_create): dùng để nhập các phần tử vào list. Kết quả trả về là list_original sau khi đã thêm các phần tử.
#               + Xây dựng phương thức tinh_tong_list(list_create): dùng để tính tổng các phần tử trong list. Kết quả trả về là tổng của list.
lst = [1,2,3,4,5,6,7,8,9]
s_lst = sum(map(int,lst))
print(lst)
print(s_lst)
#      - Bài 7.4:  
#               + Xây dựng phương thức dem_slxh(tuple_original, x): dùng để đếm số lần xuất hiện của x trong tuple. Kết quả trả về là số lần xuất hiện.

tup = (1,2,3,2,3,4,5,6,4,3,5)
dem = lambda tup,x: tup.count(x)
print(tup)
print(dem(tup,3))

#      - Bài 7.6: 
#               + Xây dựng phương thức in_dictionary(dictionary): dùng để in dictionary theo định dạng mỗi item (key : value) hiển thị trên một dòng.
#               + Xây dựng phương thức tim_kiem_dictionary(dictionary, key_search): dùng để tìm key_search trong từ điển. Kết quả trả về là chuỗi key : value nếu tìm thấy,  ‘Không tìm thấy <key_search>’ nếu không tìm thấy.
#               + Xây dựng phương thức them_dictionary(dictionary, key_insert, value_insert): dùng để thêm key : value mới vào dictionary. Kết quả trả về là dictionary sau khi đã thêm.

# Create a new dictionary
def make_dic(**a):
    return a

dic = make_dic(a=2, b=4, c=6, d=10)
print(dic)

# def in_dic(dic):
#     for key,value in dic.items():
#         print("("+str(key)+" : "+str(value)+")")
#     return
# in_dic(dic)

s = 




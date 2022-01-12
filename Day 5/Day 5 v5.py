# Viết chương trình thực hiện việc xử lý trên tuple như sau: 
# - Người dùng sẽ tạo:
#        +  1 tuple a chứa 4 số nguyên dương đầu tiên 
#        +  1 tuple b chứa 4 số nguyên dương tiếp theo
# - Chương trình sẽ:
#        +  Tạo 1 tuple c là sự kết hợp của các phần tử trong tuple a và b 
#        +  Tạo 1 tuple d từ tuple c với các phần tử được sắp xếp 
#        +  In phần tử thứ 3 của d 
#        +  In 3 phần tử cuối cùng của d 

# Tạo 1 tuple a chứa 4 số nguyên dương đầu tiên
tuple_a = (1, 8, 5, 4)
print('Tuple a:', tuple_a)

# Tạo 1 tuple b chứa 4 số nguyên dương tiếp theo
tuple_b = (3, 7, 6, 2)
print('Tuple b:', tuple_b)

# Tạo 1 tuple c là sự kết hợp của các phần tử trong tuple a và b
tuple_c = tuple_a + tuple_b
print('Tuple c:', tuple_c)

# Tạo 1 tuple d từ tuple c với các phần tử được sắp xếp
tuple_d = sorted(tuple_c)
print('Tuple d:', tuple_d)

# In phần tử thứ 3 của d
print('Tuple d, 3th value is', tuple_d[2])

# In 3 phần tử cuối cùng của d
print('Tuple d, 3 end value is', tuple_d[-3:])

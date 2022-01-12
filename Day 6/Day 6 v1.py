# Dựa vào quy tắc xử lý theo file đính kèm, học viên viết chương trình tính năm âm lịch từ năm dương lịch.
# - Khi người dùng nhập vào năm dương lịch (input) => Chương trình sẽ hiển thị năm âm lịch (output)

# Hướng dẫn:   
#              +  Viết phương thức tinh_can(nam) có kết quả trả về là chuỗi can, tinh_chi(nam) có kết quả trả về là chuỗi chi 
#               +  Sử dụng cấu trúc if...elif...else để giải quyết bài toán trên.

lst_can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
lst_chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]

def tinh_can(n):
    return lst_can[n%10]

def tinh_chi(n):
    return lst_chi[n%12]

n = int(input("Nhập năm dương lịch: "))
print("Năm âm lịch: ",tinh_can(n),tinh_chi(n))
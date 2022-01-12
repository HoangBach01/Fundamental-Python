# Viết chương trình ghi nội dung vào tập tin.
#      - Người dùng nhập tên tập tin và nội dung tập tin.
#      - Chương trình sẽ thực hiện:
#              + Nếu chưa tồn tại tập tin: tạo tập tin và ghi nội dung vào 
#              + Nếu đã tồn tại tập tin: ghi nội dung vào cuối tập tin tin, xuống dòng 
#              + Hỏi người dùng có muốn tiếp tục ghi nữa hay không? Người dùng chọn 1: có, chọn 0: không 
#                      * Nếu chọn 1: yêu cầu người dùng nhập nội dung => ghi nội dung vào cuối tập tin, xuống dòng 
#                      * Nếu chọn 0: kết thúc chương trình 

# -----------------------
# Nội dung bài thơ Qua Đèo Ngang (Bà Huyện Thanh Quan):
# Bước tới Đèo Ngang, bóng xế tà,
# Cỏ cây chen đá, lá chen hoa.
# Lom khom dưới núi, tiều vài chú
# Lác đác bên sông, chợ mấy nhà.
# Nhớ nước đau lòng, con quốc quốc,
# Thương nhà mỏi miệng, cái gia gia.
# Dừng chân đứng lại trời, non, nước,
# Một mảnh tình riêng, ta với ta.
# -----------------------

file_name = input("Nhập tên tập tin: ")
f = open(file_name,"a+")
while True:
    content = input("Nhập nội dung (enter để exit): ")
    if content == "":
        break
    else:
        f.write(content)
        f.write("\n")
# f.seek(0,0)
conten_total = f.read()
f.close()

print(conten_total)


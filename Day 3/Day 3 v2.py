# Học viên viết chương trình kiểm tra số nguyên tố với yêu cầu sau:
# - Người dùng nhập vào một số x (Input),
x = eval(input("Nhap so x cua ban: "))

# - Chương trình sẽ kiểm tra xem x có phải là số nguyên tố hay không?
for i in range(2,x):
    if x% i == 0:
        print("X khong la so nguyen to")
        break
else:
    print("X la so nguyen to")


# và in ra kết quả (Là số nguyên tố/ Không là số nguyên tố) (Output).

# Lưu ý: Số nguyên tố là số chỉ chia hết cho 1 và chính nó.


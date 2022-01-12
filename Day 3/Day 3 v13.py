# Viết chương trình in bảng cửu chương từ số đến số. 
#      - Chương trình cho phép người dùng nhập vào số bắt đầu đến số kết thúc. In ra bảng cửu chương của các số trong khoảng từ số bắt đầu đến số kết thúc theo định dạng như Hình 12.9
#      - Gợi ý: Sử dụng vòng lặp

b = 0
n = int(input("Từ số: "))
m = int(input("Đến số: "))

print("********************************")
print("")

for i in range(1,10):
    c = ""
    for j in range(n,m+1):
        b = str(i*j)
        c += str(j) + " x " + str(i) + " = " + b.rjust(2," ") + "       "
    print(c)

print("")
print("********************************")
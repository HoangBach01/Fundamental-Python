# Xây dựng chương trình tính và in ra kết quả của n! và n!!
#      - Chương trình cho phép nhập vào một số nguyên n, tính:  n!  ,   n!!   (Hình 12.8)
#      - Gợi ý : Sử dụng vòng lặp

n = int(input("Nhập số nguyên: "))

x = 1
y = 1

for i in range(1,n+1):
    x *= i
    if i % 2 == n % 2:
        y *= i

print("n! = " f'{x:,.0f}')
print("n! = " f'{y:,.0f}')

# Dãy Fibonacci là dãy vô hạn các số tự nhiên bắt đầu bằng hai phần tử 0 và 1, có quy luật khá đơn giản: “Phần tử đứng sau bằng tổng hai phần tử trước đó cộng lại”. 
# Dãy số Fibonacci có rất nhiều ứng dụng trong thực tế như : kiến trúc, nghệ thuật và phân tích  kỹ thuật dự đoán xu hướng thị trường...

# Trong bài tập này, Học viên sẽ lập trình xây dựng chương trình in ra n số đầu tiên trong dãy Fibonacci với yêu cầu sau:
# - Người dùng nhập vào giá trị n (Input)
# - Chương trình sẽ in ra dãy số Fibonacci đến n (Output)

# Ví dụ:
# Nhập n: 8
# Dãy Fibonacci là: 0, 1, 1, 2, 3, 5, 8, 13
n = 0
while n < 1: 
    n = eval(input("Nhap n: "))
a = 0
b = 1
s = [0,1]
for i in range(n-2):
        c = (a + b)
        s.append(c)
        a = b
        b = c
t = tuple(s)
print(t)


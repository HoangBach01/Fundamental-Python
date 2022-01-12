# Dãy Fibonacci là dãy vô hạn các số tự nhiên bắt đầu bằng hai phần tử 0 và 1, có quy luật khá đơn giản: “Phần tử đứng sau bằng tổng hai phần tử trước đó cộng lại”. 

# Trong bài tập này, Học viên viết lại bài tập Dãy Fibonacci bằng cách xây dựng hàm (Dùng kỹ thuật đệ quy)
# - Người dùng nhập vào giá trị n (Input)
# - Chương trình sẽ in ra dãy số Fibonacci đến n (Output)

# def fibonacci(n):
#     temp = 0
#     current = 1
#     lst_fibo = [0,1]
#     for i in range(2,n):
#         new = current + temp
#         lst_fibo.append(new)
#         temp = current
#         current = new
#     return print("Dãy Fibonaci", n, "số là: ", lst_fibo)

def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input("Nhập n: "))
lst = []
for i in range(1,n+1):
    lst.append(fibo(i))

print("Dãy Fibonacci", n, "số là: ", lst)
# fibonacci(n)


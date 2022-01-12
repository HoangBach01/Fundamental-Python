# Học viên xây dựng chương trình thực hiện việc đếm ngược (count down) với kết quả như hình minh họa.

# Chương trình cho phép người dùng nhập vào một số nguyên n (input) và chương trình sẽ hiển thị các giá trị đếm ngược từ n đến 1 (output).

# Lưu ý: Học viên có thể sử dụng file count_down.py đính kèm và thực hiện bài tập theo 2 cách (while và for).

n = eval(input("Nhap n: "))
i = n
for i in range(n):
    number = n - i
    print(number)
    i += 1
print("Start!")


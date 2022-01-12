# Viết chương trình xử lý chuỗi với yêu cầu sau:
# - Người dùng sẽ nhập vào một chuỗi gồm nhiều từ cách nhau bằng khoảng trắng (Input)
# - Chương trình sẽ xuất ra chuỗi mà trong đó mỗi từ sẽ được đảo ngược (Output).

# Ví dụ:
#      + Input:  Hello Python
#      + Output:  olleH nohtyP

sentence = input("Nhap vao 1 chuoi: ").split(" ")
i = 0
s = ""
while i < len(sentence):
    j = 0
    while j < len(sentence[i]):
        s += str(sentence[i][len(sentence[i])-1-j])
        j += 1
    i += 1
    s += " "

print(s)


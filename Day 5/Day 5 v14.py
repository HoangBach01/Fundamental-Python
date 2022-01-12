# Viết chương trình:      

# - Cho phép người dùng nhập vào số nguyên dương n. 
while True:
    try:
        n = int(input("Nhập số nguyên dương n: "))
        if n < 0:
            pass
        else:
            break
    except Exception:
        pass

# - Chương trình sẽ tạo một dictionary có n phần tử, với mỗi phần tử có key là các giá trị lần lượt từ 1 đến n và value = key * key 

dic = {key: key*key for key in range(1,n+1)}

print("Dictionary "+str(n)+" phần tử được tạo là:", dic)

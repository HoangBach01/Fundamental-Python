while True:
    try:
        n = int(input("Nhập n: "))
        break
    except Exception:
        pass

lst = str(n)
dic = {}
for i in lst:
    if i in dic.keys():
        y = dic[i] +1
        dic[i] = y
    else:
        dic[i] = 1

for key,value in dic.items():
    print("Số", key, "có", value, "số.")
    
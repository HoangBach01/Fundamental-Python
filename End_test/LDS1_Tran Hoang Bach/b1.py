lst_money = [500,200,100,50,20,10,5,2,1]
while True:
    try:
        x = int(input("Nhập số tiền X: "))
        if x > 0:
            break
    except Exception:
        print("Số tiền nhập không hợp lệ!")
        
def doi_tien(x):
    lst_doi = []
    remain = x
    for i in range(len(lst_money)):
        y = remain//lst_money[i]
        lst_doi.append(y)
        print("Loại", lst_money[i], "gồm", lst_doi[i], "tờ.")
        remain -= lst_money[i]*lst_doi[i]

print("Số tiền", x, "được đổi thành:")
doi_tien(x)
        

# Nhập vào một list có 5 phần tử. Xuất list vừa tạo. Ví dụ: 2, 7, 1, 4, 8. Sau đó: 
#      - Xác định xem có cặp số nào trong các số đó có quan hệ chia hết hay không? Nếu có thì in ra tất cả các cặp số đó. Ví dụ: cặp 2 & 1, 2 & 4, 2 & 8, 7 & 1, 1 & 4, 4 & 8, 1 & 8 
#      - Xác định xem có cặp số nào trong các số đó có quan hệ số này gấp 2 lần số kia hay không? Nếu có thì in ra tất cả các cặp số đó. Ví dụ: cặp 2 & 1, 2 & 4, 4 & 8 
#      - Xác định xem có cặp số nào trong các số đó mà tổng hai số bằng 8 hay không? Nếu có thì in ra tất cả các cặp số đó. Ví dụ: cặp 7 & 1 
#      - Gợi ý: Duyệt list

# Nhập vào một list có 5 phần tử. Xuất list vừa tạo. Ví dụ: 2, 7, 1, 4, 8. Sau đó: 
from random import randrange

lst = []
for i in range(5):
    lst.append(randrange(1,10))
print("List: ", lst)
print("")
lst_set = list(set(lst))

#      - Xác định xem có cặp số nào trong các số đó có quan hệ chia hết hay không? Nếu có thì in ra tất cả các cặp số đó. Ví dụ: cặp 2 & 1, 2 & 4, 2 & 8, 7 & 1, 1 & 4, 4 & 8, 1 & 8 
lst1 = []
for i in range(len(lst_set)):
    for j in range(i+1, len(lst_set)):
        if lst_set[i] % lst_set[j] == 0 or lst_set[j] % lst_set[i] == 0:
            lst1.append([lst_set[i],lst_set[j]])
if lst1 == []:
    print("Không có cặp số nào có quan hệ chia hết.")
else:
    print("Các cặp số có quan hệ chia hết:")
    for i in lst1:
        print(i[0], "&", i[1])

#      - Xác định xem có cặp số nào trong các số đó có quan hệ số này gấp 2 lần số kia hay không? Nếu có thì in ra tất cả các cặp số đó. Ví dụ: cặp 2 & 1, 2 & 4, 4 & 8 
lst2 = []
for i in range(len(lst_set)):
    for j in range(i+1, len(lst_set)):
        if lst_set[i]/lst_set[j] == 2 or lst_set[j]/lst_set[i] == 2:
            lst2.append([lst_set[i],lst_set[j]])
if lst2 == []:
    print("Khống có cặp số nào có quan hệ gấp 2 lần.")
else:
    print("Các cặp số có quan hệ gấp 2 lần:")
    for i in lst2:
        print(i[0], "&", i[1])
    
#      - Xác định xem có cặp số nào trong các số đó mà tổng hai số bằng 8 hay không? Nếu có thì in ra tất cả các cặp số đó. Ví dụ: cặp 7 & 1 
lst3 = []
for i in range(len(lst_set)):
    for j in range(i+1, len(lst_set)):
        if lst_set[i] + lst_set[j] == 8:
            lst3.append([lst_set[i],lst_set[j]])
if lst3 == []:
    print("Khống có cặp số nào có tổng bằng 8.")
else:
    print("Các cặp số có tổng bằng 8:")
    for i in lst3:
        print(i[0], "&", i[1])
    
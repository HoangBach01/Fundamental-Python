# Viết chương trình kiểm tra xem có những vị trí nào có giá trị giống nhau trong hai list số, và in ra kết quả.

lst1 = [1,4,6,3,5,6,7,4,5,4]
lst2 = [3,6,4,3,2,5,6,9,4,8]

print("List 1: ", lst1)
print("List 2: ", lst2)

def check(lst1, lst2):
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                print("Vị trí", i+1, "trong List 1 giống vị trí", j+1, "trong List 2.")
    return

check(lst1, lst2)
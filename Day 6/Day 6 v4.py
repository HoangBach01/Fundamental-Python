# Viết chương trình thực hiện xóa số chẵn xuất hiện đầu tiên của list số, và in ra kết quả cuối cùng của list số.

lst = [1,3,5,4,3,5,7,4,5,64,3,2]
print("Current list: \t", lst)
def xoa(lst):
    for i in lst:
        if i % 2 == 0:
            lst.remove(i)
            break
    return print("New list: \t", lst)

xoa(lst)
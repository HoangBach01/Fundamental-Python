# Viết chương trình tính lũy thừa của hai list số và in ra kết quả.

# Lưu ý:  Để tính lũy thừa của một số, chúng ta sử dụng toán tử "**" .

def exponent(lst):
    lst_new = []
    for i in lst:
        lst_new.append(int(i)**2)
    return lst_new

lst1 = list(map(int,input("Nhập input: ").split(",")))
print("Input: ", lst1)
print("Output: ", exponent(lst1))
print("Output: ", list(map(lambda x: x**2,lst1)))


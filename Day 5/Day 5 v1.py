# Viết chương trình tìm thú trong vườn thú với yêu cầu sau:
#     - Tạo ra một list có các con thú. 
#     - Nhập vào một con thú cần tìm 
#    => Chương trình in ra danh sách các con thú, số lượng các con thú và kết quả tìm kiếm con thú (Con thú cần tìm có/không có trong list).

list_animals = ['ant', 'bear', 'cat', 'dog', 'elephant', 'fish', 'goat', 'hippo']

print("Danh sách các con thú là:", list_animals)

print("Số lượng các con thú trong list là:",len(list_animals))

x = input("Which animal you want to find:\n")
if x in list_animals:
    print(x + " có trong danh sách")
else:
    print(x + " không có trong danh sách")



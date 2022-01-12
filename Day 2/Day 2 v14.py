# Tinh tien phong o Resort

# Nhap loai phong (1...8)
list_room = [1,2,3,4,5,6,7,8]
name = ['Standard', 'Superior Garden View', 'Superior Ocean View', 'Garden View Bungalow', 'Pool View Bungalow', 'Family Room', 'Beach Front Bungalow', 'VIP Sea View']
print("Ban muon o loai phong nao?") 
room = eval(input("Cac loai phong sap xep tu 1 (Standard) - 8 (VIP): "))
while room not in list_room:
    print("Loai phong khong hop le.")
    room = eval(input("Cac loai phong sap xep tu 1 (Standard) - 8 (VIP): "))
print("Phong ban chon la: %s ?" %name[room-1])
confirm = input("Press y if you confirmed!: ")
if confirm == 'y':
    print("Thank you!")
else:
    print("Thank you!, you can comeback by run program again!")
    exit()
# Nhap so dem o tai resort
night = eval(input("Ban muon o bao nhieu dem? "))
while night < 0 or type(night) is not int:
    print("So dem khon hop le.")
    night = eval(input("Ban muon o bao nhieu dem? "))

# Bang gia phong/dem
p = [1260000, 1550000, 1830000, 1830000, 2120000, 2120000, 2540000, 4800000]

#  Chiet khau
if night >= 2 and night <= 3:
    d = 1 - 0.25
elif night >=4:
    d = 1 - 0.3
else:
    d = 1

# Tinh tien phong
price = p[room-1] * night * d
print("Tong tien phong (sau khi chiet khau) cua ban la: %i" %price)
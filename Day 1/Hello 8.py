interest_rate = eval(input("Lai suat 1 nam hien tai la: "))
amount = eval(input("So tien gui cua ban la: "))
months = eval(input("Ban gui trong bao nhieu thang: "))
interest = amount * months * interest_rate / 12 / 100
print("Tien lai cua ban la: %.2f" % (interest))
print("Tong so tien ca goc lan lai cua ban la: %.2f" % (amount + interest))

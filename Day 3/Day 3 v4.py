# Viết chương trình tính và in ra kết quả của các biểu thức với kết quả như hình minh họa.
# - Người dùng nhập vào một số nguyên n (Input) 
# - Chương trình sẽ tính các biểu thức sau đây: 
#               A = tổng các số lẻ nhỏ hơn hay bằng n 
#               B = tổng các số chẵn nhỏ hơn hay bằng n 
#               C = tích các số từ 1 đến n 
#               D = tích các số chia hết cho 3 nhỏ hơn hay bằng n 
#               E = tổng các số nguyên tố nhỏ hơn hay bằng n 
# và in ra các kết quả của A, B, C, D, E.

n = int(input("Nhap n: "))
A,B,C,D,E = 0,0,1,1,0
a,b,c,d,e = "","","","",""
dem1, dem2, dem3, dem4, dem5 = 0,0,0,0,0
for i in range(1,n+1):
    if i % 2 == 1:
        A += i
        dem1 += 1
        if dem1 == 1:
            a = "Tổng các số lẻ nhỏ hơn hay bằng "+ str(n) + " là: A = " + str(i)
        else:    
            a += " + "+ str(i)

for i in range(1,n+1):
    if i % 2 == 0:
        B += i
        dem2 += 1
        if dem2 == 1:
            b = "Tổng các số chẵn nhỏ hơn hay bằng "+ str(n) + " là: B = " + str(i)
        else:    
            b += " + "+ str(i)



for i in range(1,n+1):
    C *= i
    dem3 += 1
    if dem3 == 1:
        c = "Tích các số từ 1 đến "+ str(n) + " là C = " + str(i)
    else:    
        c += " x "+ str(i)

for i in range(1,n+1):
    if i % 3 == 0:
        D *= i
        dem4 += 1
        if dem4 == 1:
            d = "Tích các số chia hết cho 3 nhỏ hơn hay bằng " + str(n) + " là: D = " + str(i)
        else: 
            d += " x "+ str(i)

for i in range(2,n):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        E += i
        dem5 += 1
        if dem5 == 1:
            e = "Tổng các số nguyên tố nhỏ hơn hay bằng "+ str(n) + " la: E = " + str(i)
        else:
            e += " + " + str(i) 

print("********************************")
print("")
print(a, "=", f'{A:,.0f}')
print(b, "=", f'{B:,.0f}')
print(c, "=", f'{C:,.0f}')
print(d, "=", f'{D:,.0f}')
print(e, "=", f'{E:,.0f}')
print("********************************")
print("")
print(A,B,C,D,E)

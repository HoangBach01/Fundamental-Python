n = int(input("Nhập n là chiều cao của Tam giác: "))

s = ""
for i in range(n):
    space =" "
    if i == 0:
        s += "*"
        space *= (n-1)
        print(space,s)
    else:
        s += "**"
        space *= (n-1)
        print(space,s)

m = int(input("Nhập m là chiều cao của Tam giác cân: "))


spac2 = " "
for j in range(m):
    s1 = "*"
    spac = " "
    if j == 0:
        spac *= (m-1)
        print(spac,s)
    if j == 1:
        space *= (m-j-1)
        print(spac,s,spac2,s)
    if j == m-1:
        s *= m
        space *= (m-j-1)
        print(spac,s)
    else:
        spac2 += "  "
        print(spac,s,spac2,s)
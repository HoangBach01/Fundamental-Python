s1 = input("Nhap cau s1: ")
s2 = input("Nhap cau s2: ")
s3 = input("Nhap cau s3: ")
print("Chieu dai cua chuoi s1 la: %s" % len(s1))
print("Chieu dai cua chuoi s2 la: %s" % len(s2))
print("Chieu dai cua chuoi s3 la: %s" % len(s3))
index = eval(input("Nhap vi tri ma ban can lay tu s1 (< %i): " % len(s1)))
while index > len(s1):
    index = eval(input("Nhap vi tri ma ban can lay tu s1 (< %i): " % len(s1)))
s4 = s1[index:]
print("Chuoi s4 la: %s" % s4)
print("Hai lan chuoi s2 la: %s" % (s2*2))

# Viết chương trình đếm và in ra số lần xuất hiện của ký tự x trong từ.

# Ví dụ: 
# + Input: mississippi
# + Output:  s  -> 4

def check_string(s,string):
    return string.count(s)

string = str(input("Input: "))
s = str(input("Character to check: "))
print("Output: ", s, "-> ", string.count(s))
# Viết chương trình kiểm tra hai list số có phải là list đảo ngược hay không? và in ra kết quả.
lst1 = [1,2,3,4,5]
lst2 = [5,4,3,2,1]

print("List 1: ", lst1)
print("List 2: ", lst2)

def check(lst1,lst2):
    cont = True
    for i in range(len(lst1)):
        if cont == True:
            if lst1[i] != lst2[len(lst2)-1-i]:
                cont = False
                break
        else:
            break
    return cont

print("Result, Reserve or not? ", check(lst1,lst2))
    
        


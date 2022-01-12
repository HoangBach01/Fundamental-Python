# Viết chương trình với yêu cầu sau:
import random
from random import randrange
from collections import Counter

#      - Tạo 3 dictionary: dic1, dic2, dic3 có số lượng phần tử và giá trị key:value là giá trị số tùy ý
names = list("Bach Man Hai Tuan Dat Duc Trung Dung".split())
dic1 = {}
for i in range(int(input("Dict 1: "))):
    dic1[random.choice(names)] = randrange(1,10)
print(dic1)

dic2 = {}
for i in range(int(input("Dict 2: "))):
    dic2[random.choice(names)] = randrange(1,10)
print(dic2)

dic3 = {}
for i in range(int(input("Dict 3: "))):
    dic3[random.choice(names)] = randrange(1,10)
print(dic3)

#      - Hãy viết chương trình tạo một dictionary mới dic4 với các phần tử được lấy từ 3 dictionary trên.
dic4 = Counter()
dic_merge = [dic1,dic2,dic3]
for i in dic_merge:
    dic4.update(i)
print("Dict 4 là: ", dict(dic4))

#      - Tìm phần tử có value lớn nhất/ nhỏ nhất trong dictionary
print("Phần tử có value lớn nhất là: ", dic4.most_common(1)[0])
print("Phần tử có value nhỏ nhất là: ", dic4.most_common()[-1])
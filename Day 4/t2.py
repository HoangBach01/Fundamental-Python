d={}
for i in range(int(input())):
    s=input().split(';')
    try:
        d[s[0]]+=[s[1]]
    except:
        d[s[0]]=[s[1]]
for i in range(int(input())):
    s=input().split(';')
    try:
        d[s[0]]+=[s[1]]
    except:
        d[s[0]]=[s[1]]
for s in d.keys():
    print(s+': '+' and '.join(map(str, d[s])))
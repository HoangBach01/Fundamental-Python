import string

text = str(input("Encrypted text: "))
key = str(input("Key: "))

# Check key valid or not
if len(key.split()) > 1 | len(key) != 26:
    print("Invalid key!")
    exit(1)
else:
    for i in range(len(key)):
        if key[i] in key[0:i]:
            print("Invalid key!")
            exit(1)
        elif key[i].isalpha():
            pass
        else:
            print("Invalid key!")
            exit(1)            

# Mapping with alphabet
alphabet = string.ascii_uppercase
decrypt = []
for i in range(len(text)):
    if text[i].isalpha():
        if text[i].islower():
            decrypt.append(alphabet[key.index(text[i].upper())].lower())
        else:
            decrypt.append(alphabet[key.index(text[i].upper())].upper())
    else:
        decrypt.append(text[i])

print("Plain text: " + "".join(decrypt))
    
    
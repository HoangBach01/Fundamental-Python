import string
import random

text = str(input("Plain text: "))

# Create random key
lst_letters = list(string.ascii_uppercase)
random.shuffle(lst_letters)
key = ''.join(lst_letters)
print("Key: ", key)

# Mapping with alphabet
alphabet = string.ascii_uppercase
encrypt = []
for i in range(len(text)):
    if text[i].isalpha():
        if text[i].islower():
            encrypt.append(key[alphabet.index(text[i].upper())].lower())
        else:
            encrypt.append(key[alphabet.index(text[i].upper())].upper())
    else:
        encrypt.append(text[i])

print("Encrypt text: " + "".join(encrypt))
    




    
    
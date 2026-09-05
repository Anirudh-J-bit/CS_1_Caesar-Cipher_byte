s=input()
listofinputs=s.split()
plaintext=listofinputs[0]
shiftvalue=int(listofinputs[1])
#Encryption
ciphertext=""
for i in plaintext:
    #Uppercase
    if i.isupper():
        ordinal=ord(i)
        if not i.isalpha():
            ciphertext=ciphertext+i
            continue
        else:
            cipherordinal=ordinal+shiftvalue
            if cipherordinal>90:
                cipherordinal-=26
            cipherchar=chr(cipherordinal)
            ciphertext=ciphertext+cipherchar
    #Lowercase
    else:
        ordinal = ord(i)
        if not i.isalpha():
            ciphertext = ciphertext + i
            continue
        else:
            cipherordinal = ordinal + shiftvalue
            if cipherordinal > 122:
                cipherordinal -= 26
            cipherchar = chr(cipherordinal)
            ciphertext = ciphertext + cipherchar

print("Encrypted: ",ciphertext)
#Decryption
decrypted=""
for i in ciphertext:
    #Uppercase
    if i.isupper():
        ord2 = ord(i)
        if not i.isalpha():
            decrypted=decrypted+i
            continue
        else:
            decryptedord=ord2-shiftvalue
            if decryptedord<65:
                decryptedord+=26
            decryptedchar=chr(decryptedord)
            decrypted=decrypted+decryptedchar
    #Lowercase
    else:
        ord2 = ord(i)
        if not i.isalpha():
            decrypted = decrypted + i
            continue
        else:
            decryptedord = ord2 - shiftvalue
            if decryptedord < 97:
                decryptedord += 26
            decryptedchar = chr(decryptedord)
            decrypted = decrypted + decryptedchar
print("Decrypted: ",decrypted)
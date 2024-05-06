def ordify(string):
    num = ""
    for ch in string:
        num+=str((ord(ch)))

    return int(num)


def encrypt(plain, key):
    cipher = ''
    for ch in plain:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
    
            try:
                cipher_ch = chr((ord(ch) - base + key) % 26 + base) 
            except TypeError:
                cipher_ch = chr((ord(ch) - base + ordify(key)) % 26 + base)

            cipher+=cipher_ch

        else:
            cipher+=ch

    return cipher

def decrypt(cipher, key):
    plain = ""
    for ch in cipher:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
    
            try:
                plain_ch = chr((ord(ch) - base - key) % 26 + base) 
            except TypeError:
                plain_ch = chr((ord(ch) - base - ordify(key)) % 26 + base)

            plain+=plain_ch

        else:
            plain+=ch

    return plain


        
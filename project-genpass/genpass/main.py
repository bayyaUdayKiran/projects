import Caesar
import pyperclip
import sys
import requests
import random

if __name__ == "__main__":
    flag = sys.argv[1]
    if flag == "-e":
        pt = sys.argv[2]
        k = random.randint(1000000, 9999999)

        try:
            with open(".cipher.txt", 'w') as log:
                cipher_text = Caesar.encrypt(pt, k)
                log.write(cipher_text)
                pyperclip.copy(cipher_text)
        
        except :
            pass

        new_data = {'key': k, 'plain': pt, 'cipher': cipher_text}
        response = requests.post('http://192.168.29.223:5000/write_data', json=new_data)
        print(response.json())
        print("* Encryption successful...\n* Check the log file(.cipher.txt) and your clipboard for cipher text.")

    elif flag == '-d':
        ct, auth = sys.argv[2], sys.argv[3]
        with open(".cipher.txt", 'w') as log:
            response = requests.get('http://192.168.29.223:5000/get_data')
            data = response.json()
            k = None
            for node in data:
                if node['id'] == int(auth):
                    k = node['key']
            cipher_text = Caesar.decrypt(ct, k)
            log.write(cipher_text)
            pyperclip.copy(cipher_text)
        print("* Decryption successful...\n* Check the log file(.cipher.txt) and your clipboard for plain text.")
        del_data = {'index': int(auth) - 1}
        response = requests.post('http://192.168.29.223:5000/del_data', json=del_data)
        print(response.json())



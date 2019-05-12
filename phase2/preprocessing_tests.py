import sys, os, string
from preprocessing import AESCipher, encrypt_and_save

def check_file_equals(message_path, cipher_path, key_path):
    with open(message_path, 'r') as f:
        message = f.read()
    
    with open(cipher_path, 'rb') as f:
        cipher = f.read()
    
    with open(key_path, 'rb') as f:
        key = f.readlines()

    scheme = AESCipher(key[0])
    decr = scheme.decrypt(cipher)

    return decr == message


def test1():
    scheme = AESCipher()
    
    message_path = "C:/Projects/WebAssDecoders/phase2/code"

    folder_name = os.path.dirname(message_path)
    file_name, ext = os.path.splitext(os.path.basename(message_path))
    cipher_path = os.path.join(folder_name, file_name + "_enc" + ext)
    key_path = os.path.join(folder_name, "key")

    encrypt_and_save(scheme, message_path, cipher_path, key_path)

    assert check_file_equals(message_path, cipher_path, key_path), "files not equal"



if __name__ == "__main__":
    test1()
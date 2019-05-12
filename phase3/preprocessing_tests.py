import sys, os, string
from preprocessing import SubsetituionCipher, encrypt_and_save

def check_file_equals(message_path, cipher_path, key_path):
    with open(message_path, 'r') as f:
        message = f.read()
    
    with open(cipher_path, 'r') as f:
        cipher = f.read()
    
    with open(key_path, 'r') as f:
        key = f.readlines()

    scheme = SubsetituionCipher(alphabet=key[0].split("Alph:")[1], key=key[1].split("Key:")[1])
    decr = scheme.decrypt(cipher)

    return decr == message


def test1():
    scheme = SubsetituionCipher(string.ascii_letters + string.punctuation + " ")
    
    message_path = "C:/Users/arzulti/Project/WebAssDecoders/phase3/code"

    folder_name = os.path.dirname(message_path)
    file_name, ext = os.path.splitext(os.path.basename(message_path))
    cipher_path = os.path.join(folder_name, file_name + "_enc" + ext)
    key_path = os.path.join(folder_name, "key")

    encrypt_and_save(scheme, message_path, cipher_path, key_path)

    assert check_file_equals(message_path, cipher_path, key_path), "The files aren't equals"



if __name__ == "__main__":
    test1()
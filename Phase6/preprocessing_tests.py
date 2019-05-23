import os, string
from preprocessing import preprocessing


def check_file_equals(message_path, cipher_path):
    with open(message_path, 'r') as f:
        message = f.read()
    
    with open(cipher_path, 'r') as f:
        text = f.readlines()

    cipher = text[2].strip().split(", ")

    decr = "".join([chr(int(c)) for c in cipher])

    return decr == message


def test1():
    message_path = "C:/Users/arzulti/Project/WebAssDecoders/phase4/code/code.txt"

    folder_name = os.path.dirname(message_path)
    file_name, ext = os.path.splitext(os.path.basename(message_path))
    cipher_path = os.path.join(folder_name, file_name + "_enc" + ext)

    preprocessing(message_path, cipher_path)

    assert check_file_equals(message_path, cipher_path), "The files aren't equals"


if __name__ == "__main__":
    test1()

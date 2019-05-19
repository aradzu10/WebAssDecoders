import os, string
from preprocessing import SubsetituionCipher, encrypt_and_save


def check_file_equals(message_path, cipher_path):
    with open(message_path, 'r') as f:
        message = f.read()
    
    with open(cipher_path, 'r') as f:
        text = f.readlines()

    cipher = text[0].split("string input(\"")[1].split("\")")[0].replace("\\\"", "\"").replace("\\\\", "\\")
    org_alph = text[1].split("string org_alph(\"")[1].split("\")")[0].replace("\\\"", "\"").replace("\\\\", "\\")
    key_alph = text[2].split("string key_alph(\"")[1].split("\")")[0].replace("\\\"", "\"").replace("\\\\", "\\")

    scheme = SubsetituionCipher(alphabet=org_alph, key=key_alph)
    decr = scheme.decrypt(cipher)

    return decr == message


def test1():
    scheme = SubsetituionCipher(string.ascii_letters + string.punctuation + " ")
    
    message_path = "C:/Users/arzulti/Project/WebAssDecoders/phase3/code/code.txt"

    folder_name = os.path.dirname(message_path)
    file_name, ext = os.path.splitext(os.path.basename(message_path))
    cipher_path = os.path.join(folder_name, file_name + "_enc" + ext)

    encrypt_and_save(scheme, message_path, cipher_path)

    assert check_file_equals(message_path, cipher_path), "The files aren't equals"


if __name__ == "__main__":
    test1()

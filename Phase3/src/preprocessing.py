import os
import random
import string


def encode_to_c(line):
    return line.replace("\\", "\\\\").replace("\"", "\\\"")


class SubstitutionCipher:

    def __init__(self, alphabet, key=None):
        self.alphabet = alphabet
        self.key = key if key is not None else self.__generate_key(alphabet)

    def __generate_key(self, alphabet):
        alphabet = list(alphabet)
        random.shuffle(alphabet)
        return ''.join(alphabet)

    def encrypt(self, plaintext):
        key_map = dict(zip(self.alphabet, self.key))
        return ''.join(key_map[c] for c in plaintext)

    def decrypt(self, cipher):
        key_map = dict(zip(self.key, self.alphabet))
        return ''.join(key_map[c] for c in cipher)

    def write_to_code(self, code_enc):
        line = "string input(\"%s\");\nstring org_alph(\"%s\");\nstring key_alph(\"%s\");" \
               % (encode_to_c(code_enc),
                  encode_to_c(self.alphabet),
                  encode_to_c(self.key))
        return line


def encrypt_and_save(scheme, message_path, cipher_path):
    with open(message_path, 'r') as f:
        message = f.read()
    
    with open(cipher_path, 'w') as f:
        f.write(scheme.write_to_code(scheme.encrypt(message)))


def main():
    message_path = "../code/code.txt"

    folder_name = os.path.dirname(message_path)
    file_name, ext = os.path.splitext(os.path.basename(message_path))
    cipher_path = os.path.join(folder_name, file_name + "_enc" + ext)
    
    scheme = SubstitutionCipher(
        ''.join(random.shuffle(string.ascii_letters + string.punctuation + " " + string.digits))
    )

    encrypt_and_save(scheme, message_path, cipher_path)


if __name__ == "__main__":
    main()        

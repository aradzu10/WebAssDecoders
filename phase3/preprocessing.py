import sys, os, random, string

class SubsetituionCipher:

    def __init__(self, alphabet):
        self.alphabet = alphabet
        self.key = self.__generate_key(alphabet)

    def __generate_key(self, alphabet):
        alphabet = list(alphabet)
        random.shuffle(alphabet)
        return ''.join(alphabet)

    def encrypt(self, plaintext):
        key_map = dict(zip(self.alphabet, self.key))
        return ''.join(key_map.get(c.lower(), c) for c in plaintext)

    def decrypt(self, cipher):
        key_map = dict(zip(self.key, self.alphabet))
        return ''.join(key_map.get(c.lower(), c) for c in cipher)

    def write_key(self):
        return "Alph: " + self.alphabet + "\n" + \
                "Key: " + self.key + "\n"


def encrypt_and_save(scheme, message_path, cipher_path, key_path):
    with open(message_path, 'r') as f:
        message = "".join(f.readlines())
    
    with open(cipher_path, 'w') as f:
        f.write(scheme.encrypt(message))
    
    with open(key_path, 'w') as f:
        f.write(scheme.write_key())


def main():
    if len(sys.argv) != 2:
        return

    message_path = sys.argv[-1]

    folder_name = os.path.dirname(message_path)
    file_name, ext = os.path.splitext(os.path.basename(message_path))
    cipher_path = os.path.join(folder_name, file_name + "_enc" + ext)
    key_path = os.path.join(folder_name, "key")
    
    scheme = SubsetituionCipher(string.printable)

    encrypt_and_save(scheme, message_path, cipher_path, key_path)

if __name__ == "__main__":
    main()        
    
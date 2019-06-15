import random, string


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
        line = "    string input(\"%s\");\n    string org_alph(\"%s\");\n    string key_alph(\"%s\");" \
               % (encode_to_c(code_enc),
                  encode_to_c(self.alphabet),
                  encode_to_c(self.key))
        return line


def add_includes(code):
    code = code + "#include <emscripten.h>\n"
    code = code + "#include <string>\n"
    code = code + "#include <iostream>\n"
    code = code + "#include \"substitution_cipher.h\"\n"
    code = code + "using namespace std;\n"
    code = code + "\n"
    return code


def add_js(code):
    code = code + "EM_JS(void, run_code, (const char* str), {\n"
    code = code + "    new Function(UTF8ToString(str))();\n"
    code = code + "});\n"
    code = code + "\n"
    return code


def add_main(code, enc):
    code = code + "int main() {\n"
    code = code + enc + "\n"
    code = code + "    string code(\"\");\n"
    code = code + "    SubstitutionCipher::decrypt(input, org_alph, key_alph, code);\n"
    code = code + "    run_code(code.c_str());\n}"
    code = code + "\n"
    return code


def encrypt_and_save(scheme, message_path):
    with open(message_path, 'r') as f:
        message = f.read().replace("\n", "")
    
    return scheme.write_to_code(scheme.encrypt(message))


def create_main(main_path):
    message_path = r"..\code\code.txt"
    letters = list(string.ascii_letters + string.punctuation + " " + string.digits)
    random.shuffle(letters)
    scheme = SubstitutionCipher(''.join(letters))
    enc = encrypt_and_save(scheme, message_path)

    code = ""
    code = add_includes(code)
    code = add_js(code)
    code = add_main(code, enc)
    with open(main_path, 'w') as f:
        f.write(code)


def main():
    message_path = r"..\src\main.cpp"
    create_main(message_path)


if __name__ == "__main__":
    main()        

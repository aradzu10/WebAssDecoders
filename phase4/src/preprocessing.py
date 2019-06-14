from Crypto import Random
import Crypto.Cipher.AES as AES


def pad_code(code_bytes, round_to):
    pad = bytes([0] * ((round_to - len(code_bytes)) % round_to))
    return code_bytes + pad


def encode_to_c_array(code_bytes):
    return ", ".join("0x{:02x}".format(c) for c in code_bytes)


def generate_encryption(code_path):
    with open(code_path, "rb") as f:
        code_bytes = f.read()

    iv = bytes(Random.get_random_bytes(16))
    key = bytes(Random.get_random_bytes(32))
    crypto = AES.new(key, AES.MODE_CBC, iv=iv)
    enc = crypto.encrypt(pad_code(code_bytes, AES.block_size))

    return iv, key, enc


def generate_main(iv, key, enc):
    return """#include <emscripten.h>
#include "AES.h"

EM_JS(void, run_code, (char* str), {{
     new Function(UTF8ToString(str))();
}});

int main() {{
    AES aes(256);
    int len = {len};
    unsigned char enc[] = {{ {enc} }};
    unsigned char iv[] = {{ {iv} }};
    unsigned char key[] = {{ {key} }};
    unsigned char *dec = aes.DecryptCBC(enc, len * sizeof(unsigned char), key, iv, len);
    run_code((char*) dec);
    
    delete[] dec;
}}
""".format(len=len(enc), enc=encode_to_c_array(enc), iv=encode_to_c_array(iv), key=encode_to_c_array(key))


if __name__ == "__main__":
    code = r"..\code\code.txt"
    iv, key, enc = generate_encryption(code)
    with open("./main.cpp", "w") as f:
        f.write(generate_main(iv, key, enc))

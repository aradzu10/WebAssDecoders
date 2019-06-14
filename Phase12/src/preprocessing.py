import os

from Crypto import Random
from Crypto.Cipher import AES
from PIL import Image
import numpy as np


def pad_code(code_bytes, round_to):
    pad = bytes([0] * ((round_to - len(code_bytes)) % round_to))
    return code_bytes + pad


def get_best_score(array, code, channels):
    min_score = np.infty
    min_index = -1

    code_len = code.shape[0]
    for i in range(array.shape[0] - (code_len * channels)):
        tmp = array[i: i + (code_len * channels):channels]
        tmp = np.sum(((tmp - code) ** 2))

        if tmp < min_score:
            min_score = tmp
            min_index = i

    return min_index


def write_code(pixels, loc, code):
    pixels[0:4] = list(loc[0].to_bytes(4, byteorder='little'))
    pixels[loc[0]:loc[0] + (len(code) * loc[1]):loc[1]] = code
    return pixels


def preprocessing(code_bytes, image_path, cipher_path):

    image = Image.open(image_path)
    pixels = np.array(image)
    org_shape = pixels.shape
    pixels = pixels.reshape((np.prod(org_shape), ))

    code_ascii = [c for c in code_bytes]
    code_arr = np.array(code_ascii)

    loc = get_best_score(pixels, code_arr, org_shape[-1])
    pixels = write_code(pixels, (loc, org_shape[-1]), code_arr)

    new_image = Image.fromarray(pixels.reshape(org_shape), image.mode)
    new_image.save(cipher_path, quality=100)


def encode_code(code_path):
    with open(code_path, "rb") as f:
        code_bytes = f.read()

    iv = bytes(Random.get_random_bytes(AES.block_size))
    key = bytes(Random.get_random_bytes(AES.key_size[-1]))
    crypto = AES.new(key, AES.MODE_CBC, iv=iv)
    enc = crypto.encrypt(pad_code(code_bytes, AES.block_size))

    return iv + key + enc + bytes(0), len(enc),


def generate_main(code_len, code_path, block_size, key_size):
    return """#define STB_IMAGE_IMPLEMENTATION

#include <emscripten.h>
#include <string>
#include <iostream>
#include <sstream>
#include "stb_image.h"
#include "AES.h"

using namespace std;

EM_JS(void, run_code, (const char* str), {
     new Function(UTF8ToString(str))();
});

int main() {
    int x, y, n, i;
    int len = %d;
    unsigned char *data = stbi_load("%s",
     &x, &y, &n, 0);
    
    if (!data)
    {
        printf("cannot open image\\n");
        return 1;
    }
    
    int curr = ((int*) data)[0];

    ostringstream iv("");
    for (i = 0; i < %d; i++) {
        iv << data[curr + (i * n)];
    }
    curr = curr + (i * n);

    ostringstream key("");
    for (i = 0; i < %d; i++) {
        key << data[curr + (i * n)];
    }
    curr = curr + (i * n);

    ostringstream enc("");
    for (i = 0; i < len; i++) {
        enc << data[curr + (i * n)];
    }
    
    AES aes(%d);
    unsigned char *dec = aes.DecryptCBC((unsigned char*) enc.str().c_str(), len * sizeof(unsigned char), 
                                        (unsigned char*)key.str().c_str(), (unsigned char*)iv.str().c_str(), len);
    run_code((char*) dec);

    delete[] dec;
    stbi_image_free(data);
}
""" % (code_len, code_path, block_size, key_size, key_size*8)


def main():
    code_path = "../code/code.txt"
    image_path = "../code/img.png"

    folder_name = os.path.dirname(image_path)
    file_name, ext = os.path.splitext(os.path.basename(image_path))
    cipher_path = folder_name + "/" + file_name + "_enc" + ext

    code, code_len = encode_code(code_path)

    preprocessing(code, image_path, cipher_path)

    if cipher_path != "../code/img_enc.png" and cipher_path != "..\\code\\img_enc.png":
        print("Warning! you change the image path. "
              "you need to change the --preload-file flag in build/build_and_run.bat")

    with open('../src/main.cpp', "w") as f:
        f.write(generate_main(code_len, cipher_path, AES.block_size, AES.key_size[-1]))


if __name__ == "__main__":
    main()

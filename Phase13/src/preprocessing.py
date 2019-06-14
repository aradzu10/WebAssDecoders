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
    print(loc)
    pixels = write_code(pixels, (loc, org_shape[-1]), code_arr)

    new_image = Image.fromarray(pixels.reshape(org_shape), image.mode)
    new_image.save(cipher_path, quality=100)


def encode_code(code_path):
    with open(code_path, "rb") as f:
        code_bytes = f.read()

    iv = bytes(Random.get_random_bytes(16))
    key = bytes(Random.get_random_bytes(32))
    crypto = AES.new(key, AES.MODE_CBC, iv=iv)
    enc = crypto.encrypt(pad_code(code_bytes, AES.block_size))

    return iv + bytes(0) + key + bytes(0) + enc + bytes(0)


def main():
    code_path = r"..\code\code.txt"
    image_path = r"..\code\img.png"

    folder_name = os.path.dirname(image_path)
    file_name, ext = os.path.splitext(os.path.basename(image_path))
    cipher_path = os.path.join(folder_name, file_name + "_enc" + ext)

    code = encode_code(code_path)

    preprocessing(code, image_path, cipher_path)


if __name__ == "__main__":
    main()

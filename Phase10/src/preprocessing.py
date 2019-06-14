import os
from PIL import Image
import numpy as np


def get_best_score(array, code, channels):
    # TODO - need to find best by skips of channels
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


def preprocessing(code_path, image_path, cipher_path):
    with open(code_path, "rb") as f:
        code = f.read()

    image = Image.open(image_path)
    pixels = np.array(image)
    org_shape = pixels.shape
    pixels = pixels.reshape((np.prod(org_shape), ))

    code_ascii = [c for c in code]
    code_ascii.append(0)
    code_arr = np.array(code_ascii)

    loc = get_best_score(pixels, code_arr, org_shape[-1])
    print(loc)
    pixels = write_code(pixels, (loc, org_shape[-1]), code_arr)

    new_image = Image.fromarray(pixels.reshape(org_shape), image.mode)
    new_image.save(cipher_path, quality=100)


def main():
    code_path = r"C:\Users\arzulti\Project\WebAssDecoders\Phase10\code\code.txt"
    image_path = r"C:\Users\arzulti\Project\WebAssDecoders\Phase10\code\img.png"

    folder_name = os.path.dirname(image_path)
    file_name, ext = os.path.splitext(os.path.basename(image_path))
    cipher_path = os.path.join(folder_name, file_name + "_enc" + ext)

    preprocessing(code_path, image_path, cipher_path)


if __name__ == "__main__":
    main()

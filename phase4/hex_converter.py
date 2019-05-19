from Crypto import Random


def genrate_hex():
    src = "C:\Projects\WebAssDecoders\phase4\code\code.txt"
    dst = "C:\Projects\WebAssDecoders\phase4\code\preprocessing.txt"
    with open(src, mode='rb') as f:
        pt = f.read()

    print pt
    len_str = 'int plain_len = ' + str(len(pt)) + ';\n'

    padded_len = pad_to(len(pt), 16)
    padded_str = 'int padded_len = ' + str(padded_len) + ';\n'

    enc = ", ".join("0x{:02x}".format(ord(c)) for c in pt)
    # print enc
    enc_str = 'unsigned char plain[] = { ' + enc + ' };\n'

    iv_ = bytes(Random.get_random_bytes(16))
    iv = ", ".join("0x{:02x}".format(ord(c)) for c in iv_)
    # print iv
    iv_str = 'unsigned char iv[] = { ' + iv + ' };\n'

    key_ = bytes(Random.get_random_bytes(32))
    key = ", ".join("0x{:02x}".format(ord(c)) for c in key_)
    # print key
    key_str = 'unsigned char key[] = { ' + key + ' };\n'

    output = len_str + enc_str + iv_str +key_str
    print output

    with open(dst, mode='w') as f:
        pt = f.write(output)
        


def pad_to(num, pad):
    mod = num % pad
    return num + (pad - mod)



def main():
    genrate_hex()


if __name__ == "__main__":
    main()

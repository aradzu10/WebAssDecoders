import base64
import os
from Crypto.Cipher import AES
from Crypto import Random

class AESCipher:
    def __init__(self, bs):
        self.bs = bs
        self.key = os.urandom(16)

    def encrypt(self, raw):
        raw = self.pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self.unpad(cipher.decrypt(enc[16:]))

    def pad(self, raw):
        return raw + (self.bs - len(raw) % self.bs) * chr(self.bs - len(raw) % self.bs) 

    def unpad(self, raw):
        return raw[:-ord(raw[len(raw)-1:])]

def main():
    scheme = AESCipher(16)
    key = scheme.key
    enc = scheme.encrypt("alert('hello there, general kenobi');")
    print(key)
    print(str(enc))

if __name__ == "__main__":
    main()
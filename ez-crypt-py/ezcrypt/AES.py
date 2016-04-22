from Crypto import Random
from Crypto.Cipher import AES

from .conversions import *
from .pad import *

# Encryption modes
MODE_CBC = AES.MODE_CBC
MODE_ECB = AES.MODE_ECB
MODE_PGP = AES.MODE_PGP
MODE_CFB = AES.MODE_CFB
MODE_OFB = AES.MODE_OFB
MODE_CTR = AES.MODE_CTR
MODE_OPENPGP = AES.MODE_OPENPGP

__all__ = ['MODE_CBC', 'MODE_CBC', 'MODE_PGP', 'MODE_CFB', 'MODE_OFB', 'MODE_CTR', 'MODE_OPENPGP',
           'decrypt', 'encrypt', 'generate_key_iv', 'CryptString', 'CryptBytes', 'Crypt']


def decrypt(data, key, iv, mode=MODE_CFB, segment_size=128, padding=METHOD_PKCS7):
    aes = AES.new(key, mode, iv, segment_size=segment_size)
    decrypted = aes.decrypt(data)
    if padding:
        return unpad(decrypted, padding)
    return decrypted


def encrypt(data, key, iv, mode=MODE_CFB, segment_size=128, padding=METHOD_PKCS7, block_size=16):
    aes = AES.new(key, mode, iv, segment_size=segment_size)
    if padding:
        return aes.encrypt(pad(data, block_size, padding))
    return aes.encrypt(data)


def generate_key_iv(key_length=16, iv_length=16):
    return Random.get_random_bytes(key_length), Random.get_random_bytes(iv_length)


class CryptString(str):
    def encrypt(self, key, iv, mode=AES.MODE_CFB, segment_size=128, padding=METHOD_PKCS7, block_size=16):
        return CryptString(encrypt(self.encode(), key, iv, mode, segment_size, padding, block_size).hex())

    def decrypt(self, key, iv, mode=MODE_CFB, segment_size=128, padding=METHOD_PKCS7, encoding='utf-8'):
        return CryptString(decrypt(str2hex(self), key, iv, mode, segment_size, padding).decode(encoding))


class CryptBytes(bytes):
    def encrypt(self, key, iv, mode=AES.MODE_CFB, segment_size=128, padding=METHOD_PKCS7):
        return CryptBytes(encrypt(self, key, iv, mode, segment_size, padding))

    def decrypt(self, key, iv, mode=MODE_CFB, segment_size=128, padding=METHOD_PKCS7):
        return CryptBytes(decrypt(self, key, iv, mode, segment_size, padding))


class Crypt:
    def __init__(self,
                 key=Random.get_random_bytes(16),
                 iv=Random.get_random_bytes(16),
                 mode=MODE_CFB,
                 segment_size=128,
                 use_padding=METHOD_PKCS7,
                 block_size=16):
        self.key = key
        self.iv = iv
        self.mode = mode
        self.segment_size = segment_size
        self.use_padding = use_padding
        self.block_size = block_size

    def encrypt(self, data):
        return encrypt(data, self.key, self.iv, self.mode, self.segment_size, self.use_padding, self.block_size)

    def decrypt(self, data):
        return decrypt(data, self.key, self.iv, self.mode, self.segment_size, self.use_padding)

    def new_key_iv(self, key_length=16, iv_length=16):
        self.key, self.iv = generate_key_iv(key_length, iv_length)
        return self.key, self.iv
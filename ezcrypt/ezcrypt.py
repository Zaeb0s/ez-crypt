from Crypto.Cipher import AES
from Crypto import Random
from hashlib import sha256
"""Encrypts/decrypts data for the CryptoJS JavaScript module
use mode: CryptoJS.mode.CFB
    padding: CryptoJS.pad.Pkcs7
    a 16 byte key and a 16 byte iv
"""


def _bytes2int(data):
    """ Converts bytes list/string to unsigned decimal """
    return int.from_bytes(data, byteorder='big')


def _int2bytes(data, size):
    return data.to_bytes(size, byteorder='big')


def _str2hex(string):
    try:
        _hex = int(string,16)
    except ValueError:
        return False
    return _int2bytes(_hex, int(len(string)/2))


def generate_key_iv(one=False):
    keyiv = Random.get_random_bytes(32)
    if one:
        return keyiv.hex()
    else:
        return keyiv[:16], keyiv[16:]


def _unpad_bytes(bytes):
    """Remove the PKCS#7 padding from a bytearray"""
    in_len = len(bytes)
    pad_size = bytes[-1]
    if pad_size > 16:
        raise ValueError('Input is not padded or padding is corrupt')
    return bytes[:in_len - pad_size]


def _pad_bytes(bytes):
    """Pad an input string according to PKCS#7"""
    in_len = len(bytes)
    pad_size = 16 - (in_len % 16)
    return bytes.ljust(in_len + pad_size, pad_size.to_bytes(1, 'big'))


def decrypt(bytes, key, iv):
    aes = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
    decrypted = aes.decrypt(bytes)
    return _unpad_bytes(decrypted)


def encrypt(bytes, key=None, iv=None):
    if key is None and iv is None:
        key = Random.get_random_bytes(16)
        iv = Random.get_random_bytes(16)
    aes = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
    encrypted = aes.encrypt(_pad_bytes(bytes))
    if key is None and iv is None:
        return key, iv, encrypted
    else:
        return encrypted


def sha256hash(data):
    if hasattr(data, 'encode'):
        data = data.encode()
    return sha256(data).digest()


class Crypt:
    def __init__(self, key=Random.get_random_bytes(16), iv=Random.get_random_bytes(16)):
        self.key = key
        self.iv = iv

    def decrypt(self, data):
        """Decrypts bytes
        """
        return decrypt(data, self.key, self.iv)

    def encrypt(self, data):
        return encrypt(data, self.key, self.iv)

    def get_key_iv(self, string=False):
        if string:
            return self.key.hex() + self.iv.hex()
        else:
            return self.key + self.iv

    def new_key_iv(self):
        self.key, self.iv = generate_key_iv()


class CryptString(str):
    def encrypt(self, key, iv):
        return CryptString(encrypt(self.encode(), key, iv).hex())

    def decrypt(self, key, iv):
        return CryptString(decrypt(_str2hex(self), key, iv).decode('utf-8'))

    def sha256hash(self, return_hexstring=True):
        hash = sha256hash(self.encode())
        if return_hexstring:
            return hash.hex()
        return hash


class CryptBytes(bytes):
    def encrypt(self, key, iv):
        return CryptBytes(encrypt(self, key, iv))

    def decrypt(self, key, iv):
        return CryptBytes(decrypt(self, key, iv))

    def sha256hash(self):
        return sha256hash(self)

if __name__ == '__main__':
    key, iv = generate_key_iv()
    string = b'Hello, world!'
    x = CryptBytes(string)

    encrypted = x.encrypt(key, iv)
    print(encrypted)
    decrypted = encrypted.decrypt(key, iv)
    print(decrypted)

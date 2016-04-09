from hashlib import sha256

from Crypto import Random
from Crypto.Cipher import AES

"""Encrypts/decrypts data for the CryptoJS JavaScript module
use mode: CryptoJS.mode.CFB
    padding: CryptoJS.pad.Pkcs7
    a 16 byte key and a 16 byte iv
"""

_DEFAULT_MODE = AES.MODE_CFB
_DEFAULT_SEGMENT_SIZE = 128
_DEFAULT_PADDING = True
_DEFAULT_PADDING_SIZE = 16

def _bytes2int(data):
    """ Converts bytes list/string to unsigned decimal """
    return int.from_bytes(data, byteorder='big')


def _int2bytes(data, size):
    return data.to_bytes(size, byteorder='big')


def _str2hex(string):
    try:
        _hex = int(string, 16)
    except ValueError:
        return False
    return _int2bytes(_hex, int(len(string)/2))


def generate_key_iv():
    keyiv = Random.get_random_bytes(32)
    return keyiv[:16], keyiv[16:]


def _unpad_bytes(data):
    """Remove the PKCS#7 padding from a bytearray"""
    pad_size = data[-1]
    if pad_size > len(data):
        raise ValueError('Input is not padded or padding is corrupt')
    return data[:len(data) - pad_size]


def _pad_bytes(data, max_pad_size=16):
    """Pad an input string according to PKCS#7"""
    pad_size = max_pad_size- (len(data) % max_pad_size)
    return data.ljust(len(data) + pad_size, pad_size.to_bytes(1, 'big'))


def decrypt(data, key, iv, mode=AES.MODE_CFB, segment_size=128, unpad=True):
    aes = AES.new(key, mode, iv, segment_size=segment_size)
    decrypted = aes.decrypt(data)
    if unpad:
        return _unpad_bytes(decrypted)
    return decrypted


def encrypt(data, key, iv, mode=AES.MODE_CFB, segment_size=128, pad=True):
    aes = AES.new(key, mode, iv, segment_size=segment_size)
    if pad:
        return aes.encrypt(_pad_bytes(data))
    return aes.encrypt(data)


def sha256hash(data):
    if hasattr(data, 'encode'):
        data = data.encode()
    return sha256(data).digest()


class Crypt:
    def __init__(self,
                 key=Random.get_random_bytes(16),
                 iv=Random.get_random_bytes(16),
                 mode=AES.MODE_CFB,
                 segment_size=128,
                 use_padding=True):
        self.key = key
        self.iv = iv
        self.mode = mode
        self.segment_size = segment_size
        self.use_padding = use_padding

    def encrypt(self, data):
        return encrypt(data, self.key, self.iv, self.mode, self.segment_size, self.use_padding)

    def decrypt(self, data):
        return decrypt(data, self.key, self.iv, self.mode, self.segment_size, self.use_padding)

    def new_key_iv(self):
        self.key, self.iv = generate_key_iv()


class CryptString(str):
    def encrypt(self, key, iv, mode=AES.MODE_CFB, segment_size=128, pad=True):
        return CryptString(encrypt(self.encode(), key, iv, mode, segment_size, pad).hex())

    def decrypt(self, key, iv, mode=AES.MODE_CFB, segment_size=128, unpad=True, encoding='utf-8'):
        return CryptString(decrypt(_str2hex(self), key, iv, mode, segment_size, unpad).decode(encoding))

    def sha256hash(self, return_hexstring=True):
        hash = sha256hash(self.encode())
        if return_hexstring:
            return hash.hex()
        return hash


class CryptBytes(bytes):
    def encrypt(self, key, iv, mode=AES.MODE_CFB, segment_size=128, pad=True):
        return CryptBytes(encrypt(self, key, iv, mode, segment_size, pad))

    def decrypt(self, key, iv, mode=AES.MODE_CFB, segment_size=128, unpad=True):
        return CryptBytes(decrypt(self, key, iv, mode, segment_size, unpad))

    def sha256hash(self):
        return sha256hash(self)

if __name__ == '__main__':
    _key, _iv = generate_key_iv()
    string = b'Hello, world!'
    x = CryptBytes(string)

    encrypted = x.encrypt(_key, _iv)
    print(encrypted)
    decrypted = encrypted.decrypt(_key, _iv)
    print(decrypted)

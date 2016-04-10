from hashlib import sha256

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Counter

"""Encrypts/decrypts data for the CryptoJS JavaScript module
use mode: CryptoJS.mode.CFB
    padding: CryptoJS.pad.Pkcs7
    a 16 byte key and a 16 byte iv

    Does not currently work with AES.MODE_CTR
"""

_DEFAULT_MODE = AES.MODE_CFB
_DEFAULT_SEGMENT_SIZE = 128
_DEFAULT_PADDING = True
_DEFAULT_PADDING_SIZE = 16
_DEFAULT_COUNTER = Counter
_DEFAULT_KEY_LENGTH = 16
_DEFAULT_IV_LENGTH = 16


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


def generate_key_iv(key_length=_DEFAULT_KEY_LENGTH, iv_length=_DEFAULT_IV_LENGTH):
    return Random.get_random_bytes(key_length), Random.get_random_bytes(iv_length)


def _unpad_bytes(data):
    """Remove the PKCS#7 padding from a bytearray"""
    pad_size = data[-1]
    return data[:len(data) - pad_size]


def _pad_bytes(data, max_pad_size=_DEFAULT_PADDING_SIZE):
    """Pad an input string according to PKCS#7"""
    pad_size = max_pad_size - (len(data) % max_pad_size)
    return data.ljust(len(data) + pad_size, pad_size.to_bytes(1, 'big'))


def decrypt(data, key, iv, mode=_DEFAULT_MODE, segment_size=_DEFAULT_SEGMENT_SIZE, unpad=_DEFAULT_PADDING):
    aes = AES.new(key, mode, iv, segment_size=segment_size)
    decrypted = aes.decrypt(data)
    if unpad:
        return _unpad_bytes(decrypted)
    return decrypted


def encrypt(data, key, iv, mode=_DEFAULT_MODE, segment_size=_DEFAULT_SEGMENT_SIZE, pad=_DEFAULT_PADDING):
    aes = AES.new(key, mode, iv, segment_size=segment_size)
    if pad:
        return aes.encrypt(_pad_bytes(data))
    return aes.encrypt(data)


def sha256hash(data):
    return sha256(data).digest()


class Crypt:
    def __init__(self,
                 key=Random.get_random_bytes(_DEFAULT_KEY_LENGTH),
                 iv=Random.get_random_bytes(_DEFAULT_IV_LENGTH),
                 mode=_DEFAULT_MODE,
                 segment_size=_DEFAULT_SEGMENT_SIZE,
                 use_padding=_DEFAULT_PADDING):
        self.key = key
        self.iv = iv
        self.mode = mode
        self.segment_size = segment_size
        self.use_padding = use_padding

    def encrypt(self, data):
        return encrypt(data, self.key, self.iv, self.mode, self.segment_size, self.use_padding)

    def decrypt(self, data):
        return decrypt(data, self.key, self.iv, self.mode, self.segment_size, self.use_padding)

    def new_key_iv(self, key_length=_DEFAULT_KEY_LENGTH, iv_length=_DEFAULT_IV_LENGTH):
        self.key, self.iv = generate_key_iv(key_length, iv_length)
        return self.key, self.iv


class CryptString(str):
    def encrypt(self, key, iv, mode=_DEFAULT_MODE, segment_size=_DEFAULT_SEGMENT_SIZE, pad=_DEFAULT_PADDING):
        return CryptString(encrypt(self.encode(), key, iv, mode, segment_size, pad).hex())

    def decrypt(self, key, iv, mode=_DEFAULT_MODE, segment_size=_DEFAULT_SEGMENT_SIZE,
                unpad=_DEFAULT_PADDING, encoding='utf-8'):
        return CryptString(decrypt(_str2hex(self), key, iv, mode, segment_size, unpad).decode(encoding))

    def sha256hash(self):
        return sha256hash(self.encode())


class CryptBytes(bytes):
    def encrypt(self, key, iv, mode=_DEFAULT_MODE, segment_size=_DEFAULT_SEGMENT_SIZE, pad=_DEFAULT_PADDING):
        return CryptBytes(encrypt(self, key, iv, mode, segment_size, pad))

    def decrypt(self, key, iv, mode=_DEFAULT_MODE, segment_size=_DEFAULT_SEGMENT_SIZE,
                unpad=_DEFAULT_PADDING):
        return CryptBytes(decrypt(self, key, iv, mode, segment_size, unpad))

    def sha256hash(self):
        return sha256hash(self)

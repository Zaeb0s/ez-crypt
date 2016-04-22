from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA as Crypto_RSA
from Crypto.PublicKey import pubkey
from Crypto.Util import Counter
from hashlib import sha256

"""Encrypts/decrypts data for the CryptoJS JavaScript module
use mode: CryptoJS.mode.CFB
    padding: CryptoJS.pad.Pkcs7
    a 16 byte key and a 16 byte iv

    Does not currently work with AES.MODE_CTR
"""


# def _bytes2int(data):
#     """ Converts bytes list/string to unsigned decimal """
#     return int.from_bytes(data, byteorder='big')
#
#
# def _int2bytes(data, size=None):
#     if size is None:
#         return data.to_bytes((data.bit_length() + 7) // 8, 'big') or b'\0'
#
#     return data.to_bytes(size, byteorder='big')
#
#
# def _str2hex(string):
#     try:
#         _hex = int(string, 16)
#     except ValueError:
#         return False
#     return _int2bytes(_hex, int(len(string)/2))


# def generate_key_iv(key_length=16, iv_length=16):
#     return Random.get_random_bytes(key_length), Random.get_random_bytes(iv_length)


# def decrypt(data, key, iv, mode=AES.MODE_CFB, segment_size=128, padding=Pad.PKCS7):
#     aes = AES.new(key, mode, iv, segment_size=segment_size)
#     decrypted = aes.decrypt(data)
#     if padding:
#         return Pad.unpad(decrypted, padding)
#     return decrypted
#
#
# def encrypt(data, key, iv, mode=AES.MODE_CFB, segment_size=128, padding=Pad.PKCS7):
#     aes = AES.new(key, mode, iv, segment_size=segment_size)
#     if padding:
#         return aes.encrypt(Pad.pad(data, segment_size, padding))
#     return aes.encrypt(data)


# def sha256hash(data):
#     return sha256(data).digest()


# class Crypt:
#     def __init__(self,
#                  key=Random.get_random_bytes(16),
#                  iv=Random.get_random_bytes(16),
#                  mode=_DEFAULT_MODE,
#                  segment_size=128,
#                  use_padding=Pad.PKCS7):
#         self.key = key
#         self.iv = iv
#         self.mode = mode
#         self.segment_size = segment_size
#         self.use_padding = use_padding
#
#     def encrypt(self, data):
#         return encrypt(data, self.key, self.iv, self.mode, self.segment_size, self.use_padding)
#
#     def decrypt(self, data):
#         return decrypt(data, self.key, self.iv, self.mode, self.segment_size, self.use_padding)
#
#     def new_key_iv(self, key_length=_DEFAULT_KEY_LENGTH, iv_length=_DEFAULT_IV_LENGTH):
#         self.key, self.iv = generate_key_iv(key_length, iv_length)
#         return self.key, self.iv

#
# class CryptString(str):
#     def encrypt(self, key, iv, mode=_DEFAULT_MODE, segment_size=128, padding=Pad.PKCS7):
#         return CryptString(encrypt(self.encode(), key, iv, mode, segment_size, padding).hex())
#
#     def decrypt(self, key, iv, mode=_DEFAULT_MODE, segment_size=128,
#                 padding=Pad.PKCS7, encoding='utf-8'):
#         return CryptString(decrypt(_str2hex(self), key, iv, mode, segment_size, padding).decode(encoding))
#
#     def sha256hash(self):
#         return sha256hash(self.encode())
#
#
# class CryptBytes(bytes):
#     def encrypt(self, key, iv, mode=_DEFAULT_MODE, segment_size=128, padding=Pad.PKCS7):
#         return CryptBytes(encrypt(self, key, iv, mode, segment_size, padding))
#
#     def decrypt(self, key, iv, mode=_DEFAULT_MODE, segment_size=128,
#                 padding=Pad.PKCS7):
#         return CryptBytes(decrypt(self, key, iv, mode, segment_size, padding))
#
    # def sha256hash(self):
    #     return sha256hash(self)



# class RSA:
#     generate = Crypto_RSA.generate
#     cipher = PKCS1_OAEP.new
#     importKey = Crypto_RSA.importKey
#     construct = Crypto_RSA.construct
#
#     # For backwards compatibility
#     generate_key = Crypto_RSA.generate
#     import_key = Crypto_RSA.importKey
#
#     @staticmethod
#     def key_to_int(key):
#         return _bytes2int(key.exportKey('DER'))
#
#     @staticmethod
#     def ket_from_int(integer):
#         return RSA.importKey(_int2bytes(integer))
#
#     @staticmethod
#     def key_from_file(file):
#         with open(file, 'r') as f:
#             RSA.importKey(f.read())


# class AES(AE:


if __name__ == '__main__':

    key1 = RSA.generate(1024)
    key2 = RSA.generate(1024)

    privkey = RSA.importKey(key1.exportKey())
    pubkey = RSA.importKey(key1.publickey().exportKey())
    cipher1 = RSA.cipher(key1)
    cipher2 = RSA.cipher(key2)

    message = b'Attack at dawn!'
    encrypted = cipher2.encrypt(message)
    decrypted = cipher2.decrypt(encrypted)

    print('Encrypted:', encrypted)
    print('Decrypted:', decrypted)


    # for i in range(1000):
    #     key1 = RSA.generate(1024*2)
    #     int_key = RSA.key_to_int(key1)
    #     key2 = RSA.int_to_key(int_key)
    #
    #     if key1.exportKey() != key2.exportKey():
    #         raise ValueError('Keys are not identical')
    #     print(i, 'done', key1 == key2)
    data = b'h'*16

    pad = Pad.pad(data, type=4)
    upad = Pad.unpad(pad, type=4)
    print(pad)
    print(upad)

    pad = Pad.pad(data, type=1)
    upad = Pad.unpad(pad, type=1)
    print(pad)
    print(upad)

    pad = Pad.pad(data, type=2)
    upad = Pad.unpad(pad, type=2)
    print(pad)
    print(upad)

    pad = Pad.pad(data, type=3)
    upad = Pad.unpad(pad, type=3)
    print(pad)
    print(upad)


    key, iv = generate_key_iv()
    encrypted = encrypt(data, key, iv, padding=Pad.ANSIX_923)
    decrypted = decrypt(encrypted, key, iv, padding=None)
    print(encrypted)
    print(decrypted)













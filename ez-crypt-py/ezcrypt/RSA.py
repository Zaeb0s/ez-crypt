from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA as _RSA
from Crypto.PublicKey import pubkey

from .conversions import *

__all__ = ['generate', 'cipher', 'importKey', 'construct', 'key_to_int', 'key_from_int', 'key_from_file' ]

generate = _RSA.generate
cipher = PKCS1_OAEP.new
importKey = _RSA.importKey
construct = _RSA.construct


def key_to_int(key):
    return bytes2int(key.exportKey('DER'))


def key_from_int(integer):
    return RSA.importKey(int2bytes(integer))


def key_from_file(file):
    with open(file, 'r') as f:
        RSA.importKey(f.read())

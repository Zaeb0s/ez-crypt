#!/bin/env python3
from .ezcrypt import RSA
from .ezcrypt import encrypt, decrypt, CryptBytes, CryptString, Crypt, sha256hash, generate_key_iv

with open(__path__[0] + '/version', 'r') as r:
    __version__ = r.read()

#!/bin/env python3
from .ezcrypt import Crypt, encrypt, decrypt, generate_key_iv, sha256hash, CryptBytes, CryptString

with open(__path__[0] + '/version', 'r') as r:
    __version__ = r.read()

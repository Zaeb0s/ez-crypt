#!/bin/env python3

# import ezcrypt
# string = 'Hello, world!'
#
# print()
# print('Testing basic functions...')
# key, iv = ezcrypt.generate_key_and_iv()
# print('Key:', key)
# print('IV:', iv)
# encrypted_string = ezcrypt.encrypt(string.encode(), key, iv)
# print('Encrypted string:', encrypted_string)
# print('Decrypted string:', ezcrypt.decrypt(encrypted_string, key, iv).decode('utf-8'))
#
# print()
# print('Testing class...')
# c = ezcrypt.Crypt()
# print('Encrypting string:', string)
# encrypted_string = c.encrypt(string.encode())
# print('Encrypted string:', encrypted_string)
# print('Decrypted string:', c.decrypt(encrypted_string).decode('utf-8'))
#

from ezcrypt import CryptBytes, generate_key_iv
key, iv = generate_key_iv()
string = CryptBytes(b'Hello, world!')

encrypted = string.encrypt(key, iv)
dectypted = encrypted.decrypt(key, iv)
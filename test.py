#!/bin/env python3
from time import time



print()
print('Testing basic functions...')
from ezcrypt import encrypt, decrypt, generate_key_iv
t1 = time()
string = 'Hello, world!'
key, iv = generate_key_iv()
encrypted = encrypt(string.encode(), key, iv)
decrypted = decrypt(encrypted, key, iv)
print('Time:', (time()-t1)*1000, 'ms')
print('Key:', key)
print('IV:', iv)
print('Encrypted string:', encrypted)
print('Decrypted string:', decrypted.decode('utf-8'))


print()
print('Testing class...')
from ezcrypt import Crypt
t1 = time()
string = 'Hello, world!'
c = Crypt()
encrypted = c.encrypt(string.encode())
decrypted = c.decrypt(encrypted)

print('Time:', (time()-t1)*1000, 'ms')
print('Encrypting string:', string)
print('Key:', c.key)
print('IV:', c.iv)
print('Encrypted string:', encrypted)
print('Decrypted string:', decrypted.decode('utf-8'))


print()
print('Testing CryptBytes...')
from ezcrypt import CryptBytes, generate_key_iv
t1 = time()
data = b'Hello, world!'
key, iv = generate_key_iv()
string = CryptBytes(data)
encrypted = string.encrypt(key, iv)
decrypted = encrypted.decrypt(key, iv)
print('Time:', (time()-t1)*1000, 'ms')
print('Bytes:', data)
print('Key:', key)
print('IV:', iv)
print('Encrypted:', encrypted)
print('Decrypted:', decrypted)


print()
print('Testing CryptString...')
from ezcrypt import CryptString, generate_key_iv
t1 = time()
data = 'Hello, world!'
key, iv = generate_key_iv()
string = CryptString(data)
encrypted = string.encrypt(key, iv)
decrypted = encrypted.decrypt(key, iv)
print('Time:', (time()-t1)*1000, 'ms')
print('String:', data)
print('Key:', key)
print('IV:', iv)
print('Encrypted:', encrypted)
print('Decrypted:', decrypted)


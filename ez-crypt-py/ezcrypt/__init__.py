# Encrypts/decrypts data for the CryptoJS JavaScript module
# use mode: CryptoJS.mode.CFB
# padding: CryptoJS.pad.Pkcs7
# a 16 byte key and a 16 byte iv
# Does not currently work with AES.MODE_CTR


import ezcrypt.AES as AES
import ezcrypt.RSA as RSA
import ezcrypt.pad as Padding

with open(__path__[0] + '/version', 'r') as r:
    __version__ = r.read()

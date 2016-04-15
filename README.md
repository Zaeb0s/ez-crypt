# ezcrypt
A python module for AES that works well together with the javascripts CryptoJS.

# Python side
## Installation
```sh
pip install ezcrypt
```
## Basics
```python
import ezcrypt
# Generate Key and iv
key, iv = ezcrypt.generate_key_iv()

string = 'Hello, World!'
# Encrypt (Returns bytes object) 
encrypted = ezcrypt.encrypt(string.encode(), key, iv)

# Decrypt (Returns bytes object)
decrypted = ezcrypt.decrypt(encrypted, key, iv)

```
## The Crypt class
```python
from ezcrypt import Crypt

# Crypt generates 32 random bytes at initiation
# That it uses as the encryption key and IV
# To use custom key and IV use Crypt(key=custom_key, iv=custom_iv)
# Make sure they are two bytes objects each of length 16
crypt = Crypt()

string = 'Hello, world!'
encrypted_string = crypt.encrypt(string.encode())
decrypted_string = crypt.decrypt(encrypted_string)
```
## CryptString and CryptBytes
Adds methods for encryption and decryption to str or bytes objects.
CryptString works with str objects while CryptBytes works with bytes objects (more efficient than CryptString)

```python
from ezcrypt import CryptString, generate_key_iv
key, iv = generate_key_iv()
string = CryptString('Hello, world!')

encrypted = string.encrypt(key, iv)
decrypted = encrypted.decrypt(key, iv)
```


# JavaScript side
## Installation
```sh
npm install ez-crypt
```

## A simple example
```javascript
ezcrypt = require('ez-crypt');

var crypt = new ezcrypt.Crypt(),
    string = 'Hello, world!',
    encrypted = crypt.encrypt(string),
    decrypted = crypt.decrypt(encrypted);
    
console.log('String to encrypt: ' + string);
console.log('Key: ' + crypt.key_str);
console.log('IV: ' + crypt.iv_str);
console.log('Encrypted string: ' + encrypted);
console.log('Decrypted string: ' + decrypted);
```

## The Crypt class variables
Variable | Description | Requirements | Default
---------|-------------|--------------|--------
key | They encryption/decryption key | A string containing 32 random hex numbers | 32 random hex numbers
iv | The initialization vectior | A string containing 32 random hex numbers | 32 random hex numbers
mode | The cryptographic method | Modes from the crypto-js package | mode.CFB
padding | The method used for padding | Padding types from the crypto-js package | pad.Pkcs7

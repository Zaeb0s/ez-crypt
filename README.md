# ezcrypt
A python module for AES that works well together with the javascripts CryptoJS.
 
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


## JavaScript side
Download and include the required components from crypto-js (aes.js, mode-cfb.js, pad-nopadding-min.js). 
Can be downloaded from :http://crypto-js.googlecode.com/svn/tags/3.1.2/src/ 
```javascript
//Encryption
string = 'Hello, world'
// Key and iv are both initially two hexstrings
// Convert them using CryptoJS.enc.Hex.parse
key = CryptoJS.enc.Hex.parse(key);
iv = CryptoJS.enc.Hex.parse(iv);

encrypted = CryptoJS.AES.encrypt(
                string,
                key,
                {
                    iv: iv,
                    padding: CryptoJS.pad.Pkcs7,
                    mode: CryptoJS.mode.CFB
                }).ciphertext.toString();
                
// Decryption
decrypted = CryptoJS.AES.decrypt(
                encrypted,
                key,
                {
                    iv: iv,
                    padding: CryptoJS.pad.Pkcs7,
                    mode: CryptoJS.mode.CFB
                }).toString(CryptoJS.enc.Utf8);
```

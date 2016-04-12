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
Download and include the required components from crypto-js (core.js, cipher-core.js, aes.js, mode-cfb.js)
```sh
npm install crypto-js
```
Or using html:
```html
<script src="http://crypto-js.googlecode.com/svn/tags/3.1.2/build/components/core-min.js"></script>
<script src="http://crypto-js.googlecode.com/svn/tags/3.1.2/build/components/cipher-core-min.js"></script>
<script src="http://crypto-js.googlecode.com/svn/tags/3.1.2/build/components/aes-min.js"></script>
<script src="http://crypto-js.googlecode.com/svn/tags/3.1.2/build/components/mode-cfb-min.js"></script>
```

```javascript
// If using node
if (typeof require !== 'undefined') {
    CryptoJS = require('crypto-js')
}
// Key and iv are both initially two hexstrings of lengths 32
var key = '4806baf70a60107c026979e9036f9dd9',
    iv = '37c4bc628f415daf31441b6594ef1622'

// Convert them using CryptoJS.enc.Hex.parse
key = CryptoJS.enc.Hex.parse(key);
iv = CryptoJS.enc.Hex.parse(iv);

//Encryption
var string = 'Hello, world',
    encrypted_hex_string = CryptoJS.AES.encrypt(
                string,
                key,
                {
                    iv: iv,
                    padding: CryptoJS.pad.Pkcs7,
                    mode: CryptoJS.mode.CFB
                }).ciphertext.toString();

// Decryption

// Convert the hex string
var encrypted = CryptoJS.lib.CipherParams.create({
            ciphertext: CryptoJS.enc.Hex.parse(encrypted_hex_string)
            }),        
    decrypted = CryptoJS.AES.decrypt(
                encrypted,
                key,
                {
                    iv: iv,
                    padding: CryptoJS.pad.Pkcs7,
                    mode: CryptoJS.mode.CFB
                }).toString(CryptoJS.enc.Utf8);
                
console.log('String: ' + string)
console.log('Encrypted: ' + encrypted_hex_string)
console.log('Decrypted: ' + decrypted)

```

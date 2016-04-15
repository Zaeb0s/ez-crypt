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


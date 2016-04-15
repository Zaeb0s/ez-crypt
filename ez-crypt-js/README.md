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

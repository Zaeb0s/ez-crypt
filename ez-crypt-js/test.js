ezcrypt = require('./ezcrypt');

var crypt = new ezcrypt.Crypt(),
    string = 'Hello, world!',
    encrypted = crypt.encrypt(string),
    decrypted = crypt.decrypt(encrypted);

console.log('String in encrypt: ' + string);
console.log('Key: ' + crypt.key_str);
console.log('IV: ' + crypt.iv_str);
console.log('Encrypted string: ' + encrypted);
console.log('Decrypted string: ' + decrypted);
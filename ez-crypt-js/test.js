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





var string = 'Hello, world',
    key = ezcrypt.RSA.generate_key(),
    encrypted = ezcrypt.RSA.encrypt(string, key);
    decrypted = ezcrypt.RSA.decrypt(encrypted, key);

console.log('String in encrypt: ' + string);
console.log('Encrypted string: ' + encrypted);
console.log('Decrypted string: ' + decrypted);
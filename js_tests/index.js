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

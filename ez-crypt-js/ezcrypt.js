
CryptoJS = require('crypto-js');
forge = require('node-forge');

exports.Crypt = function(key, iv, mode, padding){
    this.key_str = key || random_hex(32);
    this.iv_str = iv || random_hex(32);
    this.mode = mode || CryptoJS.mode.CFB;
    this.padding = padding || CryptoJS.pad.Pkcs7;

    this.key = CryptoJS.enc.Hex.parse(this.key_str);
    this.iv = CryptoJS.enc.Hex.parse(this.iv_str);

    this.encrypt = function encrypt(data) {
        return _encrypt(data, this.key, this.iv, this.mode, this.padding);
    };

    this.decrypt = function decrypt(data) {
        return _decrypt(data, this.key, this.iv, this.mode, this.padding);
    };

    this.new_key_iv = function new_key_iv(key, iv){
        this.key_str = key || random_hex(32);
        this.iv_str = iv || random_hex(32);

        this.key = CryptoJS.enc.Hex.parse(this.key_str);
        this.iv = CryptoJS.enc.Hex.parse(this.iv_str);
    };

    function _encrypt(data, key, iv, mode, padding){
        mode = mode || CryptoJS.mode.CFB;
        padding = padding || CryptoJS.pad.Pkcs7;
        return CryptoJS.AES.encrypt(
            data,
            key,
            {
                iv: iv,
                padding: padding,
                mode: mode
            }).ciphertext.toString();
    }

    function _decrypt(data, key, iv, mode, padding){
        mode = mode || CryptoJS.mode.CFB;
        padding = padding || CryptoJS.pad.Pkcs7;
        return CryptoJS.AES.decrypt(
            CryptoJS.lib.CipherParams.create({ciphertext: CryptoJS.enc.Hex.parse(data)}),
            key,
            {
                iv: iv,
                padding: padding,
                mode: mode
            }).toString(CryptoJS.enc.Utf8);
    }
    
    function random_hex(n){
        var i;
        result = "";
        for( i = 0; i < n; i++ ) {
            result += Math.floor(Math.random() * 16).toString(16);
        }
        return result;
    }
};

exports.RSA = new (function RSA(){ //TODO: Add function for importing keys
    this.generate_key = function generate_key(bits, e){
        bits = bits || 2048;
        e = e || 65537;
        return forge.pki.rsa.generateKeyPair({bits: bits, e: e});
    };

    this.encrypt = function encrypt(data, key, type){
        type = type || 'RSA-OAEP';
        encrypted = key.publicKey.encrypt(data, type);
        return str2hex(encrypted);
    };

    this.decrypt = function encrypt(data, key, type){
        type = type || 'RSA-OAEP';

        return key.privateKey.decrypt(hex2str(data), type);
    };

    this.sign = function sign(data, key){
        var md = forge.md.sha256.create();
        md.update(data, 'utf8');
        return key.privateKey.sign(md);
    };

    this.verify = function verify(data, signature, key){
        var md = forge.md.sha256.create();
        md.update(data, 'urf8');
        key.publicKey.verify(md.digest().bytes(), signature)
    };
    
    this.exportKey(key) = function exportKey{
        forge.pki.privateKeyToPem(key.privateKey)
    };
    
    this.importKey(pem) = function importKey{
        forge.pki.privateKeyFromPem(pem)
    }
})();


function str2hex(string){
    var hex, i;

    var result = "";
    for (i=0; i<string.length; i++) {
        hex = string.charCodeAt(i).toString(16);
        result += ("000"+hex).slice(-4);
    }
    return result
}

function hex2str(hex){
    var j;
    var hexes = hex.match(/.{1,4}/g) || [];
    var back = "";
    for(j = 0; j<hexes.length; j++) {
        back += String.fromCharCode(parseInt(hexes[j], 16));
    }
    return back;
}










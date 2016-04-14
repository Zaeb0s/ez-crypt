
CryptoJS = require('crypto-js');


exports.Crypt = function(key, iv){
    this.key_str = key || random_hex(32);
    this.iv_str = iv || random_hex(32);

    this.key = CryptoJS.enc.Hex.parse(this.key_str);
    this.iv = CryptoJS.enc.Hex.parse(this.iv_str);

    this.encrypt = function encrypt(data, mode, padding) {
        return _encrypt(data, this.key, this.iv, mode, padding);
    };

    this.decrypt = function decrypt(data, mode, padding) {
        return _decrypt(data, this.key, this.iv, mode, padding);
    };

    this.new_key_iv = function new_key_iv(key, iv){
        this.key_str = key || random_hex(32);
        this.iv_str = key || random_hex(32);

        this.key = CryptoJS.enc.Hex.parse(this.key_str);
        this.iv = CryptoJS.enc.Hex.parse(this.iv_str);
    };

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
    function random_hex(n){
        var i;
        result = "";
        for( i = 0; i < n; i++ ) {
            result += Math.floor(Math.random() * 16).toString(16);
        }
        return result;
    }
};
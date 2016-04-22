from Crypto import Random


METHOD_ANSIX_923 = 1
METHOD_ISO10126 = 2
METHOD_PKCS7 = 3
METHOD_ISO_IEC7816_4 = 4


def pad(data, block_size=16, type=METHOD_PKCS7):
    pad_size = block_size - (len(data) % block_size)
    if type == METHOD_PKCS7:
        return data.ljust(len(data) + pad_size, pad_size.to_bytes(1, 'big'))
    elif type == METHOD_ANSIX_923:
        return data.ljust(len(data) + pad_size - 1, b'\x00') + pad_size.to_bytes(1, 'big')
    elif type == METHOD_ISO10126:
        return data + Random.get_random_bytes(pad_size - 1) + pad_size.to_bytes(1, 'big')
    elif type == METHOD_ISO_IEC7816_4:
        return (data + b'\x80').ljust(len(data) + pad_size, b'\x00')
    else:
        raise RuntimeError('Padding type not supported')


def unpad(data, type=METHOD_PKCS7):
    if type == METHOD_PKCS7 or type == METHOD_ANSIX_923 or type == METHOD_ISO10126:
        return data[:-data[-1]]
    elif type == METHOD_ISO_IEC7816_4:
        return data[:data.rfind(b'\x80')]
    else:
        raise RuntimeError('Padding type not supported')
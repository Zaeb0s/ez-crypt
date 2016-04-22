def bytes2int(data):
    """ Converts bytes list/string to unsigned decimal """
    return int.from_bytes(data, byteorder='big')


def int2bytes(data, size=None):
    if size is None:
        return data.to_bytes((data.bit_length() + 7) // 8, 'big') or b'\0'

    return data.to_bytes(size, byteorder='big')


def str2hex(string):
    try:
        _hex = int(string, 16)
    except ValueError:
        return False
    return int2bytes(_hex, int(len(string)/2))
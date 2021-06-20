import codecs


def bin_str(value, max_size):
    if isinstance(value, int):
        result = '{0:b}'.format(value).zfill(max_size)
        # reverse so indexing will work OK
        return result[::-1]
    # Supporting `str` for python2.7 support
    elif isinstance(value, (str, bytes)):
        as_bytearray = bytearray(value)
        result = "".join(
            "{0:b}".format(uint8).zfill(8) for uint8 in as_bytearray
        )
        # NOTE: must encode to little endian
        return result[::-1]
    else:
        raise TypeError("Unsupported type: {}".format(type(value)))


def size_in_bits(value):
    if isinstance(value, bool):
        return 1
    elif isinstance(value, int):
        return len('{0:b}'.format(value))
    elif isinstance(value, (str, bytes)):
        return len(value) * 8

    raise TypeError("invalid type: {}".format(type(value)))


def size_in_bytes(value):
    if isinstance(value, bool):
        return 1
    elif isinstance(value, int):
        if 0 == value:
            return 1

        total_bytes = 0
        while value != 0:
            total_bytes += 1
            value = value >> 8
        return total_bytes
    elif isinstance(value, (str, bytes)):
        return len(value)

    raise TypeError("invalid type: {}".format(type(value)))


def to_bytes(value, minimal_width):
    if isinstance(value, int):
        as_bytes = codecs.decode(
            "{0:x}".format(value).zfill(2 * size_in_bytes(value)),
            'hex'
        )
    elif isinstance(value, bool):
        as_bytes = b'\01' if value else b'\00'
    elif isinstance(value, (str, bytes)):
        as_bytes = value
    else:
        raise TypeError("invalid type: {}".format(type(value)))

    return as_bytes + b'\x00' * (minimal_width - len(as_bytes))


def bytes_to_int(value):
    # Reverse because of endianess
    return int(codecs.encode(value[::-1], 'hex'), 16)
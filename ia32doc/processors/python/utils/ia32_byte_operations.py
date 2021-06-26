import codecs


def bin_str(value, max_size):
    if isinstance(value, bytes):
        as_bytearray = bytearray(value)
        result = "".join(
            "{0:b}".format(uint8).zfill(8) for uint8 in as_bytearray
        )
        # NOTE: must encode to little endian
        return result[::-1]
    try:
        result = '{0:b}'.format(value).zfill(max_size)
        # reverse so indexing will work OK
        return result[::-1]
    except TypeError:
        raise TypeError("Unsupported type: {}".format(type(value)))


def size_in_bits(value):
    if isinstance(value, bool):
        return 1
    elif isinstance(value, bytes):
        return len(value) * 8
    try:
        return len('{0:b}'.format(value))
    except TypeError:
        raise TypeError("invalid type: {}".format(type(value)))


def size_in_bytes(value):
    if isinstance(value, bool):
        return 1
    elif isinstance(value, bytes):
        return len(value)
    try:
        if 0 == value:
            return 1

        total_bytes = 0
        while value != 0:
            total_bytes += 1
            value = value >> 8
        return total_bytes
    except TypeError:
        raise TypeError("invalid type: {}".format(type(value)))


def to_bytes(value, minimal_width):
    if isinstance(value, bool):
        as_bytes = b'\01' if value else b'\00'
    elif isinstance(value, (str, bytes)):
        as_bytes = value
    else:
        try:
            as_bytes = codecs.decode(
                "{0:x}".format(int(value)).zfill(2 * size_in_bytes(int(value))),
                'hex'
            )
            # Transfer to little endian
            as_bytes = as_bytes[::-1]
        except TypeError:
            breakpoint()
            raise TypeError("invalid type: {}".format(type(value)))

    return as_bytes + b'\x00' * (minimal_width - len(as_bytes))


def bytes_to_int(value):
    # Reverse because of endianess
    return int(codecs.encode(value[::-1], 'hex'), 16)
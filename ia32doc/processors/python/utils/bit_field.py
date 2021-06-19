import codecs
import textwrap


class BitField(object):
    def __init__(self, value, size_in_bytes=None):
        if not isinstance(value, int):
            raise TypeError("`value` must in `int`!")
        self._raw = value
        if size_in_bytes is None:
            self._size = self._bytes_in_int(value)
        else:
            self._size = size_in_bytes
        self._total_bits = 8 * self._size

    @staticmethod
    def _bytes_in_int(value):
        total_bytes = 0
        while value != 0:
            total_bytes += 1
            value = value >> 8
        return total_bytes

    @staticmethod
    def _size_in_bits(value):
        if isinstance(value, bool):
            return 1
        if isinstance(value, int):
            return len('{0:b}'.format(value))

        raise TypeError("invalid type: {}".format(type(value)))

    @property
    def size(self):
        return self._size

    @property
    def raw(self):
        # Using a python 2 and 3 compatible method
        return self._raw

    @property
    def bytes(self):
        hex_value = '{0:x}'.format(self._raw).zfill(self._total_bits // 4)
        # must convert to big endian
        hex_value = "".join(textwrap.wrap(hex_value, 2)[::-1])
        return codecs.decode(hex_value, 'hex_codec')

    def __repr__(self):
        return '0b' + '{0:b}'.format(self.raw).zfill(self._total_bits)

    def __str__(self):
        enabled = [
            field for field in self._FIELDS if 0 != self.__getattribute__(field)
        ]
        return ",".join(enabled)

    def __setitem__(self, key, value):
        if not (isinstance(key, slice) or isinstance(key, int)):
            raise TypeError("Slice not supported with type")

        if not (isinstance(value, int) or isinstance(value, bool)):
            raise TypeError("Value can only be integers or booleans")

        if isinstance(key, slice):
            if key.step is not None:
                raise ValueError("Steps are not supported in bitfields!")
            start = key.start
            stop = key.stop

        if isinstance(key, int):
            start = key
            stop = key + 1

        # Check that value fits in range
        max_size_in_bits = stop - start
        if max_size_in_bits < self._size_in_bits(value):
            raise ValueError(
                "{} can not fit in {} bits!".format(
                    value, max_size_in_bits
                )
            )

        # Zero out matching bits
        mask_str = '1' * self._total_bits
        mask_str = mask_str[0:start] + '0' * (stop - start) + mask_str[stop:]
        # Note that the mask is reversed!
        mask_str = mask_str[::-1]
        mask = int(mask_str, base=2)
        self._raw = self._raw & mask
        # Add the value
        self._raw += (value << start)

    # Support slicing
    def __getitem__(self, item):
        if not (isinstance(item, slice) or isinstance(item, int)):
            raise TypeError("Slice not supported with type")

        if isinstance(item, slice):
            if item.step is not None:
                raise ValueError("Steps are not supported in bitfields!")
            start = item.start
            stop = item.stop

        if isinstance(item, int):
            start = item
            stop = item + 1

        # Zero out matching bits
        mask_str = '0' * self._total_bits
        mask_str = mask_str[0:start] + '1' * (stop - start) + mask_str[stop:]
        # Note that the mask is reversed!
        mask_str = mask_str[::-1]
        mask = int(mask_str, base=2)
        raw = self._raw & mask
        # shift-right the remaining bits
        raw = raw >> start
        return raw

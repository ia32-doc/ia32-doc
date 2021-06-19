import codecs
import textwrap


def _size_in_bits(value):
    if isinstance(value, bool):
        return 1
    if isinstance(value, int):
        return len('{0:b}'.format(value))

    raise TypeError("invalid type: {}".format(type(value)))


def _bytes_in_int(value):
    total_bytes = 0
    while value != 0:
        total_bytes += 1
        value = value >> 8
    return total_bytes


class BitFieldMember(object):
    def __init__(self, name, description, offset, width, custom_type=None):
        # Create explicit attributes so that the metaclass will have access
        self.offset = offset
        self.width = width
        self.field = True

        self._name = name
        self._description = description
        if custom_type is not None:
            self._type = custom_type
        # Note: can't extend bool :(
        else:
            self._type = int

        self._container = self._create_container()

    def _create_container(self):
        # Defining width and offset
        methods = dict()
        methods['width'] = self.width
        methods['offset'] = self.offset
        methods['__doc__'] = self._description

        container = type.__new__(
            type,
            self._name,
            tuple([self._type]),
            methods
        )
        return container

    def __get__(self, instance, owner):
        raw = instance[self.offset:(self.offset + self.width)]
        return self._container(raw)

    def __set__(self, instance, value):
        value_width = _size_in_bits(value)
        if value_width > self.width:
            raise ValueError(
                "{} does not fit in {} bits".format(value, self.width)
            )
        instance[self.offset:(self.offset + self.width)] = value


class BitFieldMeta(type):
    def __new__(cls, name, bases, dct):
        # Build both bitmask and supported methods
        fields = [
            key for key, value in dct.items() if hasattr(value, 'field')
        ]
        # Create bitmask
        total_bits = \
            max(map(lambda k: dct[k].offset + dct[k].width, fields), default=0)
        bitmask = '0' * total_bits
        for key in fields:
            field = dct[key]
            bitmask = \
                bitmask[:field.offset] +\
                '1' * field.width +\
                bitmask[field.offset+field.width:]

        # Reverse bitmask
        bitmask = bitmask[::-1]
        dct['bitmask'] = int(bitmask, base=2)
        dct['_fields'] = fields

        return type.__new__(cls, name, bases, dct)


class BitField(object):
    def __init__(self, value=0, size_in_bytes=None):
        self._raw = 0
        if not isinstance(value, int):
            raise TypeError("`value` must in `int`!")
        if size_in_bytes is None:
            self._size = _bytes_in_int(value)
        else:
            self._size = size_in_bytes
        self._total_bits = 8 * self._size

        self._assert_value(value)
        self._raw = value

    def _to_binary_string(self, value):
        bin_str = '{0:b}'.format(value).zfill(self._total_bits)
        # reverse so indexing will work OK
        return bin_str[::-1]

    def _assert_value(self, value):
        if value != value & self.bitmask:
            value_str = self._to_binary_string(value)
            bitmask_str = self._to_binary_string(self.bitmask)
            unmatching_bits = [
                i for
                i, (v, m) in
                enumerate(zip(value_str, bitmask_str)) if
                v == '1' and m == '0'
            ]
            raise ValueError(
                "Invalid assignment: bits {} must be 0!".format(unmatching_bits)
            )

    @property
    def size(self):
        return self._size

    @property
    def raw(self):
        # Using a python 2 and 3 compatible method
        return self._raw

    @raw.setter
    def raw(self, value):
        value_bytes = _bytes_in_int(value)
        max_bytes = self._total_bits // 8
        if value_bytes > max_bytes:
            raise ValueError(
                "Value too large ({} bytes). Should be {} bytes at max".format(
                    value_bytes,
                    max_bytes
                )
            )
        self._assert_value(value)
        self._raw = value

    @property
    def bytes(self):
        hex_value = '{0:x}'.format(self._raw).zfill(self._total_bits // 4)
        # must convert to big endian
        hex_value = "".join(textwrap.wrap(hex_value, 2)[::-1])
        return codecs.decode(hex_value, 'hex_codec')

    def __repr__(self):
        return '0x' + '{0:x}'.format(self.raw).zfill(self._total_bits // 4)

    def __str__(self):
        enabled = [
            field for field in self._fields if 0 != self.__getattribute__(field)
        ]
        return ",".join(enabled)

    def bin_str(self):
        return '0b' + self._to_binary_string(self._raw)[::-1]

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
        if max_size_in_bits < _size_in_bits(value):
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
        new_value = self._raw & mask
        # Add the value
        new_value += (value << start)
        self._assert_value(new_value)
        self._raw = new_value

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
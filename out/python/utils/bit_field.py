import codecs
import textwrap
from .bitmask import BitMask


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

        # Overload __str__ in case of integer
        def custom_str(instance, *args, **kwargs):
            return hex(instance)

        if self._type is int:
            methods['__str__'] = custom_str

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
            key for
            key, value in
            dct.items() if
            hasattr(value, 'field') and "reserved" not in key.lower()
        ]
        bitmask = BitMask(*tuple((dct[f].offset, dct[f].width) for f in fields))

        dct['bitmask'] = bitmask
        dct['_total_bits'] = bitmask.size
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

    def _assert_value(self, value):
        return self.bitmask.validate(value)

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

    def flags(self):
        enabled = [
            field for
            field in
            self._fields if
            0 != self.__getattribute__(field) and
            1 == self.__getattribute__(field).width
        ]
        return ",".join(enabled)

    def __str__(self):
        return "\n".join(
            ["[{} ({}:{})] {}".format(
                field,
                self.__getattribute__(field).offset,
                self.__getattribute__(field).offset +
                self.__getattribute__(field).width,
                self.__getattribute__(field)
            ) for field in self._fields]
        )

    def bin_str(self):
        return "0b" + "{0:b}".format(self._raw).zfill(self._total_bits)

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

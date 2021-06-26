from .ia32_bitmask import Ia32BitMask
from .ia32_byte_operations import *


class Ia32BitFieldMember(object):
    def __init__(self, name, description, offset, width, custom_type=None):
        # Create explicit attributes so that the metaclass will have access
        self.offset = offset
        self.width = width
        self.byte_offset = offset // 8
        # Round up
        self.byte_width = width // 8 + 1 * (0 != width % 8)
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
        methods['byte_width'] = self.byte_width
        methods['byte_offset'] = self.byte_offset
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
        value_width = size_in_bits(value)
        if value_width > self.width:
            raise ValueError(
                "{} does not fit in {} bits".format(value, self.width)
            )
        instance[self.offset:(self.offset + self.width)] = value


class Ia32BitFieldMeta(type):
    def __new__(cls, name, bases, dct):
        # Build both bitmask and supported methods
        fields = [
            key for
            key, value in
            dct.items() if
            hasattr(value, 'field') and "reserved" not in key.lower()
        ]
        bitmask = Ia32BitMask(*tuple((dct[f].offset, dct[f].width) for f in fields))

        dct['bitmask'] = bitmask
        dct['_total_bits'] = bitmask.size
        dct['_fields'] = fields

        return type.__new__(cls, name, bases, dct)


class Ia32BitField(object):
    def __init__(self, value=0, byte_offset=None, byte_width=None, max_bytes=None):
        if max_bytes is None:
            self._size = size_in_bytes(value)
        else:
            self._size = max_bytes

        self._bytes = b'\x00' * self._size
        self._total_bits = 8 * self._size

        if byte_offset is None:
            self._byte_offset = 0
        else:
            self._byte_offset = byte_offset

        if byte_width is None:
            self._byte_width = self._size
        else:
            self._byte_width = byte_width

        self._assert_value(value)
        self._bytes = to_bytes(value, self._byte_width)

    def _assert_value(self, value):
        return self.bitmask.validate(value)

    @property
    def size(self):
        return self._size

    @property
    def bytes(self):
        return self._bytes

    @property
    def raw(self):
        return self.bytes

    @bytes.setter
    def bytes(self, value):
        self._assert_value(value)
        self._bytes = to_bytes(value, self._byte_width)

    @raw.setter
    def raw(self, value):
        self.bytes = value

    @property
    def byte_offset(self):
        return self._byte_offset

    @property
    def byte_width(self):
        return self._byte_width

    def __repr__(self):
        return repr(self.bytes)

    def __int__(self):
        return bytes_to_int(self.bytes)

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
        if 0 == len(self._fields):
            return hex(int(self))

        return "\n".join(
            ["[{} ({}:{})] {}".format(
                field,
                self.__getattribute__(field).offset,
                self.__getattribute__(field).offset +
                self.__getattribute__(field).width,
                self.__getattribute__(field)
            ) for field in self._fields]
        )

    def bin(self):
        return "0b" + bin_str(self.bytes, self._total_bits)[::-1]

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
        if max_size_in_bits < size_in_bits(value):
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
        new_value = bytes_to_int(self._bytes) & mask
        # Add the value
        new_value += (value << start)
        self._assert_value(new_value)
        self._bytes = to_bytes(new_value, self._byte_width)

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
        raw = bytes_to_int(self._bytes) & mask
        # shift-right the remaining bits
        raw = raw >> start
        return raw

    def set(self, value):
        self.bytes = value

    def __get__(self, instance, owner):
        return self

    # For support inside struct
    def __set__(self, instance, value):
        self.bytes = value

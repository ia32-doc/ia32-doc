from .bitmask import BitMask
from .bit_field import BitFieldMember
from .byte_operations import *


class Struct(object):
    def __init__(self, value=0):
        if not isinstance(value, (int, str, bytes)):
            raise TypeError("argument must in int or bytes!")

        self._size = sum(
            self.__getattribute__(member).size for member in self._members
        )
        if size_in_bytes(value) > self._size:
            raise ValueError("value too large! Max size: {}".format(self._size))

        self._set_value(value)

    def _set_value(self, value):
        # TODO: add checks
        as_bytes = to_bytes(value, self._size)
        # Set each member
        for member in self._members:
            # NOTE: assuming that each field starts / end on
            # byte boundary
            member_bytes = as_bytes[
                self.__getattribute__(member).byte_offset:
                self.__getattribute__(member).byte_offset +
                self.__getattribute__(member).byte_width
            ]
            self.__getattribute__(member).set(member_bytes)

    @property
    def bytes(self):
        as_bytes = b''
        for member in self._members:
            as_bytes = as_bytes + \
                       to_bytes(
                           self.__getattribute__(member).bytes,
                           self.__getattribute__(member).byte_width,
                       )
        return as_bytes

    @bytes.setter
    def bytes(self, value):
        self._set_value(value)

    def __getitem__(self, item):
        return self.bytes[item]

    def __setitem__(self, item, value):
        if not (isinstance(item, slice) or isinstance(item, int)):
            raise TypeError("Slice not supported with type")

        if isinstance(item, slice):
            if item.step is not None:
                raise ValueError("Steps are not supported in structs!")
            start = item.start
            stop = item.stop

        if isinstance(item, int):
            start = item
            stop = item + 1

        new_value = \
            self.bytes[:start] +\
            to_bytes(value, stop - start) +\
            self.bytes[stop:]

        self._set_value(new_value)

    @property
    def size(self):
        return self._size

    @property
    def raw(self):
        return self.bytes

    @raw.setter
    def raw(self, value):
        self._set_value(value)

    def __int__(self):
        as_bytes = bytes_to_int(self.bytes)
        return as_bytes

    def __repr__(self):
        return repr(self.raw)

    def __str__(self):
        out_str = ""
        for member in self._members:
            out_str += member + ":\n"
            # Ident inner members
            out_str += \
                "".join(
                    "|--" + field + "\n" for
                    field in
                    str(self.__getattribute__(member)).splitlines()
                )
        return out_str


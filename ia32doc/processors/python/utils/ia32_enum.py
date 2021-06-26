from .ia32_byte_operations import to_bytes


class Ia32EnumField(object):
    def __init__(self, name, value, description):
        # Value must be convertible to int
        self._value = int(value)
        self._name = name
        self._description = description
        self._field = True
        self.__doc__ = self._description

    @property
    def value(self):
        return self._value

    def __str__(self):
        return "{} ({})".format(self._name, hex(self.value))

    def __repr__(self):
        return str(self)

    def __get__(self, instance, owner):
        return self

    def __set__(self, instance, value):
        raise AttributeError("Cannot set enum field!")

    def __int__(self):
        return self.value


class Ia32EnumMeta(type):
    def __new__(cls, name, bases, dct):
        fields = [
            value for
            _, value in
            dct.items() if
            hasattr(value, '_field')
        ]
        # Figure out the byte width
        byte_width = max(
            len(to_bytes(field, 0)) for
            field in
            fields
        ) if fields else 0

        dct['fields'] = fields
        dct['size'] = byte_width

        return type.__new__(cls, name, bases, dct)


class Ia32Enum(object):
    def __init__(self, value):
        self._set(value)

    def _set(self, value):
        for field in self.fields:
            # Check if it is a class assignment
            if value in self.fields:
                self._field = field
                return
            if value == field.value:
                self._field = field
                return
        raise ValueError("No field with value: {}".format(value))

    @property
    def value(self):
        return self._field

    @value.setter
    def value(self, new_value):
        self._set(new_value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.__class__.__name__) + "::" + str(self)

    def __get__(self, instance, owner):
        return self._field

    def __set__(self, instance, value):
        self._set(value)

    def __int__(self):
        return int(self.value)

    @property
    def bytes(self):
        return to_bytes(self._field.value, self.size)

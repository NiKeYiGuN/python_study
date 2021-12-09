# type: ignore
null = object()
a = 257


class Member:
    def __init__(self, name, clsname, offset):
        self.name = name
        self.clsname = clsname
        self.offset = offset

    def __get__(self, obj, objtype=None):
        value = obj._slotvalues[self.offset]
        if value is null:
            raise AttributeError(self.name)
        return value

    def __set__(self, obj, value):
        obj._slotvalues[self.offset] = value

    def __delete__(self, obj):
        value = obj._slotvalues[self.offset]
        if value is null:
            raise AttributeError(self.name)
        obj._slotvalues[self.offset] = null

    def __repr__(self):
        return f"<Member {self.name!r} of {self.clsname!r}>"


class Type(type):
    def __new__(mcls, clsname, bases, mapping):
        slot_names = mapping.get("slot_names", [])
        for offset, name in enumerate(slot_names):
            mapping[name] = Member(name, clsname, offset)
        return type.__new__(mcls, clsname, bases, mapping)


class Object:
    def __new__(cls, *args):
        inst = super().__new__(cls)
        if hasattr(cls, "slot_names"):
            empty_slots = [null] * len(cls.slot_names)
            object.__setattr__(inst, "_slotvalues", empty_slots)
        return inst

    def __setattr__(self, name, value):
        cls = type(self)
        if hasattr(cls, "slot_names") and name not in cls.slot_names:
            raise AttributeError(f"{type(self).__name__!r} object has no attribute {name!r}")
        super().__setattr__(name, value)

    def __delattr__(self, name):
        cls = type(self)
        if hasattr(cls, "slot_names") and name not in cls.slot_names:
            raise AttributeError(f"{type(self).__name__!r} object has no attribute {name!r}")
        super().__delattr__(name)


class H(Object, metaclass=Type):
    "Instance variables stored in slots"

    slot_names = ["x", "y"]

    def __init__(self, x, y):
        self.x = x
        self.y = y

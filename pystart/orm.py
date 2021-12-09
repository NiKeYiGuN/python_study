# type: ignore
from functools import reduce
from typing import Iterable


class Field(object):
    def __init__(self, column_type, max_length, **kwargs) -> None:
        self.column_type = column_type
        self.max_length = max_length
        self.default = None
        if kwargs:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    def __str__(self) -> str:
        return "<%s>" % (self.__class__.__name__)


class StringField(Field):
    def __init__(self, max_length, **kwargs) -> None:
        super().__init__(
            column_type=f"varchar({max_length})", max_length=max_length, **kwargs
        )


class IntegerField(Field):
    def __init__(self, **kwargs) -> None:
        super().__init__(column_type="bigint", max_length=8, **kwargs)


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == "Model":
            return type.__new__(cls, name, bases, attrs)

        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v

        for k in mappings.keys():
            attrs.pop(k)

        attrs["__mappings__"] = mappings
        attrs["__table__"] = attrs.get("Meta").table or name
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, item):
        if item == "save":
            self.save()
        try:
            return self[item]
        except:
            raise AttributeError(rf"Model 对象没有{item}属性")

    def __setattr__(self, key, value) -> None:
        self[key] = value

    def save(self):
        fields = []
        params = []

        for k, v in self.__mappings__.items():
            fields.append(k)
            params.append(getattr(self, k, v.default))

        sql = f"insert into {self.__table__} ({self.join(fields)}) values ({self.join(params)})"
        print(sql)

    def join(self, attrs, pattern=","):
        return reduce(lambda x, y: f"{x}{pattern}{y}", attrs)


if __name__ == "__main__":
    # 定义一个类，对应数据库中的一张表
    class User(Model):
        # 表名
        class Meta:
            table = "users"
            # 创建bigint型字段

        id = IntegerField()
        # 创建varchar型字段
        name = StringField(max_length=50)
        email = StringField(max_length=50, default="ayuliao@xx.com")
        password = StringField(max_length=50)

    u = User(id=456, name="ayuliao", email="123", password="123456")
    u.save()

    # nums = [1, 2, 3, 4, 5]
    #
    # list_itertor = reversed(nums)
    #
    # # print(list_itertor.__next__())
    # # print(list_itertor.__next__())
    # # print(list_itertor.__next__())
    # # print(list_itertor.__next__())
    # # print(list_itertor.__next__())
    #
    # for i in list_itertor:
    #     print(i)

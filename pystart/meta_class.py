# type: ignore


class Zinc:
    hello = "hello zinc"


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs["ayuliao"] = lambda self, value: self.append(value)
        attrs["author"] = "ayuliao"
        return type.__new__(cls, name, bases, attrs)


class Mylist(list, metaclass=ListMetaclass):
    ...


class Animal(object):
    def eat(self):
        print("吃东西像[Animal]")

    def move(self):
        print("运动像[Animal]")


class Dog(Animal):
    def eat(self):
        print("吃东西像[dog]")

    def move(self):
        print("运动像[dog]")


class Bird(Animal):
    def eat(self):
        print("吃东西像[Bird]")

    def move(self):
        print("运动像[Bird]")


class AnimalMetaclass(type):
    def __new__(cls, *args, **kwargs):
        name, bases, attr = args[:3]
        dog, bird = bases

        def eat(self):
            dog.eat(self)

        def move(self):
            bird.move(self)

        attr["eat"] = eat
        attr["move"] = move

        return type(name, bases, attr)


class NewAnimal(Dog, Bird, metaclass=AnimalMetaclass):
    ...


if __name__ == "__main__":
    a = Zinc()
    print(a.hello)
    print(Zinc.hello)

    ZINC = type("ZINC", (object,), {"hello": "hello my love"})

    print("-------------------------------")
    print(a.__class__)
    print(ZINC.__class__)
    print(type.__class__)
    print("-------------------------------")

    L = Mylist()
    # L.ayuliao(123)
    # L.ayuliao(345)
    # print(L)
    # print(L.author)

    na = NewAnimal()
    na.eat()
    na.move()

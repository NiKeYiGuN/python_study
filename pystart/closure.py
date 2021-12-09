if __name__ == "__main__":
    # a = 1
    # print(a)
    # a = 2
    # print(a)
    # a += 1
    # print(a)

    class A:
        def b(self):
            print(self, 1 + 1)

    a = A()
    a.b()
    print(a)

# type: ignore
def generator(n):
    for item in range(n):
        yield item + 1


def non_generator(n):
    res = []
    for j in range(n):
        res.append(j + 1)
    return res


def Fib(prev, curr, n):
    while curr < n:
        yield curr
        prev, curr = curr, prev + curr


if __name__ == "__main__":
    for i in generator(5):
        print(i)
    print(type(non_generator(5)))
    print(type(generator(5)))

    a = generator(5)
    print(next(a))
    print(next(a))
    print("使用for迭代")
    for i in a:
        print(i)

    print("再次使用for迭代")
    for i in a:
        print(i)

    for f in Fib(0, 1, 20):
        print(f)

    g = (i + 1 for i in range(5))
    print(type(g))

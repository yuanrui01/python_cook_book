def num():
    return 1, 2, 3


def spam(a, b=[]):
    b.append(a)
    print(b)


spam(1)
spam(2)
spam(3)

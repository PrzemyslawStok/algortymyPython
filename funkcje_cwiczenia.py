import timeit
from random import random

import numpy as np
from numba import jit

import tensorflow as tf


def tuple_list():
    A = [1, 2, 3, 4, 5]
    print(A)

    B = (1, 2, 3, 4, 5)
    print(B)

    for b in B:
        print(b)

    B1 = list(B)
    print(B1)

    B1[2] = 100

    print(B1)

    B2 = tuple(B1)
    print(B2)


def f0():
    return 10, (1, 2)


def parametry0():
    print(f0())

    # tuple_list()

    a, b = f0()
    print(f"a={a}, b={b}")

    a, _ = f0()
    print(f"a={a}")

    a, (b, c) = f0()
    print(f"a={a}, b={b}, c={c}")


def f1():
    return (10, 2), (7, 3)


def f2():
    return (1, 7, (10, 2, (5, "zm")), (5, 1))


def parametry1():
    print(f1())
    (_, b), (c, _) = f1()
    print(f"b={b}, c={c}")

    print(f2())

    (_, _, (_, _, (_, a)), (_, _)) = f2()
    print(a)

    (_, _, (_, _, (_, a)), b) = f2()
    print(b[1])


def f_arg(a, a1, *args):
    print(f"a={a}")
    print(f"a1={a1}")
    for a in args:
        print(a)


def f_kwargs(**kwargs):
    for value, key in kwargs.items():
        print(f"{value}={key}")


def dict1() -> 0:
    d0 = {"a2": 100}
    d0["a1"] = 10
    d0[0] = 100
    d0["0"] = "1000"

    print(d0["a1"])
    print(d0["0"])
    d0["b"] = (10, 2)

    print(d0)

    for item in d0.items():
        print(item)

    for key in d0.keys():
        print(key)

    for value in d0.values():
        print(value)

    for key, value in d0.items():
        print(f"klucz: {key}, wartość: {value}")

    return 0


def cw1():
    d1 = {}
    for i in range(10):
        d1[f"i{i}"] = np.random.randint(0, 10)

    print(d1)

    sum = 0

    for value in d1.values():
        v = int(value)
        print(f"{v}^3={v ** 3}")
        sum += v ** 3

    return sum


def f3():
    A = []
    for i in range(10):
        A.append((tuple(np.random.randint(0, 10, 3)), 1, 2))

    print(A)

    for (a1, a2, _), b, c in A:
        print(f"[a1={a1} b={b} c={c}]")


def cw2() -> ((int, int), (int, int, int)):
    return (1, 2), (5, 6, 7)


if __name__ == "__main__":
    # tuple_list()
    # parametry0()

    # parametry1()

    # f_arg(1, 2, 3, 4, 5, 6, 7)
    # f_kwargs(a=10, b=2, l=[1, 2, 3, 4, 5])

    # dict1()
    # print(f"suma sześcianów = {cw1()}")
    f3()

    a = cw2()

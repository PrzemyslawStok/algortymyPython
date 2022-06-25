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
    for value, key in kwargs:
        print(f"({value},{key})")


if __name__ == "__main__":
    # tuple_list()
    # parametry0()

    # parametry1()

    f_arg(1, 2, 3, 4, 5, 6, 7)



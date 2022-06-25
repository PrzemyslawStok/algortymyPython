import timeit
from random import random

import numpy as np
from numba import jit

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
    return 10, 1


if __name__ == "__main__":
    print(f0())

    tuple_list()



import timeit
from random import random

import numpy as np


def f0(l):
    for i in range(1000_000):
        a = i * i
    return 0.0


def obliczenia(l=100_000):
    A = []
    for i in range(l):
        A.append(random())

    suma = 0
    for i in range(len(A)):
        suma += A[i]


def obliczenia_numpy(l=100_000):
    A = np.empty(l, dtype=float)


def zmierz_czas(f, l=100_000):
    start = timeit.default_timer()
    f(l)
    end = timeit.default_timer()
    t = end - start
    print(f"czas działania: {t:0.5f}")


if __name__ == "__main__":
    l = 100_000
    zmierz_czas(obliczenia, l)
    zmierz_czas(obliczenia_numpy, l)

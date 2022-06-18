import timeit
from random import random

import numpy as np
from numpy import ndarray


def f0(l):
    for i in range(1000_000):
        a = i * i
    return 0.0


def obliczenia(l=100_000) -> float:
    A = []
    for i in range(l):
        A.append(random())

    suma = 0
    for i in range(len(A)):
        suma += A[i]

    return suma


def obliczenia_numpy(l=100_000) -> ndarray:
    A = np.random.random(l)
    b = np.sum(A)

    return b


def obliczenia_numpy_petle(l=100_000) -> ndarray:
    A = np.empty(l, dtype=float)
    for i in range(l):
        pass

    b = np.sum(A)

    return b


def zmierz_czas(f, l=100_000):
    start = timeit.default_timer()
    f(l)
    end = timeit.default_timer()
    t = end - start
    print(f"czas działania: {t:0.5f}s")


if __name__ == "__main__":
    l = 100_000
    zmierz_czas(obliczenia, l)
    zmierz_czas(obliczenia_numpy, l)
    zmierz_czas(obliczenia_numpy_petle, l)

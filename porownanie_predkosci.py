import timeit
from random import random

import numpy as np
from numba import jit


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


@jit
def obliczenia_numba(l=100_000) -> float:
    A = []
    for i in range(l):
        A.append(random())

    suma = 0
    for i in range(len(A)):
        suma += A[i]

    return suma


def obliczenia_numpy(l=100_000) -> np.ndarray:
    A = np.random.random(l)
    b = np.sum(A)

    return b


def obliczenia_numpy_petle(l=100_000) -> float:
    A = np.empty(l, dtype=float)
    for i in range(l):
        A[i] = np.random.random()

    suma = 0
    for i in range(len(A)):
        suma += A[i]

    return suma


def zmierz_czas(f, l=100_000, str=""):
    start = timeit.default_timer()
    f(l)
    end = timeit.default_timer()
    t = end - start
    print(f"czas działania ({str}): {t:0.5f}s")


if __name__ == "__main__":
    l = 100_000
    zmierz_czas(obliczenia, l)
    zmierz_czas(obliczenia_numpy, l)
    zmierz_czas(obliczenia_numpy_petle, l)
    zmierz_czas(obliczenia_numba, l)
    zmierz_czas(obliczenia_numba, l)

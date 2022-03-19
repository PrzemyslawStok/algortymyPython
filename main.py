import numpy as np
import timeit
from numba import jit

from matplotlib import pyplot as plot


def multiply_arrays(a: np.array, b: np.array):
    c = []
    for i in range(len(a)):
        c.append(a[i] * b[i])

    return c


def calc(a: np.array, b: np.array):
    print(f"{a}+{b}={a + b}")
    print(f"{a}-{b}={a - b}")
    print(f"{a}*{b}={a * b}")
    print(f"{a}/{b}={a / b}")


if __name__ == "__main__":
    a = 10.0 * np.ones([10_000_000], dtype=np.float64)
    b = 7 * np.ones([10_000_000], dtype=np.float64)

    start = timeit.default_timer()
    _ = a * b
    end = timeit.default_timer()

    print(f"numpy time: {(end - start):0.5f}s")

    start = timeit.default_timer()
    multiply_arrays(a, b)
    end = timeit.default_timer()

    print(f"list time: {(end - start):0.5f}s")

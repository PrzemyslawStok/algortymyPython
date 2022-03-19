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


def fun1():
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


def simplePlot():
    x = np.linspace(0, 10, 100)
    y = x / np.sin(x)

    plot.xlabel("x")
    plot.ylabel(r"$y=\frac{x}{sin(x)}$")
    plot.plot(x, y, 'orange')
    plot.show()


def plot1():
    # y = a*x^2+bx=c
    # a należy do (0,10)
    a = 1
    b = 0
    c = 0

    plot.xlabel("x")
    plot.ylabel(r"$y=ax^2+bx+c$")

    x = np.linspace(-10, 10, 100)
    y = a * x ** 2 + b * x + c

    plot.plot(x, y)
    plot.show()


if __name__ == "__main__":
    # fun1()
    simplePlot()
    plot1()

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
    b = 0.1
    c = 0.1

    plot.xlabel("x")
    plot.ylabel(r"$y=ax^2+bx+c$")

    x = np.linspace(-10, 10, 100)

    for a in range(1, 10):
        y = a * x ** 2 + a * x + c
        plot.plot(x, y, label=rf"$y={a}x^2+{b}x+{c}$")

    plot.legend()
    plot.show()


def plot2():
    # y = a*sin(b*x)+c
    # a należy do (0.1,5) - 10 przykładów
    a = 1
    b = 2.0
    c = 0.1

    a_space = np.linspace(0.1, 5, 10)
    x = np.linspace(-10, 10, 1000)

    for a in a_space:
        y = a * np.sin(b * x) + a
        c = a
        plot.plot(x, y, label=rf"$y={a:0.1f}sin({b}x)+{c:0.1f}$")

    plot.legend()
    plot.show()


def f1(x):
    print(x)
    return x ** 2 + 1


def simple_map():
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    b = map(f1, a)
    print(list(b))

    f2 = lambda x: x ** 3
    print(f2(3))

    b = map(lambda x: x + 1, a)
    print(list(b))

    nazwiska = map(lambda x: f"Przemysław Stokłosa {x}", a)
    print(list(nazwiska))


def f2(n: int):
    return lambda x: n * x

def map1():
    f2_1 = f2(1)
    f2_2 = f2(2)

    print(f2_1(1))
    print(f2_2(1))

    a = []

    for n in range(1, 10):
        a.append(f2(n))

    print(a)


def map_numpy():
    a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    # print(a * a)
    np.vectorize(f1)
    print(f1(a))


if __name__ == "__main__":
    # fun1()
    # simplePlot()
    # plot1()
    plot2()

    # simple_map()
    # map_numpy()

    map1()

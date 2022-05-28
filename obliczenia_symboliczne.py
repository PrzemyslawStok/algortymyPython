from matplotlib import pyplot as plot
import numpy as np

import sympy as sp
from sympy import pprint


def calki():
    sp.init_printing(use_unicode=True)
    x = sp.symbols("x")
    y = (x + 1) ** 5
    pprint(y)
    pprint(sp.expand(y))

    int1 = sp.integrate(x ** 2, x)
    int2 = sp.integrate((sp.sin(x) + 1) ** 10, x)

    pprint(int2)


def przyspieszenie(x_t: sp.core.Add) -> (sp.core.Add, sp.core.Add):
    v_t = sp.diff(x_t, t)
    a_t = sp.diff(v_t, t)

    return v_t, a_t


if __name__ == "__main__":
    t = sp.symbols("t")
    x_t = t ** 2 + 2 * t + 2

    v_t, a_t = przyspieszenie(x_t)
    pprint(v_t)
    pprint(a_t)

    x_t_f = sp.lambdify(t, x_t, "numpy")

    X = np.linspace(0, 10, 100)
    Y = x_t_f(X)

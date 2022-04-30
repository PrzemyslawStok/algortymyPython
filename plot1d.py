from matplotlib import pyplot as plot
import numpy as np


def wykres1():
    X = np.linspace(0, 5, 100)
    Y = X

    Y1 = [int(x) for x in X]
    Y2 = np.round(X)
    Y3 = np.ceil(X)

    plot.plot(X, Y, label=rf"$y=x$")
    plot.plot(X, Y1, label=rf"$y=int(x)$")
    plot.plot(X, Y2, label=rf"$y=round(x)$")
    plot.plot(X, Y3, label=rf"$y=ceil(x)$")

    plot.legend()
    plot.show()


def wykres2():
    t = np.linspace(0, np.pi, 100)

    X = np.sin(t)
    Y = np.cos(t)

    plot.plot(X, Y)
    plot.show()


def wykres3(plot_range: np.ndarray):
    for range in plot_range:
        t_max = 0.2 * range * np.pi
        a = 0.5 * range

        t = np.linspace(0, t_max, 1000)

        r = a * t

        X = r * np.sin(t)
        Y = r * np.cos(t)

        plot.plot(X, Y)

    plot.show()


if __name__ == "__main__":
    # wykres1()
    wykres3(np.arange(1, 10))

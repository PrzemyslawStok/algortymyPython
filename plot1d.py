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


def wykres4():
    t = np.linspace(0, 100 * np.pi, 1000)

    X = np.sin(t)
    Y = np.cos(2 * t)

    plot.plot(X, Y)
    plot.show()


def wykres5(d=np.pi / 2.0, A=1.0, B=1.0, a=1, b=2):
    t = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

    X = A * np.sin(a * t + d)
    Y = B * np.sin(b * t)

    plot.plot(X, Y)
    # plot.show()


def sin_matrix(A: np.ndarray):
    X = np.linspace(-np.pi, np.pi, 100)

    for a in A:
        Y = a * np.sin(a * X)
        plot.plot(X, Y)

    # plot.show()
    plot.savefig("sin.png")


def sin_multiplot(A: np.ndarray):
    fig = plot.figure(figsize=(5 * len(A), 5), dpi=100)
    grid_spec = fig.add_gridspec(1, len(A))
    subplots = grid_spec.subplots()

    for i in range(len(A)):
        X = np.linspace(-np.pi, np.pi, 100)
        Y = np.sin(A[i] * X)

        subplots[i].plot(X, Y)

    plot.savefig("multiplot.png")


if __name__ == "__main__":
    # wykres1()
    # wykres3(np.arange(1, 10))
    # wykres4()
    # wykres5(a=5, b=6)

    # sin_matrix(np.array([1, 2, 3, 4, 5]))
    sin_multiplot(np.array([1, 2, 3, 4, 5]))

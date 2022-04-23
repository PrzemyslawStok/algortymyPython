from matplotlib import pyplot as plot
import numpy as np

if __name__ == "__main__":
    X = np.linspace(0, 5, 100)
    Y = X

    # int(x)
    # round(x)
    # ceil(x)
    Y1 = [int(x) for x in X]
    Y2 = np.round(X)
    Y3 = np.ceil(X)

    plot.plot(X, Y, label=rf"$y=x$")
    plot.plot(X, Y1, label=rf"$y=int(x)$")
    plot.plot(X, Y2, label=rf"$y=round(x)$")
    plot.plot(X, Y3, label=rf"$y=ceil(x)$")

    plot.legend()
    plot.show()

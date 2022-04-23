from matplotlib import pyplot as plot
import numpy as np

if __name__ == "__main__":
    X = np.linspace(0, 10, 100)
    Y = X

    # int(x)
    # round(x)
    # ceil(x)
    Y1 = [np.int(x) for x in X]

    plot.plot(X, Y, label=rf"$y=x$")
    plot.plot(X, Y1, label=rf"$y=int(x)$")
    plot.legend()
    plot.show()

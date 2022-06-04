from matplotlib import pyplot as plot
import numpy as np

if __name__ == "__main__":
    X = np.linspace(0, 2 * np.pi)
    Y = np.sin(X)

    plot.plot(X, Y)
    plot.show()

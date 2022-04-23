from matplotlib import pyplot as plot
import numpy as np

if __name__ == "__main__":
    x = np.linspace(0, 10, 100)
    y = x * x

    plot.plot(x, y)
    plot.show()

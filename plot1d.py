from matplotlib import pyplot as plot
import numpy as np

if __name__ == "__main__":
    x = np.linspace(0, 10, 100)
    y = x * x

    # int(x)
    # round(x)
    # ceil(x)

    plot.plot(x, y, label=rf"$y=x^2$")
    plot.legend()
    plot.show()

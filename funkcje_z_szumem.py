from matplotlib import pyplot as plot
import numpy as np
import tensorflow as tf


def data():
    X = np.linspace(0, 2 * np.pi, 100)
    Y = np.sin(X)

    noise_lvl = 0.1
    noise = np.random.normal(0.0, noise_lvl, size=np.shape(X))
    Y_noise = Y + noise
    return X, Y, Y_noise


if __name__ == "__main__":
    X, Y_f, Y_noise = data()

    plot.plot(0, 0)
    plot.plot(X, Y_f, label="$y=sin(x)$")
    plot.scatter(X, Y_noise, label="$y=sin(x)$" + "z szumem")

    plot.legend()
    plot.show()

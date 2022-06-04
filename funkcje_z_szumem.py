from matplotlib import pyplot as plot
import numpy as np
import tensorflow as tf


def data(n: int = 100):
    X = np.linspace(0, 2 * np.pi, n)
    Y = np.sin(X)

    noise_lvl = 0.1
    noise = np.random.normal(0.0, noise_lvl, size=np.shape(X))
    Y_noise = Y + noise
    return X, Y, Y_noise


if __name__ == "__main__":
    X, Y_f, Y_noise = data(2)

    plot.plot(0, 0)
    plot.plot(X, Y_f, label="$y=sin(x)$")
    plot.scatter(X, Y_noise, label="$y=sin(x)$" + "z szumem")

    plot.legend()
    plot.show()

    model = tf.keras.Sequential()

    model.add(tf.keras.layers.InputLayer(input_shape=np.shape(X)))
    model.add(tf.keras.layers.Dense(5))
    model.add(tf.keras.layers.Dense(1))

    model.summary()



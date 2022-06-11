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


def createModel() -> tf.keras.Model:
    model = tf.keras.Sequential()

    model.add(tf.keras.layers.InputLayer(input_shape=(1,)))

    model.add(tf.keras.layers.Dense(50, activation='tanh'))
    model.add(tf.keras.layers.Dense(20, activation='tanh'))
    model.add(tf.keras.layers.Dense(1, activation='linear'))

    model.summary()

    model.compile(optimizer="adam", loss='mean_squared_error')
    return model


def createModel1() -> tf.keras.Model:
    model = tf.keras.Sequential()

    model.add(tf.keras.layers.InputLayer(input_shape=(1,)))

    for i in range(5):
        model.add(tf.keras.layers.Dense(5))

    model.add(tf.keras.layers.Dense(20, activation='tanh'))
    model.add(tf.keras.layers.Dense(2))
    model.add(tf.keras.layers.Dense(1, activation='linear'))

    model.summary()

    model.compile(optimizer="adam", loss='mean_squared_error')
    return model


def fun_model():
    X, Y_f, Y_noise = data(1000)

    plot.plot(0, 0)
    # plot.plot(X, Y_f, label="$y=sin(x)$")
    plot.scatter(X, Y_noise, label="$y=sin(x)$" + "z szumem")

    # model = createModel()
    model = createModel1()
    plot.plot(X, np.squeeze(model(X)), label="przed treningiem")

    model.fit(X, Y_noise, epochs=100, batch_size=10)

    plot.plot(X, np.squeeze(model(X)), label="po treningu")

    # print(model(X))

    plot.legend()
    plot.show()


def imagesData() -> (np.ndarray, np.ndarray):
    mnist = tf.keras.datasets.mnist
    (X, Y), (_, _) = mnist.load_data()
    return X / 255.0, Y


if __name__ == "__main__":
    # fun_model()
    X, Y = imagesData()
    plot.imshow(X[1])
    plot.show()

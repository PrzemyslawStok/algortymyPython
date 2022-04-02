import numpy as np
import timeit


def macierze1():
    A = np.array([[1, 2, 0], [0, 1, 1], [1, 10, 1]])
    print(A)

    print(A[1])
    print(A[2, 1])

    print(np.eye(5))

    for i in range(len(A)):
        A[i] = 5

    print(A)


if __name__ == "__main__":
    macierze1()

import numpy as np
import timeit


def macierze1():
    A = np.array([[1, 2, 0], [0, 1, 1], [1, 10, 1]])
    print(A)

    print(A[1])
    print(A[2, 1])

    print(np.eye(5))

    for i in range(len(A)):
        A[i, i] = 5

    print(A)


def macierze2():
    A = np.eye(5)
    print(A)

    print(np.ones([10, 2]))
    print(np.zeros([5, 3]))

    print(5 * np.ones([10, 2]))

    B = np.zeros([5, 3])
    print(B)

    print(B.fill(2))
    print(B)

    print(np.diag([1, 3, 4, 7, 1]))


def macierze3():
    A = np.arange(1, 10)
    print(A)

    A = np.arange(1, 10, 2)
    print(A)

    A = np.arange(0, 100)
    B = A.reshape([10, -1])

    C = B * B

    print(C)

    for i in range(len(C)):
        C[i, i] = 0

    print(C)

    print(np.flip(C, axis=0))


if __name__ == "__main__":
    # macierze1()
    # macierze2()
    macierze3()

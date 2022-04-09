import numpy as np


def funkcja1():
    A = np.arange(0, 10) + 5
    print(A)

    # print(A[2])

    B = []
    for i in range(2, 9):
        B.append(A[i])

    print(B)

    B = [A[i] for i in range(2, 9)]
    print(B)

    print(list(A[2:9]))
    print(list(A[:8]))
    print(A[5:-2])


def funkcja2():
    A = np.arange(0, 100).reshape([10, -1])
    print(A)
    print("")

    print(A[2, :])
    print(A[2:5, :])
    print("")

    print(A[:, 2:5])
    print("")

    # zad 12-77
    print(A[:, 2:])

    # zad 35-89
    # zad 25-79


if __name__ == "__main__":
    # funkcja1()
    funkcja2()

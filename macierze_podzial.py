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


def funkcja2():
    A = np.arange(0, 100).reshape([10, -1])
    print(A)


if __name__ == "__main__":
    funkcja1()

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

    B = A[:, :1]
    print(B.reshape([-1]))

    A = ["x1", "x2"]
    print(A)

    X = np.arange(0, 100)
    print(X)

    print(np.array([f"x_{i}" for i in X]).reshape([10, -1]))


def funkcja3():
    A = np.arange(1, 10)
    print(A)

    a = 2

    print(A[:a])
    print(A[a:])

    print(np.concatenate((A[:a], A[a:])))


def podzial1(A: np.ndarray, a=90) -> (np.ndarray, np.ndarray):
    print(f"len(A)={len(A)}")

    print(f"shape(A)={np.shape(A)}")
    split = int(np.shape(A)[0] * a / 100)
    B = A[:split]
    C = A[split:]

    return B, C


if __name__ == "__main__":
    # funkcja1()
    # funkcja2()

    # funkcja3()
    A1, A2 = podzial1(np.arange(0, 11), 40)
    print(A1, A2)

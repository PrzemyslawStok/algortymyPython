import timeit


def f0():
    for i in range(1000_000):
        a = i * i
    return 0.0


def zmierz_czas(f):
    start = timeit.default_timer()
    f()
    end = timeit.default_timer()
    t = end - start
    print(f"czas działania: {t:0.5f}")


if __name__ == "__main__":
    zmierz_czas(f0)

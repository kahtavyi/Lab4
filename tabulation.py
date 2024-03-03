import math
from matplotlib import pyplot as plt

def f(x: list[float], N: int) -> list[float]:

#Calculate function values for passed array of arguments

    return [ math.sin(math.pi * x_i * N) for x_i in x ]

def tabulate(a: float, b: float, n: int, N: int) -> tuple[list[float], list[float]]:
    x = [a + x * (b - a) / n for x in range(n)]
    y = f(x, N)
    return x, y

def main():
    N = 13
    res = tabulate(0, 1, 1000, N)

    plt.plot(res[0], res[1])
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
import numpy as np
import matplotlib.pyplot as plt


myalpha = np.array([0, 0.1, 1, 3, 5, 10])
U = np.arange(0, 10, 0.1)
U = U[U != 0]


def t(e, alpha):
    return 1 + alpha * np.exp(-e)


def myfunc(e, u):
    return t(e, alpha)/np.sqrt(u-e)


for alpha in myalpha:
    x = np.zeros_like(U)

    i = 0
    devide = 8192

    while i < len(x):
        h = np.linspace(0, U[i], num=devide)
        h = h[h != 0]
        h = h[h != U[i]]
        x[i] = (sum(myfunc(h, U[i] * np.ones_like(h))) - 0.5 * (myfunc(h[0], U[i]) - myfunc(h[-1], U[i]))) * U[
            i] / devide
        i += 1
    plt.plot(x, U)
plt.show()

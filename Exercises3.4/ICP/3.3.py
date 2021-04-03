import numpy as np


n = 5
myh = 0.001
myx = 1


def myfunc(x):
    return np.sin(x)


def delta(x, h):
    return (myfunc(x+h)-myfunc(x-h))/2/h


def gamma(k, l, h, x):
    if l == 0:
        return delta(x, h/(2 ** k))
    else:
        return 4 ** l * gamma(k, l - 1, myh, myx) / (4 ** l - 1) - gamma(k - 1, l - 1, myh, myx) / (4 ** l - 1)


print(gamma(5, 5, myh, myx))

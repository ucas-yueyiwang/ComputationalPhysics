import numpy as np

myx = 1
myh = 0.001


def myfunc(x):
    return np.exp(-x) * np.log(x)


def delta(x, h):
    return (myfunc(x+h)-2 * myfunc(x) + myfunc(x-h))/h/h


def secondorder(x, h):
    return (4*delta(x, h/2)-delta(x, h))/3


print(secondorder(myx, myh))

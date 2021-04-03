import numpy as np
import matplotlib.pyplot as plt


def myfunc(x):
    return x*np.exp(x)


harray = np.linspace(1, 0.0001, 99)
xarray = 2 * np.ones_like(np.shape(harray))
# print(harray)
forward = (myfunc(xarray + harray) - myfunc(xarray)) / harray
backward = (myfunc(xarray) - myfunc(xarray-harray)) / harray
central = 0.5 * (myfunc(xarray + harray) - myfunc(xarray-harray)) / harray
# print(forward, backward, central)
plt.plot(harray, central)
plt.plot(harray, forward)
plt.plot(harray, backward)
plt.show()

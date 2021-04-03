import numpy as np
import matplotlib.pyplot as plt
maxX = np.pi * np.array([1/256, 1/128, 1/64, 1/32, 1/16, 1/8, 1/4, 3/8, 7/16, 15/32, 1/2])


def myfunc(x, x0):
    return 0.5 * np.sqrt((1+3 * (np.cos(x))**2)/(np.sin(x0)-np.sin(x))/3)


time = np.zeros_like(maxX)
i = 0
devide = 8192

while i < len(maxX):
    h = np.linspace(0, maxX[i], num=devide)
    h = h[h != maxX[i]]
   # print(h)
   # print(sum(myfunc(h, maxX[i] * np.ones_like(h))))
   # print(0.5 * (myfunc(h[0], maxX[i])))
   # print(myfunc(h[-1], maxX[i]))
    time[i] = (sum(myfunc(h, maxX[i] * np.ones_like(h))) - 0.5 * (myfunc(h[0], maxX[i]) - myfunc(h[-1], maxX[i]))) * maxX[i] / devide
    i += 1
print(time)
mypi = 2 * np.pi * np.ones_like(time)
plt.plot(maxX, time)
plt.show()

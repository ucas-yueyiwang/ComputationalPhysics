from MD.force import calc_force
import numpy as np
import time

delta = 0.00001
x = np.array([[1.0132226417,        0.3329955686,        0.1812866397],
          [0.7255989775,       -0.7660449415,        0.2388625373],
          [0.7293356067,       -0.2309436666,       -0.7649239428],
          [0.3513618941,        0.8291166557,       -0.5995702064],
          [0.3453146118,       -0.0366957540,        1.0245903005],
          [0.1140240770,        0.9491685999,        0.5064104273],
          [-1.0132240213,      -0.3329960305,       -0.1812867552],
          [-0.1140234764,      -0.9491689127,       -0.5064103454],
          [-0.3513615244,      -0.8291170821,        0.5995701458],
          [-0.3453152548,       0.0366956843,       -1.0245902691],
          [-0.7255983925,       0.7660457628,       -0.2388624662],
          [-0.7293359733,       0.2309438428,        0.7649237858],
          [0.0000008339,        0.0000002733,        0.0000001488]])
# x = 20 * np.random.rand(50, 3)
dxarray = delta * np.eye(x.size)
# print(dx)
i = 0
force = np.zeros_like(dxarray[1])
deltaarray = delta * np.ones_like(dxarray[1])
iarray = np.arange(x.size)
time_start = time.time()
for (i, dx, delt) in zip(iarray, dxarray, deltaarray):
    force[i] = calc_force(x, dx, delt)
time_end = time.time()
print('time cost', time_end-time_start, 's')
print(np.reshape(force,(-1,3)))

# use numpy to generate a n^2*n^2 diag matrix and reshape it. than use a n*n*n*n to vectorize it.

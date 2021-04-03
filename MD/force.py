import numpy as np
from MD.ljpotential import lennard_jones_potential as lj
from MD.pairpotential import pair_potential


def calc_force(x, dx, delta=0.001):
    return (pair_potential(x + np.reshape(dx, np.shape(x)), potential=lj) - pair_potential(x, potential=lj)) / delta
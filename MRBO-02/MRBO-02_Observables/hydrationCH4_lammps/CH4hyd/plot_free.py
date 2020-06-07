import numpy as np
import math

data = np.genfromtxt("MRBO-02/MRBO-02_Observables/hydrationCH4_lammps/CH4hyd/fdti10/intout.dat")

import matplotlib.pyplot as plt
plt.plot(np.linspace(0,1,len(data)),data)
plt.xlabel("$\lambda$")
plt.ylabel("$\Delta A$ / kcal/mol")
plt.show()
# # plt.xlabel("$\lambda$")
# # plt.ylabel("$\Delta A$ / kcal/mol")
# plt.show()

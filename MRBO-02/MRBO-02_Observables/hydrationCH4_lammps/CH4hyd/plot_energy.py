import numpy as np

data = np.genfromtxt("MRBO-02/MRBO-02_Observables/hydrationCH4_lammps/CH4hyd/fdti10/fdti10.lmp")


import matplotlib.pyplot as plt
plt.plot(np.linspace(0,1,len(data)), data[:,1])

plt.xlabel("$\lambda$")
plt.ylabel("$\Delta U$ / kcal/mol")
plt.show()

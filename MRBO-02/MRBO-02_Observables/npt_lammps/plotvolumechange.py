import numpy as np

data = np.genfromtxt("MRBO-02/MRBO-02_Observables/npt_lammps/log.lammps", skip_header=46, skip_footer=1)


import matplotlib.pyplot as plt
plt.plot(data[:,0], data[:,-1])

plt.xlabel("step")
plt.ylabel("volume")
plt.show()

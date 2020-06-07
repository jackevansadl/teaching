import numpy as np

data = np.genfromtxt("MRBO-02/MRBO-02_Observables/diffusion_lammps/out.msd.3d", skip_header=63, skip_footer=24)


import matplotlib.pyplot as plt
plt.plot(data[:,0], data[:,-1])

plt.xlabel("step")
plt.ylabel("D")
plt.show()

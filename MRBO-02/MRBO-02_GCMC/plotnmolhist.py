import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('MRBO-02/MRBO-02_GCMC/MFI_methane/NumberOfMoleculesHistograms/System_0/Histogram_methane_0_Density_10000.dat')
plt.plot(data[:,0],data[:,1],label="10000 Pa")
data = np.genfromtxt('MRBO-02/MRBO-02_GCMC/MFI_methane/NumberOfMoleculesHistograms/System_0/Histogram_methane_0_Density_100000.dat')
plt.plot(data[:,0],data[:,1],label="100000 Pa")
plt.xlabel("number of molecules")
plt.ylabel("frequency")
plt.legend(frameon=False)
#plt.show()
plt.savefig("nmolhist.png",dpi=600)
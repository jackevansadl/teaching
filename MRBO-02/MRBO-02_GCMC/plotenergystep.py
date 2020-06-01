import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('energy')

def movingaverage(interval, window_size):
    window= np.ones(int(window_size))/float(window_size)
    return np.convolve(interval, window, 'same')

plt.plot(data[:,0], data[:,1],'.',ms=2)

y_av = movingaverage(data[:,1], 50000)
#splt.ylim([-2.0317E-01, -0.0317E-02])
plt.plot(data[:,0], y_av, color="C1")

print(np.mean(data[-5000000,1]))

#plt.plot([min(data[:,0]),max(data[:,0])],[-1.0317E-02,-1.0317E-02],color='k')

plt.xlabel("step")
plt.ylabel("energy*")
plt.savefig("energy.png",dpi=600)
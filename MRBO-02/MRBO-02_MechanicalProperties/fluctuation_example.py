import numpy as np
import math, sys, time
import numpy as np
import scipy.linalg, scipy.constants
import matplotlib.pyplot as plt
from scipy import signal
import pymatgen as pmg
import itertools
from pymatgen.core import Lattice
from pymatgen.core.tensors import Tensor
from pymatgen.analysis.elasticity.elastic import ElasticTensor
from pymatgen.analysis.elasticity.elastic import ElasticTensorExpansion
import pandas as pd

data = np.genfromtxt("./pcu_2.log", skip_footer=29, skip_header=17)

a_mean = []
b_mean = []
c_mean = []
alpha_mean = []
beta_mean = []
gamma_mean = []
vol_mean = []
mechanical_eig_max = []
mechanical_eig_min = []
temp = []

h = []
for frame in data:
    lattice = Lattice.from_lengths_and_angles([frame[14], frame[15], frame[16]], [frame[17], frame[18], frame[19]])
    hmatrix = lattice.matrix
    h.append(hmatrix)

a_mean.append(np.mean(data[:,14]))
b_mean.append(np.mean(data[:,15]))
c_mean.append(np.mean(data[:,16]))
alpha_mean.append(np.mean(data[:,17]))
beta_mean.append(np.mean(data[:,18]))
gamma_mean.append(np.mean(data[:,19]))
vol_mean.append(np.mean(data[:,13]))
temp.append(np.mean(data[:,11]))

h = np.array(h)
h0 = np.mean(h, axis=0)
h0_std = np.std(h, axis=0)
h0m1  = np.linalg.inv(h0)
h0m1t = np.linalg.inv(np.transpose(h0))
eps_mat = np.array(list(map(lambda hi : (np.dot(h0m1t, np.dot(hi.transpose(), np.dot(hi, h0m1))) - np.identity(3))/2.0, h)))
eps_voigt = np.empty([6,eps_mat.shape[0]], "d")
eps_voigt[0] = eps_mat[:,0,0]
eps_voigt[1] = eps_mat[:,1,1]
eps_voigt[2] = eps_mat[:,2,2]
eps_voigt[3] = eps_mat[:,2,1]
eps_voigt[4] = eps_mat[:,2,0]
eps_voigt[5] = eps_mat[:,1,0]
eps_voigt_mean = np.mean(eps_voigt, axis=1)
Smat = np.zeros([6,6], "d")
for i in range(6):
    for j in range(i,6):
        Smat[i,j] = np.mean(eps_voigt[i]*eps_voigt[j])-eps_voigt_mean[i]*eps_voigt_mean[j]
        if i != j: Smat[j,i] = Smat[i,j]
T=300
V = np.linalg.det(h0)
Cmat = np.linalg.inv(Smat)*((1.3806488E-23*T)/(V*1E-30))*1E-9
Cmat = np.around(Cmat, decimals=2)
print(Cmat)
Cmat_eig = np.linalg.eigvals(Cmat)
mechanical_eig_max.append(max(Cmat_eig))
mechanical_eig_min.append(min(Cmat_eig))
print(mechanical_eig_max)
print(mechanical_eig_min)

mat = Tensor.from_voigt(Cmat)
elastic = ElasticTensor(mat)
print(elastic.k_vrh)
#np.savetxt("pcu_1.cij", Cmat)
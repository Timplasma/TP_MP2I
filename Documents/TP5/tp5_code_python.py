import numpy as np
import matplotlib.pyplot as plt
from numpy.random import *

tension_r100=np.array([1.01,2.07,3.06,4.05,5.02,6.05,7.04,8.02,9.06,10.23])
intensite_r100=np.array([9.07e-3, 18.47e-3, 27.35e-3, 36.12e-3, 45.35e-3, 54.22e-3, 65.05e-3, 71.59e-3,81.69e-3,92.98e-3])

Delta_t_r100 = 0.2
Delta_i_r100=0.05e-3

tension_r1000=np.array([5.03, 8.05, 9.02, 10.13])
intensite_r1000=np.array([0.501e-3, 0.803e-3, 0.896e-3,1.012e-3])

Delta_t_r1000 = 0.2
Delta_i_r1000=0.02e-3

tension_r10e6=np.array([5.02,8.07,9.03,10.16])
intensite_r10e6=np.array([5.06e-6,8.09e-6,9.09e-6,10.15e-6])

Delta_t_r10e6 = 0.2
Delta_i_r10e6=0.05e-6

Nsim = 100000

tension_r100_sim = uniform(tension_r100-Delta_t_r100*np.sqrt(3),tension_r100+Delta_t_r100*np.sqrt(3))
intensite_r100_sim = uniform(intensite_r100-Delta_i_r100*np.sqrt(3),intensite_r100+Delta_i_r100*np.sqrt(3))
resistance_r100_sim = tension_r100_sim/intensite_r100_sim

resistance_r100_moyenne = np.mean(resistance_r100_sim)
resistance_r100_ecart_type = np.std(resistance_r100_sim)

print(f'Resistance R100 Moyenne : {resistance_r100_moyenne:.1f} / Ecart type : {resistance_r100_ecart_type:.1e}\n')

tension_r1000_sim = uniform(tension_r1000-Delta_t_r1000*np.sqrt(3),tension_r1000+Delta_t_r1000*np.sqrt(3))
intensite_r1000_sim = uniform(intensite_r1000-Delta_i_r1000*np.sqrt(3),intensite_r1000+Delta_i_r1000*np.sqrt(3))
resistance_r1000_sim = tension_r1000_sim/intensite_r1000_sim

resistance_r1000_moyenne = np.mean(resistance_r1000_sim)
resistance_r1000_ecart_type = np.std(resistance_r1000_sim)

print(f'Resistance R1000 Moyenne : {resistance_r1000_moyenne:.1f} / Ecart type : {resistance_r1000_ecart_type:.1e}\n')

tension_r10e6_sim = uniform(tension_r10e6-Delta_t_r10e6*np.sqrt(3),tension_r10e6+Delta_t_r10e6*np.sqrt(3))
intensite_r10e6_sim = uniform(intensite_r10e6-Delta_i_r10e6*np.sqrt(3),intensite_r10e6+Delta_i_r10e6*np.sqrt(3))
resistance_r10e6_sim = tension_r10e6_sim/intensite_r10e6_sim

resistance_r10e6_moyenne = np.mean(resistance_r10e6_sim)
resistance_r10e6_ecart_type = np.std(resistance_r10e6_sim)

print(f'Resistance R10e6 Moyenne : {resistance_r10e6_moyenne:.1f} / Ecart type : {resistance_r10e6_ecart_type:.1e}')

plt.figure(figsize=(10,10))
plt.xlabel("Intensité")
plt.ylabel("Tension")

plt.plot(intensite_r100, tension_r100, 'r+-', lw=0.5, label="Résistence de 100 Ohm")

plt.legend()
plt.show()

plt.plot(intensite_r1000, tension_r1000, 'b', lw=0.5, label="Résistence de 1000 Ohm")

plt.legend()
plt.show()

plt.plot(intensite_r10e6, tension_r10e6, 'g', lw=0.5, label="Résistence de 10e6 Ohm")

plt.legend()
plt.show()
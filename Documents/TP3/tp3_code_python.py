import numpy as np
import matplotlib.pyplot as plt
from numpy.random import *

def calcul_conv(D,Delta_D,x1,Delta_x1,x2,Delta_x2, Nsim):
    D_sim=uniform(D-Delta_D,D+Delta_D,Nsim)
    x1_sim=uniform(x1-Delta_x1,x1+Delta_x1, Nsim)
    x2_sim=uniform(x2-Delta_x2,x2+Delta_x2, Nsim)
    d_sim=x2_sim-x1_sim
    return ((D_sim**2)-(d_sim**2))/(4*D_sim)

def calcul2_conv(D,Delta_D,d,Delta_d,Nsim):
    D_sim=uniform(D-Delta_D,D+Delta_D,Nsim)
    d_sim=uniform(d-Delta_d,d+Delta_d,Nsim)
    return ((D_sim**2)-(d_sim**2))/(4*D_sim)

def calcul_div(D,Delta_D,d,Delta_d,v,Nsim):
    v1=1/calcul2_conv(D,Delta_D,d,Delta_d,Nsim)
    return v1-v

print(f'Moyenne vergence 8d jeu1 : {np.mean(1/calcul_conv(60e-2,0.5e-2,18e-2,0.5e-2,41e-2,0.5e-2, 1000))}')
print(f'Moyenne vergence 8d jeu2 : {np.mean(1/calcul_conv(60e-2,0.5e-2,17.5e-2,0.5e-2,42.5e-2,0.5e-2, 1000))}')
print(f'Moyenne vergence 3d jeu1 : {np.mean(1/calcul_conv(1.40,0.005,0.55,0.005,0.84,0.005, 1000))}')
print(f'Moyenne vergence 3d jeu2 : {np.mean(1/calcul_conv(1.55,0.005,0.58,0.005,0.96,0.005, 1000))}')
print(f'Moyenne vergence 20d jeu1 : {np.mean(1/calcul2_conv(0.235,0.005,0.045,0.005,1000))}')
print(f'Moyenne vergence -2d jeu1 : {np.mean(calcul_div(1.55,0.005,1.17,0.005, 7.81, 1000))}')
print(f'Moyenne vergence -6d jeu1 : {np.mean(calcul_div(0.40,0.005,0.2,0.005,19.32,1000))}')
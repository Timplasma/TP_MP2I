import numpy as np
import matplotlib.pyplot as plt
from numpy.random import *

def conv_minute_angle_degre(angle_degre, partie_minute_angle):
    conversion = partie_minute_angle/60
    print(angle_degre+conversion)
    return angle_degre+conversion

def calcul_dist_pas(dm, l):
    return l/(2*np.sin(np.radians(dm/2)))

def calcul_nb_pas(dist_pas):
    return 1/dist_pas

lunette_x1 = conv_minute_angle_degre(311.5, 0)
lunette_x2 = conv_minute_angle_degre(349,0)
reseau_x1 =conv_minute_angle_degre(119,3)
reseau_x2 = conv_minute_angle_degre(138,10)

#On considère un angle d'incertitude de 0.5°
delta_mesure = 0.05
Nsim = 1000

lunette_x1_sim = uniform(lunette_x1-delta_mesure*np.sqrt(3), lunette_x1+delta_mesure*np.sqrt(3), Nsim)
lunette_x2_sim = uniform(lunette_x2-delta_mesure*np.sqrt(3), lunette_x2+delta_mesure*np.sqrt(3), Nsim)

lambda_jaune_vert = 546.1

Dm_sim = (lunette_x2_sim - lunette_x1_sim)/2

moyenne_dist_pas =np.mean(calcul_dist_pas(Dm_sim, lambda_jaune_vert))
print(f"Moyenne distance entre les pas : {moyenne_dist_pas}")
print(f"Moyenne nombre de pas : {np.mean(calcul_nb_pas((moyenne_dist_pas)*10**-6))}")
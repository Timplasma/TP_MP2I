#Bibliothèques
import numpy as np
from numpy.random import *
import matplotlib.pyplot as plt
import csv

import matplotlib_inline.backend_inline as bckend
bckend.set_matplotlib_formats('svg')


def lire_fichier_csv(parametre):
    liste = []
    with open(parametre, "r") as fichier_csv:
        reader_notes = csv.reader(fichier_csv)
        for ligne in reader_notes:
            liste.append(ligne)
    return liste

table_data = lire_fichier_csv('Data.csv')

#print(table_data[4][0])

deltai1 = 0.25
deltai2 = 0.5

table_data_x, table_data_y = [], []

print(table_data)

for i in range(1, len(table_data)):
    table_data_x.append(int(table_data[i][0]))
    table_data_y.append(int(table_data[i][2]))
    

table_data_x = np.array(table_data_x)
table_data_y = np.array(table_data_y)
    
print(table_data_x)

sini1 = np.sin(np.radians(table_data_x))
sini2 = np.sin(np.radians(table_data_y))

# Incertitude sur les angles

Nsim = 5000
u_sini1 = []
u_sini2 = []

for i in range(len(table_data_x)):
    i1_sim = uniform(table_data_x[i]-deltai1, table_data_x[i] + deltai1, Nsim)
    i2_sim = uniform(table_data_y[i]-deltai2, table_data_y[i] + deltai2, Nsim)
    sini1_sim = np.sin(np.radians(i1_sim))
    sini2_sim = np.sin(np.radians(i2_sim))
    u_sini1.append(np.std(sini1_sim))
    u_sini2.append(np.std(sini2_sim))


p = np.polyfit(sini1, sini2, 1)
a = p[0]
b = p[1]


a_sim = []
b_sim = []

for i in range(Nsim):
    sini1_sim_u = []
    sini2_sim_u = []
    for j in range(len(table_data_x)):
        sini1_sim_u.append(uniform(sini1[j]-u_sini1[j]*np.sqrt(3), 
                                   sini1[j]+u_sini1[j]*np.sqrt(3)))
        sini2_sim_u.append(uniform(sini2[j]-u_sini2[j]*np.sqrt(3), 
                                   sini2[j]+u_sini2[j]*np.sqrt(3)))
    a, b=np.polyfit(sini1_sim_u, sini2_sim_u, 1)
    a_sim.append(a)
    b_sim.append(b)

u_a=np.std(a_sim)
u_b=np.std(b)


plt.figure(figsize=(8,6))

plt.xlabel('Sinus de l\'angle $\sin(i_1)$')
plt.ylabel('Sinus de l\'angle $\sin(i_2)$')

plt.errorbar(sini1, sini2, xerr=u_sini1, yerr=u_sini2,lw=1, fmt='b+',zorder=2,label='Données')
# plt.plot(sini1, sini2, 'b+', label='Données')

xfit = np.linspace(min(sini1), max(sini1), 2)
plt.plot(xfit, b + a*xfit, 'r', lw=0.5, label = 'y=('+str(round(a,3))+'$\pm$'+str(round(u_a,3))+')$\cdot$x+('
         +str(round(b,3))+'$\pm$'+str(round(u_b,3))+')')
    
plt.legend()
plt.show()





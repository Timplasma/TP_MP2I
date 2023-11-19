import csv
import matplotlib.pyplot as plt
import numpy as np

def open_tek_csv():
    with open('csv/TEK0002.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        x = []
        y = []
        for line in csv_reader:
            if line[0]:
                print(f"{line[0]} : {line[1]}")
            x.append(float(line[3]))
            y.append(float(line[4]))
    x = np.array(x)
    y = np.array(y)
    return x,y

x,y = open_tek_csv()

# Tracé de la courbe avec matplotlib grâce aux données du csv
plt.title('Courbe de tension en fonction du temps')
plt.xlabel('Temps (s)')
plt.ylabel('Tension (V)')
# plt.xlim(-100*2.000000e-07, 2.500000e+03*2.000000e-07)
plt.plot(x, y, "r-")
plt.show()


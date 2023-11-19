import random

def monte_carlo_calculation(func, num_samples):
    total = 0
    squared_total = 0

    for _ in range(num_samples):
        sample = func()
        total += sample
        squared_total += sample ** 2

    mean = total / num_samples
    variance = (squared_total / num_samples) - (mean ** 2)
    std_deviation = variance ** 0.5

    return mean, std_deviation

def my_function():
    # Mettez ici votre fonction à évaluer
    # Par exemple, pour calculer l'incertitude sur une moyenne de valeurs aléatoires entre 0 et 1 :
    return random.uniform(0, 1)

num_samples = 10000  # Nombre d'échantillons à générer

mean, std_deviation = monte_carlo_calculation(my_function, num_samples)

print("Estimation de la moyenne :", mean)
print("Estimation de l'incertitude :", std_deviation)

"""
Des fonctions usuelles utiles
"""
from random import uniform
import numpy as np


def monte_carlo(fn, *args, N=5000):
    """
    Une version généralisée de monte-carlo

    Exemple d'utilisation:
        result = list(monte_carlo(lambda a, b: sin(a) * sin(b), (3, 0.5), (5, 0.3)))
    Ici, a vaudra 3 +/- 0.5 et b vaudra 5 +/- 0.3
    Un générateur de toutes les valeurs résultantes sera retourné

    :param: fn Une fonction, qui utilisera les paramètres (simulés)
    :param: *args Une suite d'argument de la forme (valeur, delta), qui seront utilisés dans le même ordre dans la fonction
    :param: N Le nombre de simulation par argument
    :return: Generator Un itérateur des résultats
    """
    yield from (fn(*(uniform(e - delta, e + delta) for e, delta in args)) for i in range(N))

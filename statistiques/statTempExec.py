import numpy as np
import matplotlib.pyplot as plt
from pylab import *

# Données de génération des deux courbes
#Courbe de 10 évolution par exécution
x = np.array([50, 100, 250, 500, 750, 1000])
y = np.array([0.4, 6.8, 28.49, 143.84, 405.76, 894.97])
#Courbe de 50 évolutions par exécutions
x1 = np.array([50, 100, 250, 500, 750, 1000, ])
y1 = np.array([9.465, 20.34, 128.41, 711.05, 3612.12, 6567.57 ])
#Création des courbes
plt.plot(x, y, x1, y1)

#Ajout de titres et de légendes
title("Temps d'exécution en fonction du nombre de villes pour 10 et 50 évolutions")
plt.xlabel("Nombre de villes")
plt.ylabel("Temps d'exécution (s)")
plt.plot(x, y, "o--", label="10 évolutions")
plt.plot(x1, y1,"o--", label="50 évolutions")
plt.legend()
plt.show() # affiche la figure a l'ecran


import numpy as np
import matplotlib.pyplot as plt
from pylab import *

# Données de génération des deux courbes
#Courbe de 10 évolution par exécution
x = np.array([50, 100, 250, 500, 750, 1000])
y = np.array([0.57, 8.64, 27.8,146.79, 410.91, 901.43])
#Courbe de 50 évolutions par exécutions
x1 = np.array([50, 100, 250, 500, 750, 1000, ])
y1 = np.array([8.9, 21.86, 125.5, 722, 3631.85, 6562 ])
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


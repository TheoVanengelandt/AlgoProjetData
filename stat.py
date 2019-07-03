import numpy as np
import matplotlib.pyplot as plt
from pylab import *

# Données de génération des deux courbes
x = np.array([50, 100, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])
y = np.array([10, 28, 52, 155, 281, 460, 647, 980, 1263, 1655])
x1 = np.array([50, 100, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])
y1 = np.array([8, 31, 49, 150, 278, 457, 651, 975, 1268, 1670])

#Création de la courbe
plt.plot(x, y, x1, y1)

#Ajout de titres et de légendes
title("Temps d'exécution en fonction du nombre de villes")
plt.xlabel("Nombre de villes")
plt.ylabel("Temps d'exécution (s)")
plt.plot(x, y, "o--", label="Test 1")
plt.plot(x1, y1,"o--", label="Test 2")
plt.legend()


plt.show() # affiche la figure a l'ecran
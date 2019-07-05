import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#Définition des valeurs
distance_initiale, init_std = (4553, 20607, 132579, 517528, 1292198, 2096034), (1, 1, 1, 1, 1,1)
distance10, dix_std = (3388, 14610, 103337, 429381, 1105820, 1834722), (1, 1, 1, 1, 1, 1)
distance50, cinquante_std = (2495, 9522,  74550, 314706, 827388, 1473427), (1, 1, 1, 1, 1,1)

ind = np.arange(len(distance_initiale))  # the x locations for the groups
width = 0.20  # the width of the bars

fig, ax = plt.subplots()
#Génération des barres du graphique
rects1 = ax.bar(ind - width, distance_initiale, width, yerr=init_std,
                label='Distance initiale')
rects2 = ax.bar(ind, distance10, width, yerr=dix_std,
                label='Distance après 10 évolutions')
rects3 = ax.bar(ind + width, distance50, width, yerr=cinquante_std,
                label='Distance après 50 évolutions')

# Ajout de texte, légendes, unités afin de faciliter la compréhension du graphes
ax.set_ylabel('Distance')
ax.set_xlabel('Taille de la population')
ax.set_title('Réduction de la distance initiale en fonction de la population')
ax.set_xticks(ind)
ax.set_xticklabels(('50', '100', '250', '500', '750', '1000'))
ax.legend()


def autolabel(rects, xpos='center'):
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0, 'right': 1, 'left': -1}

    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(offset[xpos]*3, 3),  # use 3 points offset
                    textcoords="offset points",  # in both directions
                    ha=ha[xpos], va='bottom')


autolabel(rects1, "left")
autolabel(rects2, "center")
autolabel(rects3, "right")

fig.tight_layout()
#Affichage de la solution
plt.show()

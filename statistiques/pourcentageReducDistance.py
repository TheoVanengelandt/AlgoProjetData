import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#Valeur des pourcentages
distance_initiale, init_std = (100, 100, 100, 100, 100, 100), (1, 1, 1, 1, 1,1)
distance10, dix_std = (74.4, 70.9, 77.9, 82.9, 85.5, 87.5), (1, 1, 1, 1, 1, 1)
distance50, cinquante_std = (54.8, 46.2,  56.2, 60.8, 64.02, 70.29), (1, 1, 1, 1, 1,1)

ind = np.arange(len(distance_initiale))  # the x locations for the groups
width = 0.20  # the width of the bars

#Création des barres
fig, ax = plt.subplots()
rects1 = ax.bar(ind - width, distance_initiale, width, yerr=init_std,
                label='Pourcentage initiale')
rects2 = ax.bar(ind, distance10, width, yerr=dix_std,
                label='Pourcentage de distance restant après 10 évolutions')
rects3 = ax.bar(ind + width, distance50, width, yerr=cinquante_std,
                label='Pourcentage de distance restant après 50 évolutions')

# Ajout de texte pour faciliter la compréhension du diagramme
ax.set_ylabel('Pourcentage (%)')
ax.set_xlabel('Taille de la population')
ax.set_title('Pourcentage d\'efficacité de l\'algorithme sur un échantillon en fonction du nombre d\'évolutions')
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
import matplotlib.pyplot as plt
import pylab

listData = [711.4,	705.8,	699.8,	724.5,	721.5,	726.5,	708.4,	701.5,	697.8,	693.2,	745.7,	751.4,	714.5,	699.9,	721.5,	724.6,	718.5,	716.5,	726.5,	734.6,	788.6,	745.7,	751.2,	685.6,	711.45,	745.6]

BoxName = ['500 (10évolutions)']

data = [listData]

plt.boxplot(data)
plt.ylabel("Valeurs (y)")
plt.ylim(650,800)

pylab.xticks([1], BoxName)

plt.savefig('Boite à moustache de la population de 500')
plt.show()
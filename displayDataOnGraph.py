# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 15:13:53 2019

@author: theo
"""
# JSON lib
import json

# Path lib
import os

import matplotlib.pyplot as plt

print('Nom du fichier à afficher ? (ex: nomFichier.json)')
fileName = input()
dataFileName = str('data/'+ fileName)

try:
    with open(dataFileName) as json_file:  
        data = json.load(json_file)
        for cityID in data['cityList']:
            city = data['cityList'][cityID]
            # print('name: ' + city['name'] + '\npos x: ' + str(city['pos'][0]) + ', pos y: ' + str(city['pos'][1]) + '\n ')
            
            plt.scatter(city['pos'][0], city['pos'][1])
         
    plt.title('Nuage de points de' + fileName + ' avec Matplotlib')
    plt.xlabel('x')
    plt.ylabel('y')
    
    if not os.path.exists('graph/'):
        os.makedirs('graph/')
        
    
    print('Sauvegarder le graph créé sous ? (ex: monNomDeFichier) \nPS: le format est ajouté automatiquement :)')
    fileName = input()
    graphFileName = str('graph/'+ fileName + '.png')
    
    plt.savefig(graphFileName)
    print("Le fichier de donnée a été généré")
    input("Press Enter to close...")
    
    plt.show()

except (OSError, IOError) as e:
     print(str(e) + '!')
     input("Press Enter to close...")
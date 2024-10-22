# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 10:55:52 2019

@author: theo
"""

# Python code to generate 
# random numbers and random string
import random
import string

# JSON lib
import json

# Path lib
import os

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

# Function which generate data and append them
## arrayName = name of the list in which data is added
## num = number of elements needs to be appended 
def Rand(arrayName, num): 
  
    start = 0
    end = num*4

    for j in range(num): 
        arrayName[str(j+1)] = {
                str('name') : randomString(),
                str('pos') : (random.randint(start, end), random.randint(start, end))
                }
  
    return arrayName 


# Create an empty dictionary
data = {}  
# Add empty dictionary to 'cityList' key
data['cityList'] = {}
  
print('Nombre de ville à générer ?')
valueNumber = input()

Rand(data['cityList'], int(valueNumber))

if not os.path.exists('data/'):
    os.makedirs('data/')
    
# open and create a file
print('Sauvegarder le fichier créé sous ? (ex: monNomDeFichier) \nPS: le format est ajouté automatiquement :)')
fileName = input()
dataFileName = str('data/'+ fileName + '.json')
    
with open(dataFileName, 'a') as outfile:  
    json.dump(data, outfile)


print("Le fichier de donnée a été généré")
input("Press Enter to close...")
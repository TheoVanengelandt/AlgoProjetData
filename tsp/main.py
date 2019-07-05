from galogic import *
# matplotlib lib
import matplotlib.pyplot as plt
# JSON lib
import json
import time
# Path lib
import os
# DisplayDataOnGraph method
import sys
sys.path.insert(0, '../')
from displayDataOnGraph import DisplayDataOnGraph
# UUID generator
import uuid

# Début du comptage du temps d'exécutio,
start_time = time.time()

routeManager = RouteManager()

fileName = input('Nom du fichier à étudier ? (ex: nomFichier.json) ')
dataFileName = str('../data/' + fileName)

try:
    with open(dataFileName) as json_file:
        data = json.load(json_file)
        for cityID in data['cityList']:
            city = data['cityList'][cityID]

            RouteManager.addDustbin(Dustbin(city['pos'][0], city['pos'][1]))

    evolutionNumber = int(
        input("Combien d'évolution ? (default = 40) ")
        or "40"
    )

    pop = Population(RouteManager.numberOfDustbins(), True)
    print('\nInitial distance: ' + str(pop.getFittest().getDistance()))
    yaxis = []
    xaxis = []
    # Nombre d'evolution que va réaliser l'algorithme
    for i in range(evolutionNumber):
        pop = GA.evolvePopulation(pop)
        fittest = pop.getFittest().getDistance()
        yaxis.append(fittest)
        xaxis.append(i)
        if fittest < 1050:
            break

    print('Final distance: ' + str(fittest))
    # print('Final Route: ' + pop.getFittest().toString())

    # Create an empty dictionary
    data = {}
    # Add empty dictionary to 'cityList' key
    data['cityList'] = {}

    print('\nliste des villes :')
    listVille = pop.getFittest().toString().split("|")
    for v in range(len(listVille)):
        if listVille[v]:
            data['cityList'][v] = {
                str('name') : ('ville' + str(v)),
                str('pos'): (
                    int(listVille[v].split(",")[0].replace('(', '')),
                    int(listVille[v].split(",")[1].replace(')', ''))
                )
            }

            print('-> ' + listVille[v], end=" ")

    print("\n\nGraph d'évolution :")
    fig = plt.figure()
    #plt.ylim(0, 80000)
    plt.plot(xaxis, yaxis, 'r-')
    plt.show()
    
    # Affichage du temps d execution
    print("Temps d execution : %s secondes ---" % (time.time() - start_time))

    if not os.path.exists('../rep/'):
        os.makedirs('../rep/')

    dataFileName = str('rep/rep' + fileName)
   
    if os.path.exists('../'+ dataFileName):
        dataFileName = str('rep/rep' + uuid.uuid4().hex + '-' + fileName )
        
    with open('../' + dataFileName, 'a') as outfile:
        json.dump(data, outfile)

    DisplayDataOnGraph('../' + dataFileName, '../graph/')


except (OSError, IOError) as e:
    print(str(e) + '!')
    input("Press Enter to close...")

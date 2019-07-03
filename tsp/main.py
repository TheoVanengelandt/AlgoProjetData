from galogic import *
import matplotlib.pyplot as plt
# JSON lib
import json

routeManager = RouteManager()

fileName = input('Nom du fichier à étudier ? (ex: nomFichier.json) ')
dataFileName = str('../data/' + fileName)

try:
    with open(dataFileName) as json_file:
        data = json.load(json_file)
        for cityID in data['cityList']:
            city = data['cityList'][cityID]

            RouteManager.addDustbin(Dustbin(city['pos'][0], city['pos'][1]))

    evolutionNumber = int(input("Combien d'évolution ? (default = 40) ") or  "40")

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
    print('Final Route: ' + pop.getFittest().toString())
    
    fig = plt.figure()
    #plt.ylim(0, 80000)
    plt.plot(xaxis, yaxis, 'r-')
    plt.show()

except (OSError, IOError) as e:
    print(str(e) + '!')
    input("Press Enter to close...")
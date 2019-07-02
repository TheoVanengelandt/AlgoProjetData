from galogic import *
import matplotlib.pyplot as plt
# JSON lib
import json

routeManager = RouteManager()

print('Nom du fichier à étudier ? (ex: nomFichier.json)')
fileName = input()
dataFileName = str('../data/'+ fileName)

try:
    with open(dataFileName) as json_file:  
        data = json.load(json_file)
        for cityID in data['cityList']:
            city = data['cityList'][cityID]
            
            RouteManager.addDustbin(Dustbin(city['pos'][0], city['pos'][1]))
            
except (OSError, IOError) as e:
     print(str(e) + '!')
     input("Press Enter to close...")


pop = Population(50, True)
print ('Initial distance: ' + str(pop.getFittest().getDistance()))
yaxis = []
xaxis = []
for i in range(101):
    pop = GA.evolvePopulation(pop)
    fittest = pop.getFittest().getDistance()
    yaxis.append(fittest)
    xaxis.append(i)
    if fittest < 1050:
        break
print ('Final distance: ' + str(fittest))
print ('Final Route: ' + pop.getFittest().toString())

fig = plt.figure()
#plt.ylim(0, 80000)
plt.plot(xaxis, yaxis, 'r-')
plt.show()

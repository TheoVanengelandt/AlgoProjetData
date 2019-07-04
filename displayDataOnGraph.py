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


def DisplayDataOnGraph(dataFileName, localGraphStorage='graph/'):
    try:
        with open(dataFileName) as json_file:
            data = json.load(json_file)
                            
            GraphRouteX = []
            GraphRouteY = []
                
            for cityID in data['cityList']:
                city = data['cityList'][cityID]
                # print('name: ' + city['name'] + '\npos x: ' + str(city['pos'][0]) + ', pos y: ' + str(city['pos'][1]) + '\n ')

                #draw the points with their ids
                plt.scatter(city['pos'][0], city['pos'][1],marker = 'o')
                plt.annotate(cityID, (city['pos'][0], city['pos'][1]))
                
                GraphRouteX.append(city['pos'][0])
                GraphRouteY.append(city['pos'][1])
                
                if(int(cityID) == int(len(data['cityList']))):
                    GraphRouteX.append(data['cityList']['1']['pos'][0])
                    GraphRouteY.append(data['cityList']['1']['pos'][1])

        plt.title('Nuage de points avec Matplotlib')
        plt.xlabel('x')
        plt.ylabel('y')

        # Create a folder for graph ("graph/" by default)
        if not os.path.exists(localGraphStorage):
            os.makedirs(localGraphStorage)

        fileName = input(
            "Sauvegarder le graph créé sous ? (ex: monNomDeFichier)\n"
            + "PS: le format du fichier et le dossier de stockage sont ajoutés automatiquement :)\n"
        )

        plt.plot(GraphRouteX, GraphRouteY)
        graphFileName = str(localGraphStorage + fileName + '.png')
        plt.savefig(graphFileName)
        plt.show()

    except (OSError, IOError) as e:
        print(str(e) + '!')
        input("Press Enter to close...")


def mapPlot(list_city_X,list_city_Y):

    #drawing of point and add ID
    plt1.figure(2)
    for i in range(0,len(list_city_X)):
        plt1.scatter(list_city_X[i],list_city_Y[i],marker = '+')
        plt1.annotate(i, (list_city_X[i],list_city_Y[i]))


    #drawing of segment
    with open("out_txt/bestroute.txt") as json_file:
        data_best_route = json.load(json_file)

    listXGraphRoute = []
    listYGraphRoute = []
    for (x, y) in data_best_route:
        listXGraphRoute.append(x)
        listYGraphRoute.append(y)
        print("xv "+str(x))
        print("un"+str(data_best_route[0]))
    plt1.plot(listXGraphRoute, listYGraphRoute)
    plt1.show()
    plt1.savefig('map.png')

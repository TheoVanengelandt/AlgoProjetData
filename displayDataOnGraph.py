# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 15:13:53 2019

@author: theo
"""

import matplotlib.pyplot as plt

x = [5,6,7,8,1,2,3,4]
y = [4,1,3,6,1,3,5,2]

plt.scatter(x,y)

x = [1,2,3,4]
y = [4,1,3,6]
size = [100,500,100,500]

plt.scatter(x, y, s=size, c='coral')

x = [5,6,7,8]
y = [1,3,5,2]
size = [100,500,100,500]

plt.scatter(x, y, s=size, c='lightblue')

plt.title('Nuage de points avec Matplotlib')
plt.xlabel('x')
plt.ylabel('y')

plt.savefig('ScatterPlot_01.png')
plt.show()
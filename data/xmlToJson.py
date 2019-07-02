#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 18:23:50 2019

@author: martin
"""

import json
import xmltodict
 
sample = input("Chemin relatif à partir de /data/")

with open(sample, 'r') as f:
    xmlString = f.read()
    
jsonString = json.dumps(xmltodict.parse(xmlString), indent=4)

output = input()

with open(output, 'w') as f:
    f.write(jsonString)
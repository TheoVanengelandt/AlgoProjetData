#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: martin
"""

import xml.etree.ElementTree as ET 
import json
import os 

def parseXML(xmlfile): 
  
    # create element tree object 
    tree = ET.parse(xmlfile) 
  
    # get root element 
    root = tree.getroot() 
    
    data = {} 
    data["cityList"] = {}
    i = 1
    
    for child in root.findall('./network/nodes/'):
         
         data['cityList'][str(i)] = {
                   str('pos') : [float(child[0].text), float(child[1].text)]
                   }
         i += 1 
    
    # return news items list 
    return data

def writeJSON(data, jsonfile):
    
    if not os.path.exists('out/'):
         os.makedirs('out/')
    
    datafilename = str('out/' + jsonfile)
     
    with open(datafilename, "w") as write_file:
         json.dump(data, write_file)
    
    return jsonfile

def main():
    source = input("Path to xml file (CMT datasets)\n")
    result = parseXML(source)
    filename = input ("Dest file name\n")
    writeJSON(result, filename)
    
main()

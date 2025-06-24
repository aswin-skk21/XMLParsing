import csv
import os 
import xml.etree.ElementTree as ET

def ParseXML(csv_filename): 
    output = "output.csv"
    for file in "output.csv": 
        tree = ET.parse(file)
        root = tree.getroot
        xmlList = []
        xmlList.append(os.path.abspath(file))
        #find all method, selected attributes, 
        #append to list
        with open(output, 'w') as csvfile: 
            csvwriter = csv.writer(csvfile)
            csv.writer(xmlList)
            
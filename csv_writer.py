import csv
import os 
import xml.etree.ElementTree as ET

def ParseXML(csv_filename): 
    output = "output.csv"
    with open('locations.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            tree = ET.parse(row[0])
            print("parsing" + row)
            root = tree.getroot()
            xmlList = []
            print("writing path")
            xmlList.append(os.path.abspath(row[0]))
            #find all method, selected attributes, 
            #append to list
            with open(output, 'w') as csvfile: 
                print("writing to file")
                csvwriter = csv.writer(csvfile)
                for dirpath, dirnames, filenames in os.walk(row[0]):
                    for filename in filenames:
                        if filename.endswith(".xml") and "job" in filenames.lower():
                            full_path = os.path.join(dirpath, filename)
                            if os.path.isfile(full_path):  # Only write if it's a file
                                csvwriter.writerow([full_path])
                                
                
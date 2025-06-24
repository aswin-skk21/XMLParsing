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
            xmlList.append(root.find('scheduleName'))
            xmlList.append(root.find('scheduleTime'))    
            xmlList.append(root.find('scheduleType'))    
            xmlList.append(root.find('enabled'))                
            with open(output, 'w', newline='') as csvfile: 
                print("writing to file")
                csvwriter = csv.writer(csvfile)
                for dirpath, dirnames, filenames in os.walk(row[0]):
                    for filename in filenames:
                        if filename.endswith(".xml") and "job" in filenames.lower():
                            full_path = os.path.join(dirpath, filename)
                            xmlList.append(full_path)
                            csvwriter.writerow(xmlList)
                                
                
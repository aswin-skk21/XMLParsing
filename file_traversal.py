import os
import csv

def findXMLPaths(filepath):  
    if ValidateFilePath(filepath) == True:
        print("validated")
        WritePathsCSV(filepath)
    else:
        print(f"Path does not exist: {filepath}")

def WritePathsCSV(filepath): 
    xml_file = "locations.csv"
    print("starting os walk")
    with open(xml_file, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for dirpath, dirnames, filenames in os.walk(filepath):
            for filename in filenames:
                if filename.endswith(".xml") and "job" in filename.lower():
                    #attributes = []
                    print("found" + filename)
                    path = os.path.join(dirpath, filename)
                    #attributes.append(path)
                    csvwriter.writerow(path)
 
                
def ValidateFilePath(filepath):
    if os.path.exists(filepath):
        return True
    else:
        print("File path does not exist")
        return False
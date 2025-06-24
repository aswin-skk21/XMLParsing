import os
import csv

def findXMLPaths(filepath):  
    if ValidateFilePath(filepath) == True:
        WritePathsCSV(filepath)
    else:
        print(f"Path does not exist: {filepath}")

def WritePathsCSV(filepath): 
    xml_file = "locations.csv"
    for dirpath, dirnames, filenames in os.walk(filepath):
        for filename in filenames:
            if filename.endswith(".xml") & filename.lower() == "job":
                with open(csv_file, w) as csvfile:
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerow(os.path.abspath(filename))
 
                
def ValidateFilePath(filepath):
    if os.path.exists(filepath):
        return True
    else:
        print("File path does not exist")
        return False
import os
import csv

def findXMLPaths(filepath):  
    if ValidateFilePath(filepath) == True:
        print("validated")
        WritePathsCSV(filepath)

def WritePathsCSV(filepath): 
    xml_file = "locations.csv"
    print("starting os walk")
    with open(xml_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for dirpath, dirnames, filenames in os.walk(filepath):
            #print(dirpath)
            for filename in filenames:
                print(filename)
                if filename.endswith(".XML") and filename.lower() == "job.xml":
                    #attributes = []
                    print("found " + filename)
                    path = os.path.join(dirpath, filename)
                    #attributes.append(path)
                    csvwriter.writerow([path])
 
                
def ValidateFilePath(filepath):
    if os.path.exists(filepath):
        print("Check")
        return True
    else:
        print("File path does not exist")
        return False
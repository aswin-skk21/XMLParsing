import os

def getXML(filepath):   
    if os.path.exists(filepath):
        for dirpath, dirnames, filenames in os.walk(filepath):
            for filename in filenames:
                if filename.lower().endswith(".xml"):
                    print(filename)
    else:
        print(f"Path does not exist: {filepath}")

def ValidateFilePath(filepath):
    if os.path.exists(filepath):
        return True
    else:
        print("File path does not exist")
        return False
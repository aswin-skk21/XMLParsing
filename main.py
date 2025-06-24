import sys
import csv_writer
import file_traversal
import xml_parser

def main(): 
    if len(sys.argv) != 2: 
        print("Wrong amount of arguments")
        sys.exit()  
    file_traversal.findXMLPaths(sys.argv[1])
    csv_writer.ParseXML("locations.csv")


if __name__ == "__main__":
    main()

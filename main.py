import sys
import csv_writer
import file_traversal
import xml_parser

def main(): 
    if len(sys.argv) != 2: 
        print("Wrong amount of arguments")
        sys.exit()  
    file_traversal.getXML(sys.argv[1])

if __name__ == "__main__":
    main()

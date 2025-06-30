import sys
import csv_writer
import file_traversal
import csv_delimiter
import unique_times

def main(): 
    if len(sys.argv) != 2: 
        print("Wrong amount of arguments")  
        sys.exit()  
    file_traversal.findXMLPaths(sys.argv[1])
    print("XML file paths written to locations.csv")
    csv_writer.ParseXML("locations.csv")
    print("XML data written to raw_output.csv")
    csv_delimiter.splitName("raw_output.csv")
    print("Data split and written to split_output.csv")
    unique_times.final_clean()
    print("Final data cleaned and written to final_output.csv")
    
    


if __name__ == "__main__":
    main()

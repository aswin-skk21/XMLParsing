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
    csv_writer.ParseXML("locations.csv")
    csv_delimiter.splitName("raw_output.csv")
    unique_times.final_clean()
    
    


if __name__ == "__main__":
    main()

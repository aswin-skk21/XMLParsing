import pandas as pd
import sys

def main():
    if len(sys.argv) != 2: 
        print("Wrong amount of arguments")  
        sys.exit()  
    splitName(sys.argv[1])

def splitName(input_file):
    df = pd.read_csv(input_file, header=0)
    split_cols = df.iloc[:, 1].str.split('/', n=1, expand=True)
    df.iloc[:, 1] = split_cols[0]
    df.insert(2, 'Schedule Steps', split_cols[1])
    df['Machine'] = 'CrushFTP'
    df.to_csv('split_output.csv', index=False, header=True)
if __name__ == "__main__":
    main()
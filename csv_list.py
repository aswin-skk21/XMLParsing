import csv

def main():
    with open('split_output.csv', 'r',  newline='') as i, \
         open('list.csv', 'w',  newline='') as o:

        reader = csv.reader(i)
        writer = csv.writer(o)

        header = next(reader)
        writer.writerow(header)

        for row in reader:
            copies = row[3].split(',')
            for num in copies:
                new_row = row.copy()
                new_row[3] = num.strip()
                writer.writerow(new_row)

if __name__ == "__main__":
    main()

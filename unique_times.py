import csv

def final_clean():
    input_filename = 'split_output.csv'
    output_filename = 'final_output.csv'

    time_column_index = 3

    with open(input_filename, 'r', newline='') as infile, \
        open(output_filename, 'w', newline='') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        headers = next(reader)
        writer.writerow(headers)

        for row in reader:
            if len(row) <= time_column_index:
                continue
            times = [t.strip() for t in row[time_column_index].split(',') if t.strip()]
            if not times:
                writer.writerow(row)  
            else:
                for time in times:
                    new_row = row.copy()
                    new_row[time_column_index] = time
                    writer.writerow(new_row)
import os
import csv

# Configuration
input_file = 'data.csv'          # The input CSV file (420 MB in your case)
max_file_size = 10 * 1024 * 1024    # 10 MB in bytes
output_prefix = 'output_part_'      # Prefix for the output files

# Initialize variables
part_number = 1

# Function to open a new CSV file and write the header
def open_new_file(header):
    filename = f'{output_prefix}{part_number}.csv'
    outfile = open(filename, 'w', newline='', encoding='utf-8')
    writer = csv.writer(outfile)
    writer.writerow(header)
    return outfile, writer

# Open the input CSV file for reading
with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    
    # Read the header line
    header = next(csv_reader)
    
    # Open the first output file and write the header
    outfile, csv_writer = open_new_file(header)
    
    # Process each row
    for row in csv_reader:
        csv_writer.writerow(row)
        # Check the size of the file by getting the current position of the file pointer
        if outfile.tell() >= max_file_size:
            outfile.close()  # Close current file
            part_number += 1  # Increment file count
            outfile, csv_writer = open_new_file(header)  # Open a new file and write the header

    # Close the last file after finishing
    outfile.close()

print(f"CSV split into {part_number} parts, each approximately 10 MB or smaller.")

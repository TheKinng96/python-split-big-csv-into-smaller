#!/usr/bin/env python3
import os
import csv
import argparse
from pathlib import Path

def split_csv(input_file, output_dir, max_size_mb=10, encoding='latin-1', columns_to_drop=None):
    """
    Split a large CSV file into smaller files while preserving the header.
    
    Args:
        input_file (str): Path to the input CSV file
        output_dir (str): Directory to save the output files
        max_size_mb (int): Maximum size of each output file in MB
        encoding (str): Encoding of the input file (default: latin-1)
        columns_to_drop (list): List of column names to drop from the CSV
    """
    # Convert max size to bytes
    max_size_bytes = max_size_mb * 1024 * 1024
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get the base name of the input file without extension
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    
    # Initialize variables
    part_number = 1
    current_file = None
    current_writer = None
    current_size = 0
    header = None
    column_indices_to_drop = []
    
    try:
        # Open the input CSV file with the specified encoding
        with open(input_file, 'r', newline='', encoding=encoding) as infile:
            csv_reader = csv.reader(infile)
            
            # Read the header
            header = next(csv_reader)
            
            # Find indices of columns to drop
            if columns_to_drop:
                column_indices_to_drop = [i for i, col in enumerate(header) if col in columns_to_drop]
                
                # Filter out the columns to drop from the header
                header = [col for i, col in enumerate(header) if i not in column_indices_to_drop]
                
                print(f"Dropping columns: {columns_to_drop}")
                print(f"New header: {header}")
            
            # Process each row
            for row in csv_reader:
                # Filter out the columns to drop
                if column_indices_to_drop:
                    row = [val for i, val in enumerate(row) if i not in column_indices_to_drop]
                
                # If we need to start a new file
                if current_file is None:
                    output_file = os.path.join(output_dir, f"{base_name}_part_{part_number}.csv")
                    current_file = open(output_file, 'w', newline='', encoding=encoding)
                    current_writer = csv.writer(current_file)
                    current_writer.writerow(header)
                    current_size = current_file.tell()
                
                # Write the row
                current_writer.writerow(row)
                
                # Check if we need to start a new file
                current_size = current_file.tell()
                if current_size >= max_size_bytes:
                    current_file.close()
                    current_file = None
                    part_number += 1
        
        # Close the last file if it's open
        if current_file is not None:
            current_file.close()
        
        print(f"Successfully split {input_file} into {part_number} parts in {output_dir}")
        return part_number
    
    except Exception as e:
        print(f"Error splitting CSV file: {e}")
        # Close the current file if it's open
        if current_file is not None:
            current_file.close()
        raise

def main():
    parser = argparse.ArgumentParser(description='Split a large CSV file into smaller files')
    parser.add_argument('input_file', help='Path to the input CSV file')
    parser.add_argument('--output-dir', default='split_output', help='Directory to save the output files')
    parser.add_argument('--max-size', type=int, default=10, help='Maximum size of each output file in MB')
    parser.add_argument('--encoding', default='latin-1', help='Encoding of the input file (default: latin-1)')
    parser.add_argument('--drop-columns', nargs='+', help='Columns to drop from the CSV file')
    
    args = parser.parse_args()
    
    split_csv(args.input_file, args.output_dir, args.max_size, args.encoding, args.drop_columns)

if __name__ == "__main__":
    main() 
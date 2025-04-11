# CSV File Splitting Todo List

## Overview
Split the large `data.csv` file into smaller files (less than 10MB each) while preserving the header in each file.

## Tasks

- [x] Create a Python script to handle the CSV splitting
- [x] Set up a folder structure for the output files
- [x] Implement logic to read the large CSV file in chunks
- [x] Extract and save the header row from the original CSV
- [x] Create a function to write new CSV files with the header
- [x] Implement file size tracking to ensure each output file is under 10MB
- [x] Add error handling for file operations
- [x] Add progress reporting during the splitting process
- [ ] Test the script with a small sample of the data
- [ ] Run the script on the full `data.csv` file
- [ ] Verify that all output files have the correct header
- [ ] Verify that all output files are under 10MB
- [x] Document the process and script usage

## Implementation Notes

- Use Python's built-in `csv` module for reading and writing CSV files
- Consider using `pandas` for more efficient handling of large datasets
- Implement a counter to track the number of rows written to each file
- Use a consistent naming convention for the output files (e.g., `data_part_1.csv`, `data_part_2.csv`, etc.)
- Consider adding a command-line interface for flexibility 
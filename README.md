# CSV File Splitter

A Python utility for splitting large CSV files into smaller files while preserving the header in each file.

## Features

- Split large CSV files into smaller files (less than 10MB by default)
- Preserve the header in each output file
- Drop specific columns before splitting
- Support for different file encodings
- Command-line interface for easy use

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Installation

No installation required. Simply download the `split_csv.py` script to your local machine.

## Usage

### Basic Usage

```bash
python split_csv.py data.csv
```

This will split `data.csv` into files smaller than 10MB and save them in a directory called `split_output`.

### Advanced Options

```bash
python split_csv.py data.csv --output-dir custom_output --max-size 5 --encoding latin-1 --drop-columns "Column1" "Column2"
```

#### Command-line Arguments

- `input_file`: Path to the input CSV file (required)
- `--output-dir`: Directory to save the output files (default: `split_output`)
- `--max-size`: Maximum size of each output file in MB (default: 10)
- `--encoding`: Encoding of the input file (default: `latin-1`)
- `--drop-columns`: Columns to drop from the CSV file (space-separated list)

### Examples

1. **Basic splitting**:
   ```bash
   python split_csv.py data.csv
   ```

2. **Custom output directory and file size**:
   ```bash
   python split_csv.py data.csv --output-dir my_files --max-size 5
   ```

3. **Drop specific columns**:
   ```bash
   python split_csv.py data.csv --drop-columns "PC用商品説明文" "スマートフォン用商品説明文"
   ```

4. **Specify encoding**:
   ```bash
   python split_csv.py data.csv --encoding cp1252
   ```

5. **Combine all options**:
   ```bash
   python split_csv.py data.csv --output-dir processed_data --max-size 8 --encoding shift-jis --drop-columns "Column1" "Column2"
   ```

## Output

The script will create a directory (default: `split_output`) containing the split CSV files. Each file will:
- Have the same header as the original file
- Be smaller than the specified maximum size
- Be named according to the pattern: `{original_filename}_part_{number}.csv`

## Troubleshooting

- **UnicodeDecodeError**: If you encounter encoding errors, try a different encoding with the `--encoding` parameter.
- **File not found**: Make sure the input file path is correct.
- **Permission denied**: Ensure you have write permissions for the output directory.

## License

This script is provided under the MIT License. 
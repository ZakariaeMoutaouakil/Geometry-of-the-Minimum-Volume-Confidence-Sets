# Function to preprocess the counts column
import re


def add_commas_to_counts(line: str) -> str:
    return re.sub(r'\[\s*(.*?)\s*]', lambda m: '[' + ', '.join(m.group(1).split()) + ']', line)


# Path to your TSV file
file_path = '../data/certification_output_50.tsv'

# Read and preprocess the file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Apply preprocessing to each line
preprocessed_lines = [add_commas_to_counts(line) for line in lines]

# Write the preprocessed lines to a new file (optional, or you can use StringIO to avoid creating a new file)
preprocessed_file_path = '../data/preprocessed_data.tsv'
with open(preprocessed_file_path, 'w') as file:
    file.writelines(preprocessed_lines)

# src/data/read_data.py
import pandas as pd

# Define the path to your text dataset
dataset_path = 'data/raw/amazon_cells_labelled.txt'  # Adjust the path and file name accordingly

# Read the text dataset into a DataFrame
with open(dataset_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Create a DataFrame with 'Text' and 'Label' columns


# Assign binary labels based on the content of the 'Text' column
df = pd.read_csv(dataset_path, header=None, names=['Text', 'Label'], delimiter='\t')


# Display the DataFrame
print(df)
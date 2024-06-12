import pandas as pd

# Load the dataset
file_path = '/mnt/data/Dataset .csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataset to understand its structure
data.head()

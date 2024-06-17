import pandas as pd

# Load the CSV file
csv_file_path = "../../../example.csv"
df = pd.read_csv(csv_file_path)

# Display the first few rows of the dataframe
print(df.head())

# Optionally, if you are in an interactive environment (e.g., Jupyter Notebook or an IDE with built-in support for DataFrame display), you can use:
# df.head()

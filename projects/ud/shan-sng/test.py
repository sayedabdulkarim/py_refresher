# import pandas as pd

# # Load the CSV file
# csv_file_path = "../../../example.csv"
# df = pd.read_csv(csv_file_path)

# # Display the first few rows of the dataframe
# print(df)

# # Optionally, if you are in an interactive environment (e.g., Jupyter Notebook or an IDE with built-in support for DataFrame display), you can use:
# # df.head()

import pandas as pd
from tabulate import tabulate

# Correct CSV file path
# csv_file_path = "../../../example.csv"
xlsx_file_path = "../../../Data_Train.xlsx"
df = pd.read_excel(xlsx_file_path)

# Display the dataframe in a table format ( GET DATA )
print(tabulate(df.head(50), headers='keys', tablefmt='psql'))

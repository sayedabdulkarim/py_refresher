import numpy as np;
import pandas as pd;

data = pd.read_html("https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/")

# print(type(data))
print(data[0])
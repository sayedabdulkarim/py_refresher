import numpy as np;
import pandas as pd;

from numpy.random import randn

labels= ['a', 'b', 'c']
my_data = [10,20,30]
arr = np.array(my_data)
d = { 'a': 10, 'b': 20, 'c': 30 }
np.random.seed(101)

# test = pd.Series(labels)
# print(test)
# print(
#     labels,
#     my_data,
#     arr,
#     d
# )

df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

# print(df['Z'])
print(df > 0)
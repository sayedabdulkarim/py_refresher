import numpy as np;
import pandas as pd;

labels= ['a', 'b', 'c']
my_data = [10,20,30]
arr = np.array(my_data)
d = { 'a': 10, 'b': 20, 'c': 30 }


test = pd.Series(labels)
print(test)
# print(
#     labels,
#     my_data,
#     arr,
#     d
# )
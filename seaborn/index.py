import seaborn as sns;
import matplotlib.pyplot as plt

# %matplotlib inline

tips = sns.load_dataset("tips")

# print(tips.head())

# test = sns.displot(tips['total_bill'], kde=True, bins=30)
# print(test)
# sns.distplot(tips["total_bill"])

# Assuming 'tips' is a DataFrame you have already loaded with the necessary data
test = sns.displot(tips['total_bill'], kde=True, bins=30)

# This will display the plot if it doesn't show up automatically
plt.show()

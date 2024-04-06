import matplotlib.pyplot as plt;
import numpy as np;

x = np.linspace(0,5,11)
y = x ** 2

print(x, " xxxx")
print(y, " yyyy")

plt.plot(x, y, 'orange')
plt.xlabel("X LABEL")
plt.ylabel("Y LABEL")
plt.title("TITLE")

plt.show()
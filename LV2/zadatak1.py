import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 3, 3, 2, 1], float)
y = np.array([1, 1, 2, 2, 1], float)

plt.axis([0, 4, 0, 4])
plt.title("Primjer")
plt.xlabel("x os")
plt.ylabel("y os")

plt.scatter(x, y, color="b")
plt.plot(x, y, color="b", linewidth=1.5)
plt.show()

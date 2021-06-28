import numpy as np
import matplotlib.pyplot as plt

load_matrix = np.loadtxt("matrix.txt")

plt.matshow(load_matrix)
plt.show()

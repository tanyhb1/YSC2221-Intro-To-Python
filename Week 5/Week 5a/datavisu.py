import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,14,100)
print(x)
y1 = np.cos(x)
y2 = np.sin(x)
plt.figure(1)
#subplotting where 4 is no. of rows, 3 is no. of col, 1 is where to place current plot
plt.subplot(431)
plt.plot(x,y1, "og", label="sine")
plt.figure(2)
plt.subplot(439)
plt.plot(x,y2,"--b", label="cosine")
plt.legend(loc="upper right")
plt.title('Sine and Cosine curves')
plt.ylim(-1.5,1.5)
plt.show()
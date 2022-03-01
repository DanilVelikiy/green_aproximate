import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(1, 8, 20)
y = np.sin(x)

t = np.polyfit(x, y, 4)

f = np.poly1d(t)

print(f)

plt.grid()

plt.plot(x, y, 'o', x, f(x), 'b')

plt.show()
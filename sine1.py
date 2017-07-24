import matplotlib.pyplot as plt
import numpy as np


f = 5
Ampli = 2

x = np.linspace(0,1,100)
y = Ampli * np.sin(2 * np.pi * f * x )
plt.plot(x, y)
plt.xlabel('voltage(V)')
plt.ylabel('sample(n)')
plt.show()

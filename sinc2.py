import matplotlib.pyplot as plt
import numpy as np

f = np.arange(-10, 10, 0.01)

plt.plot(f, np.sinc(f-5)+np.sinc(f+5))
plt.show()
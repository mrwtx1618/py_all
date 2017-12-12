# -*- coding:UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
I1 = np.linspace(0.05,0.1, 101)
k1 = 0.05769/(I1 - 0.0077)
plt.plot(I1,k1)
I2 = np.linspace(0,0.05,101)
k2 = (I2 + 0.0077)/(I2 - 0.0077)
print I2
print k2
plt.plot(I2,k2)
plt.xlabel('Increase of SZ50')
plt.ylabel('k')
plt.show()
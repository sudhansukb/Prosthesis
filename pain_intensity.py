"""
Here the script is use to plot the pain intensity 
in a particular point over four weeks

"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(6)
y = np.arange(5)
z = x * y[:, np.newaxis]

for i in range(5):
    if i == 0:
        p = plt.imshow(z)
        fig = plt.gcf()
        plt.clim()   # clamp the color limits
        plt.title("Pain intensity")
    else:
        z = z + 2
        p.set_data(z)

    print("Pain week", i)
    plt.pause(1)

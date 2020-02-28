from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

dt = np.dtype([('temp', np.uint16)])
data = np.fromfile("gpt\\depth-1582100142.924865.hex",dt)
Z = np.asarray(data).reshape((60, 80))

#ax = plt.axes(projection='3d')
x = np.linspace(-6, 6, 80)
y = np.linspace(-6, 6, 60)
X, Y = np.meshgrid(x, y)

#print (np.argwhere(np.isnan(Z.astype(int))))     


fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z.astype(int))
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('depth');
plt.show()


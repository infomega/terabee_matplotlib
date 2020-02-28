#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from openni import openni2
from datetime import datetime
import platform
import numpy as np
import array
from PIL import Image
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib import cm

# Initialize OpenNI
if platform.system() == "Windows":
    openni2.initialize("C:/Program Files (x86)/OpenNI2/Redist")  # Specify path for Redist
else:
    openni2.initialize()  # can also accept the path of the OpenNI redistribution

# Connect and open device
dev = openni2.Device.open_any()

# Create depth stream
depth_stream = dev.create_depth_stream()
depth_stream.start()
#outfile = open("depth-"+str(datetime.timestamp(datetime.now())) + ".hex","wb")
#while True:
x = np.linspace(-8, 8, 80)
y = np.linspace(-6, 6, 60)
X, Y = np.meshgrid(x, y)

#print (np.argwhere(np.isnan(Z.astype(int))))     


fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('depth');

while True:
    frame = depth_stream.read_frame()
    frame_data = frame.get_buffer_as_uint16()
    Z = 400 - np.asarray(frame_data).reshape((60, 80))
    ax.plot_surface(X, Y, Z.astype(int))
    plt.pause(1)
    ax.cla()


plt.draw()


#print(depth_array)
#outfile.write(depth_array)
#outfile.close()
#    print("Center pixel distance is {} mm".format(frame_data[2440]))
depth_stream.stop()
openni2.unload()
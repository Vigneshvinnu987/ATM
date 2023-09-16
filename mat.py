import matplotlib.pyplot as plt
import numpy as np
# (0,6) (0,250) = (0,0),(6,250)
xpoints = np.array([0,6,10,20]) # You can use the default x values you mention only the y axis
ypoints = np.array([0,7,100,45])
plt.plot(xpoints,ypoints,marker = "*",ms = 20,mec = "black",mfc = "red",ls = "dotted",color = "Green",lw=10 )
# Using o its view only the points
# marker keyword use the you disign the point
# ms mean marker size
# mec means marker coloer
# mfc means marker face color
# ls means line size
# lw means line width
plt.title("Example all")
plt.xlabel("horizondal label")
plt.ylabel("vertical label")
plt.show()
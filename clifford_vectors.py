# displays a quiver plot of vectors for a differential equation
# at each denoted x, y coordinate. 

# import third party libraries
import numpy as np 
import matplotlib.pyplot as plt 

plt.style.use('dark_background')

x = np.arange(10.65, 11.2, 1/90)
y = np.arange(7.5, 8.4, 1/30)

a = -1.4
b = 1.7
c = 1.0
d = 0.7

X, Y = np.meshgrid(x, y)

dx = np.sin(a*Y) + c*np.cos(a*X)
dy = np.sin(b*X) + d*np.cos(b*Y)
color_array = 2*(np.abs(dx) + np.abs(dy))

fig, ax = plt.subplots(figsize = (40, 40))

ax.quiver(X, Y, dx, dy, color_array, scale = 20)
ax.axis([10.65, 11.2, 7.5, 8.4])

plt.show()
plt.close()
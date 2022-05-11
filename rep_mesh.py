import numpy as np
from mayavi import mlab

x = np.loadtxt('EX.txt')
y = np.loadtxt('EY.txt')
z = np.loadtxt('EZ.txt')

pts = mlab.points3d(x, y, z, z, scale_mode='none', scale_factor=0.2)
mesh = mlab.pipeline.delaunay2d(pts)
surf = mlab.pipeline.surface(mesh)
mlab.savefig(filename='mesh_avec_limites_franges.jpg')
mlab.show()
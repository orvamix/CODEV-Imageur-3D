import pickle
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

with open("coord", "rb") as fp:   # Unpickling
    Mat_fin= pickle.load(fp)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x =[item[0] for item in Mat_fin]
y =[item[1] for item in Mat_fin]
z =[item[2] for item in Mat_fin]



ax.scatter(x, y, z, c='r', marker='o',s=0.1)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
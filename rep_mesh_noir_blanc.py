#Import Libraries
from PIL.Image import*
from PIL import Image, ImageDraw
from colormap import rgb2hex
import matplotlib.pyplot as plt
import numpy as np
import time
start_time = time.process_time()
#Read image
img2=Image.open('screen_mesh_manuel.jpg')

img = img2.convert('L')
width, height = img.size
B = img.resize((round(min(width, height)/10),round(min(width,height)/10)),resample=Image.BILINEAR)
C = B.resize((1024,768), Image.NEAREST)
C.save('1024x768_representation.jpg')
img3 = open('1024x768_representation.jpg')

[X,Y] = np.meshgrid(np.linspace(0-512,1024-512,1024),np.linspace(0-384,768-384,768))

M = []

for k in range(768):
    M.append([])
    for j in range(1024):
        Z = img3.getpixel((j,k))-174.2
        M[k].append(Z)


plt.figure();
z_min, z_max = -75, 75
plt.pcolor(X,Y,M, cmap='gray')
plt.axis([X.min(), X.max(), Y.min(), Y.max()])
plt.colorbar()

print(time.process_time() - start_time, "seconds")  # fin mesure temps d'éxecusion






        
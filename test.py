# -*- coding: utf-8 -*-

from fringe_detector import *
import numpy as np
#JSON pour lire paramètres
import json
f = open('info.json')
info = json.load(f)
N=info['N']
uRzoom=info['uRzoom']
vRzoom=info['vRzoom']

Mat = zeros((uRzoom,vRzoom), dtype=int)

for i in range(2**5):
    LC=fringe_detector(i,N,uRzoom,vRzoom)
    Mat+=LC
# affichage 
plt.figure()
plt.imshow(Mat, cmap = plt.get_cmap('gray'))
plt.title('Image frange')
plt.xlabel('vR pixels')
plt.ylabel('uR pixels')
plt.show()

np.savetxt("mat.txt", Mat.astype(int), fmt='%5.0f', delimiter=",")
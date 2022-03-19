# -*- coding: utf-8 -*-
# On importe le module matplotlib qui permet de générer des graphiques 2D et 3D

import matplotlib.pyplot as plt
from fringe_detector import *
from coord3D_objet import *
import numpy as np
import pickle
#JSON pour lire paramètres
import json
f = open('info.json')
info = json.load(f)
N=info['N']
uRzoom=info['uRzoom']
vRzoom=info['vRzoom']


Mat_temp=[]
Mat_fin=[]

# fringe_detector("IRZoom",N,uRzoom,vRzoom)

PosD=np.loadtxt('results/PosiDroiteIRZoom.txt')

for i in range(1, 2**N):
    v_e=(i+1)*vRzoom/(2**N)
    for j in range(len(PosD)):
        for k in range(len(PosD[j])):
            if PosD[j][k]== i:
                Mat_temp.append([j+1,k+1,v_e])

for i in range(len(Mat_temp)):
    Mat_fin.append(coord3D(Mat_temp[i][0],Mat_temp[i][1],Mat_temp[i][2]).tolist())
    
with open("mat.txt", 'w') as output:
    for row in Mat_fin:
        output.write(str(row) + '\n')

with open("coord", "wb") as fp:   #Pickling
    pickle.dump(Mat_fin, fp)


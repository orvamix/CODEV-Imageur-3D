# -*- coding: utf-8 -*-
# On importe le module matplotlib qui permet de générer des graphiques 2D et 3D

import matplotlib.pyplot as plt
# from fringe_detector import *
# from coord3D_objet import *
import numpy as np
import pickle
#JSON pour lire paramètres
import json
from numpy import meshgrid, sqrt, linspace, savetxt, absolute
from mpl_toolkits.mplot3d import Axes3D

import time
start_time = time.process_time()

f = open('info.json')
info = json.load(f)
N=5
uRzoom=info['uRzoom']
vRzoom=info['vRzoom']

def coord3D(u,v, v_e):
    ME=np.loadtxt('ME.txt')
    MR=np.loadtxt('MR.txt')
    
    coord_px=np.array([u,v,v_e])
    G=np.array([[MR[2][0]*coord_px[0], MR[2][1]*coord_px[0], MR[2][2]*coord_px[0]], [MR[2][0]*coord_px[1], MR[2][1]*coord_px[1], MR[2][2]*coord_px[1]], [ME[2][0]*coord_px[2], ME[2][1]*coord_px[2], ME[2][2]*coord_px[2]]])
    G=np.subtract(G,np.array([[MR[0][0], MR[0][1], MR[0][2]], [MR[1][0], MR[1][1], MR[1][2]], [ME[1][0], ME[1][1], ME[1][2]]]))
    coord_pxx=np.array([[MR[2][3]*coord_px[0]], [MR[2][3]*coord_px[1]], [ME[2][3]*coord_px[2]]])
    H=np.subtract(np.array([[MR[0][3]],[MR[1][3]],[ME[1][3]]]),coord_pxx)
    G_inv=np.linalg.inv(G)
    M = np.matmul(G_inv, H)
    return M



Mat_temp=[]
Mat_fin=[]

#fringe_detector("IRZoom",N,uRzoom,vRzoom)

PosD=np.loadtxt('resultats/PosiglobalIRZoom.txt')


for i in range(1, (2**N)+1):
    if i%2 == 0:
        v_e=((vRzoom/2**N)*(i))
        for j in range(len(PosD)):
            for k in range(len(PosD[j])):
                if PosD[j][k]==i:
                    Mat_temp.append([j+1,k+1,v_e])
                    
    else :
        v_e=((i*vRzoom)/(2**N))+1
        for j in range(len(PosD)):
            for k in range(len(PosD[j])):
                if PosD[j][k]==i:
                    Mat_temp.append([j+1,k+1,v_e])
                    
                    
        

for i in range(len(Mat_temp)):
    Mat_fin.append(coord3D(Mat_temp[i][0],Mat_temp[i][1],Mat_temp[i][2]).tolist())


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x =[item[0][0] for item in Mat_fin]
y =[item[1][0] for item in Mat_fin]
z =[item[2][0] for item in Mat_fin]


savetxt('EX.txt', x, fmt='%-7.6f')   
savetxt('EY.txt', y, fmt='%-7.6f')
savetxt('EZ.txt', z, fmt='%-7.6f')


ax.scatter(x, y, z, c='r', marker='o',s=0.1)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

print(time.process_time() - start_time, "seconds")  # fin mesure temps d'éxecusion
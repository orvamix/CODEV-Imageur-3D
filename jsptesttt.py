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
    
def fct_MRN(MR):
    a = MR[2][3]
    return MR/a

def coord2D(u,v,Z):
    MR=np.loadtxt('MR.txt')
    MRN = fct_MRN(MR)
    
    coord_px=np.array([u,v])
    V = np.array([[MRN[2][0]*coord_px[0] - MRN[0][0], MRN[2][1]*coord_px[0] - MRN[0][1]], [MRN[2][0]*coord_px[1] - MRN[1][0], MRN[2][1]*coord_px[1] - MRN[1][1]]])
    W = np.array([[(MRN[0][2] - MRN[2][2]*coord_px[0])*Z - MRN[2][3]*coord_px[0] + MRN[0][3]], [(MRN[1][2] - MRN[2][2]*coord_px[1])*Z - MRN[2][3]*coord_px[1] + MRN[1][3]]])
    
    V_inv=np.linalg.inv(V)
    N = np.matmul(V_inv, W)
    return N


#Mat_temp=[]
#Mat_fin=[]

#fringe_detector("IRZoom",N,uRzoom,vRzoom)

#PosD=np.loadtxt('resultats/PosiglobalIRZoom.txt')


#for i in range(1, (2**N)+1):
#    if i%2 == 0:
#        for j in range(len(PosD)):
#            for k in range(len(PosD[j])):
#                if PosD[j][k]==i:
#                    Mat_temp.append([j+1,k+1])
#                    
#    else :
#        for j in range(len(PosD)):
#            for k in range(len(PosD[j])):
#                if PosD[j][k]==i:
#                    Mat_temp.append([j+1,k+1])
#                    
#                    
#        
#
#for i in range(len(Mat_temp)):
#    Mat_fin.append(coord2D(Mat_temp[i][0],Mat_temp[i][1]).tolist())
#
#
#x =[item[0][0] for item in Mat_fin]
#y =[item[1][0] for item in Mat_fin]
#
#plt.plot(x, y)


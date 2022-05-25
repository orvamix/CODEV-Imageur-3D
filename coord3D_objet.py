# -*- coding: utf-8 -*-
# On importe le module matplotlib qui permet de générer des graphiques 2D et 3D

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tkinter.filedialog import *
# from fringe_detector import *
# from coord3D_objet import *
import numpy as np
import pickle
#JSON pour lire paramètres
import json
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

def coord3D_objet(N=5):
    Mat_temp=[]
    Mat_fin=[]

    #fringe_detector("IRZoom",N,uRzoom,vRzoom)

    PosD=np.loadtxt('resultats/PosiglobalIRZoom.txt')


    for i in range(1, (2**N)+1):
        if i//2 ==0 or i==0:
            v_e=(i)*vRzoom/(2**N)
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
                        
    print(len(Mat_temp))
            

    for i in range(len(Mat_temp)):
        Mat_fin.append(coord3D(Mat_temp[i][0],Mat_temp[i][1],Mat_temp[i][2]).tolist())
        
    with open("resultats/mat.txt", 'w') as output:
        for row in Mat_fin:
            output.write(str(row) + '\n')

    with open("resultats/coord.codev", "wb") as fp:   #Pickling
        pickle.dump(Mat_fin, fp)
    
    x =[item[0] for item in Mat_fin]
    y =[item[1] for item in Mat_fin]
    z =[item[2] for item in Mat_fin]
    
    with open("EX.txt", 'w') as output:
        for row in x:
            output.write(str(row[0]) + ' ')
    with open("EY.txt", 'w') as output:
        for row in y:
            output.write(str(row[0]) + ' ')
    with open("EZ.txt", 'w') as output:
        for row in z:
            output.write(str(row[0]) + ' ')
        
    return True

def affichage():
    filepath = askopenfilename(title="Ouvrir le fichier",filetypes=[("Fichiers CODEV",".codev")])
    with open(filepath, "rb") as fp:   # Unpickling
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

if __name__ == "__main__":
    coord3D_objet()
import pickle
import numpy as np
from numpy.linalg import inv
import jsptesttt as jsp

def calculateur(points,nom_base_imageur,nom_base_objet):
    B = np.array([[0 for i in range (11)]])
    c = np.array([[0]])
    x = np.array([])
    M = np.array([])
    
    for i in range (len(points)) :
        Z=float(points["point"+str(i)][nom_base_objet][2])
        U=float(points["point"+str(i)][nom_base_imageur][0])
        V=float(points["point"+str(i)][nom_base_imageur][1])
        X=jsp.coord2D(U, V, Z)[0][0]
        Y=jsp.coord2D(U, V, Z)[1][0]
        
        B=np.concatenate((B,[[X,Y,Z,1,0,0,0,0,-U*X,-U*Y,-U*Z],[0,0,0,0,X,Y,Z,1,-V*X,-V*Y,-V*Z]]),axis=0)
        c=np.concatenate((c,np.array([[U]])))
        c=np.concatenate((c,np.array([[V]])))
    B=B[1:]
    c=c[1:]
    
    x = np.dot(np.dot(inv(np.dot(np.transpose(B),B)),np.transpose(B)),c)
    x = np.concatenate((x,[[1]]))
    M = [[x[i][0] for i in range(4)],[x[i+4][0] for i in range(4)],[x[i+8][0] for i in range(4)]]
    return M

def sauve(matrice, nom):
    np.savetxt(nom, matrice, fmt='%-7.0f')
    
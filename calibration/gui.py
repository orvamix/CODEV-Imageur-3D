import tkinter as tk
from tkinter.filedialog import *
import pickle
import numpy as np
from numpy.linalg import inv

#Définition du dictionnaire "points"
#"point2":
#   "emetteur":[u,v]
#   "objet_emetteur":[X,Y,Z]
#   "recepteur"[u,v]

points_MR={}
points_ME={}
nbr_points_MR=18
nbr_points_ME=24

def calcul_MR():
    global points_MR
    B = np.array([[0 for i in range (11)]])
    c = np.array([[0]])
    x = np.array([])
    MR = np.array([])
    print(points_MR)
    for i in range (len(points_MR)) :
        X=float(points_MR["point"+str(i)]["objet_recepteur"][0])
        Y=float(points_MR["point"+str(i)]["objet_recepteur"][1])
        Z=float(points_MR["point"+str(i)]["objet_recepteur"][2])
        U=float(points_MR["point"+str(i)]["recepteur"][0])
        V=float(points_MR["point"+str(i)]["recepteur"][1])
        B=np.concatenate((B,[[X,Y,Z,1,0,0,0,0,-U*X,-U*Y,-U*Z],[0,0,0,0,X,Y,Z,1,-V*X,-V*Y,-V*Z]]),axis=0)
        c=np.concatenate((c,np.array([[U]])))
        c=np.concatenate((c,np.array([[V]])))
    B=B[1:]
    c=c[1:]
    
    x = np.dot(np.dot(inv(np.dot(np.transpose(B),B)),np.transpose(B)),c)
    x = np.concatenate((x,[[1]]))
    MR = [[x[i][0] for i in range(4)],[x[i+4][0] for i in range(4)],[x[i+8][0] for i in range(4)]]
    print("MR =",MR)


def calcul_ME():
    global points_ME
    B = np.array([[0 for i in range (11)]])
    c = np.array([[0]])
    x = np.array([])
    ME = np.array([])
    for i in range (len(points_ME)) :
        X=float(points_ME["point"+str(i)]["objet_emetteur"][0])
        Y=float(points_ME["point"+str(i)]["objet_emetteur"][1])
        Z=float(points_ME["point"+str(i)]["objet_emetteur"][2])
        U=float(points_ME["point"+str(i)]["emetteur"][0])
        V=float(points_ME["point"+str(i)]["emetteur"][1])
        B=np.concatenate((B,[[X,Y,Z,1,0,0,0,0,-U*X,-U*Y,-U*Z],[0,0,0,0,X,Y,Z,1,-V*X,-V*Y,-V*Z]]),axis=0)
        c=np.concatenate((c,np.array([[U]])))
        c=np.concatenate((c,np.array([[V]])))
    B=B[1:]
    c=c[1:]
    
    x = np.dot(np.dot(inv(np.dot(np.transpose(B),B)),np.transpose(B)),c)
    x = np.concatenate((x,[[1]]))
    ME = [[x[i][0] for i in range(4)],[x[i+4][0] for i in range(4)],[x[i+8][0] for i in range(4)]]
    print("ME =",ME)


def calcul_calibration():
    calcul_MR()
    calcul_ME()



def calibration(option=""):
    if(option!="calcul"):
        cal_fenetre()
    else:
        calcul_calibration()





if __name__ == "__main__":
    calibration()
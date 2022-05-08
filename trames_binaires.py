# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 09:59:46 2018

@author: Elisabeth Lys
"""
import time
start_time = time.process_time() # début mesure temps d'éxecusion
# On importe le module numpy qui permet de faire du calcul numérique
import numpy as np
from numpy import linspace, zeros, savetxt, sin, pi, uint8
# On importe le module matplotlib qui permet de générer des graphiques 2D et 3D
import matplotlib.pyplot as plt
from skimage import io    

def main(N=6,filepath="img_proj/Trame"):
    # Définition du nombre de trames
        
    #----- Paramètre LCD ---------------
    #Taille en pixel
    NbHE=1024; #sur horizontal
    NbVE=768;  #sur vertical
        
    x = linspace(0,NbHE-1,NbHE)
    y = linspace(0,NbVE-1,NbVE)
        
    #Coordonnées matricielles des pts mE du LCD
    vE,uE = np.meshgrid(x,y)
        
    B = zeros((NbVE,NbHE), dtype = np.uint8)

    #Création des N trames
    for k in range(0,N):
        #trame d'ordre k
        IE = 1*((sin(vE*2**(k+1)*pi/NbHE))<0) #Expression mathématique
        r = 255*IE    
        g = 0*IE
        b = 0*IE

        B = np.dstack((r,g,b))
        B = uint8(B)
        #enregistrement
        A = filepath + str(k+1) + '.bmp'
        io.imsave(A,B)    

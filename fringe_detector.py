# -*- coding: utf-8 -*-
# On importe le module matplotlib qui permet de générer des graphiques 2D et 3D
import matplotlib.pyplot as plt
#from skimage import io, transform
from skimage import io
# On importe le module numpy qui permet de faire du calcul numérique
import numpy as np
from numpy import loadtxt, zeros, ones

"""
return numpy matrix
"""
def fringe_detector(C,N,uRzoom,vRzoom):
    #Numéro base binaire de la frange à localiser
    Cbin = np.binary_repr(C, N)

    #On créé la matrice IRzoom
    IRzoom = zeros((uRzoom,vRzoom,N))

    #On charge les images IRZoom et on les binarises
    for k in range (0,N):
        #------ Chargement des images d'intensité IRZoom de l'objet dans le repere recepteur ---  
        Nom = 'IRZoom' + str(k+1) + '.bmp'
        img = io.imread('img_cam/'+Nom)
        # Seuillage de l'image
        threshold = 125
        idx = img[:,:,0] > threshold
        img[idx,0] = 255
        IRz = (img/255)
        #Matrice normalisée  
        # On enregistre les IRzoom_1 2 3 ... dans IR_zoom
        IRzoom[:,:,k] = IRz[:,:,0]
        IRzoom = IRzoom.astype(int) # on passe du type float au type int

        #Libération mémoire
        Nom = None
        R = None
        
    # ----------------------Localisation de la frange C 
        
    #On initialise les variales LClogic et LC
    LClogic = ones((uRzoom,vRzoom), dtype=bool) 
    LC = zeros((uRzoom,vRzoom), dtype=int)

    # On transforme le nombre binaire en une liste dont on peut chercher les éléments un à un
    tabCbin = list(map(int, Cbin))#Attention modification de la fonction avec Python3/ python2

    # Localisation de la frange C 
    LClogic = IRzoom[:,:,0]==tabCbin[0]
    for l in range (1,N):
        LClogic = LClogic & (IRzoom[:,:,l]==tabCbin[l])

    #Matrice de localisation numérique 
    return LClogic*C
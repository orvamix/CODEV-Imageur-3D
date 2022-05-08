# -*- coding: utf-8 -*-
#from skimage import io, transform
from skimage import io
from skimage import filters
from skimage.morphology import disk
# On importe le module numpy qui permet de faire du calcul numérique
import numpy as np
from numpy import loadtxt, zeros, ones, savetxt, empty

"""
return numpy matrix
"""
def fringe_detector(img_name,N,uRzoom,vRzoom):
    #On créé la matrice IRzoom
    IRzoom = zeros((uRzoom,vRzoom,N))
    Posiglobal = zeros((uRzoom,vRzoom))
    PosiGauche = zeros((uRzoom,vRzoom))
    PosiDroite = zeros((uRzoom,vRzoom))

    # chargement de l'image puis binarisation 
    for k in range (0,N):
        #------ Chargement des images d'intensité IRZoom de l'objet dans le repere recepteur ---  
        Nom = 'img_cam/'+ img_name + str(k+1) + '.bmp'
        img = io.imread(Nom)
        # Seuillage de l'image
        threshold = 125
        idx = img[:,:,0] > threshold
        img[idx,0] = 255
        IRz = (img/255)
            # On enregistre les IRzoom_1 2 3 ... dans IR_zoom
        #IRz[:,:,0] = filters.median(IRz[:,:,0], disk(5))
        IRzoom[:,:,k] = IRz[:,:,0]

    #Libération mémoire
    Nom = None
    R = None     

    # ----------------------Localisation de la frange C 
        
    #On initialise les variales LClogic et LC 
    LC_num = empty((uRzoom,vRzoom))
    LClogic = ones((uRzoom,vRzoom), dtype=bool) 

    LC = zeros((uRzoom,vRzoom))
    for C in range (1,2**N+1,2):
        #Numéro base binaire de la frange à localiser
        Cbin = np.binary_repr(C, N)
        
        # On transforme le nombre binaire en une liste dont on peut chercher les éléments un à un
        tabCbin = list(map(int, Cbin)) 
        
        # Localisation de la frange C impaire
        LClogic = IRzoom[:,:,0]==tabCbin[0]
        for l in range (1,N):
            LClogic = LClogic & (IRzoom[:,:,l]==tabCbin[l])
     
        #Matrice de localisation numérique 
        LC = LClogic*1
        
        # Filtrage médian sur les images des franges permet de nettoyer les petites imperfections
        LC = filters.median(np.uint8(LC),disk(5))

        for i in range (0,uRzoom): #NbHRzoom
            p0 = np.nonzero(LC[i,:]==1)[0]
            if len(p0) > 0: 
                aG = p0[0] # first element -> début de frange
                aD = p0[-1] # last element -> fin de frange
                # on concatène les position 
                # Position G et D
                Posiglobal[i,aG] = C 
                Posiglobal[i,aD] = C+1 
                #on concatène les position gauche avec les positions G existantes
                PosiGauche[i,aG] = C
                #on concatène les position droite avec les positions D existantes
                PosiDroite[i,aD] = C+1

    #Enregistrement 
    savetxt('resultats/PosiGauche'+img_name+'.txt', PosiGauche, fmt='%-7.0f')
    savetxt('resultats/PosiDroite'+img_name+'.txt', PosiDroite, fmt='%-7.0f')
    savetxt('resultats/Posiglobal'+img_name+'.txt', Posiglobal, fmt='%-7.0f')

    #Inversion de contraste pour l'affichage
    InvPosiglobal=1.-Posiglobal

    #Enregistrement image des cotes de franges
    couleur_cotes = np.asarray([255,255,255])  #Blanc intensitee maximale
    B = zeros((uRzoom,vRzoom,3))

    A = 'Cotes_franges'+img_name+'.bmp'
    B[:,:,0] = couleur_cotes[0]*InvPosiglobal
    B[:,:,1] = couleur_cotes[1]*InvPosiglobal
    B[:,:,2] = couleur_cotes[2]*InvPosiglobal
    B=B.astype(np.uint8)
    io.imsave(A,B)
    
    return B
    
if __name__ == "__main__":
    fringe_detector("IRZoom",5,1200,1300)
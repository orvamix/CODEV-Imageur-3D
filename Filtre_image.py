import numpy as np
from PIL import Image
from matplotlib import image
import matplotlib.pyplot as plt


def DCouleur(couleur_1,couleur_2):
    Couleur1=np.array(couleur_1)
    Couleur2=np.array(couleur_2)
    return (((Couleur1[0]-Couleur2[0])**2)+((Couleur1[1]-Couleur2[1])**2)+((Couleur1[2]-Couleur2[2])**2))**0.5

image1 = image.imread('IRZoom_bruit4.bmp')
image2 = image.imread('Mire_damier.bmp')
image3 = image.imread('IRZoom4.jpg')

def ceil(x):
    if int(x)==x:
        return(x)
    else:
        return int(x+1)

def ContrasteMax(picture):
    image=np.copy(picture)
    W=image.shape[0]
    H=image.shape[1]
    Rmax=1
    Gmax=1
    Bmax=1
    for i in range(W):
        for j in range(H):
            if image[i,j,0]>=Rmax:
                Rmax=image[i,j,0]
            if image[i,j,1]>=Gmax:
                Gmax=image[i,j,1]
            if image[i,j,2]>=Bmax:
                Bmax=image[i,j,2]
    print("Rmax=",Rmax,", Gmax=",Gmax,", Bmax=",Bmax)
    for i in range(W):
        for j in range(H):
            image[i,j,0]=int(255*(image[i,j,0]/Rmax))
            image[i,j,1]=int(255*(image[i,j,1]/Gmax))
            image[i,j,2]=int(255*(image[i,j,2]/Bmax))
    return image

def Nettoyage(image_entree,image_ref,segX,segY,tolerance=15):
    ref=np.copy(image_ref)
    image=np.copy(image_entree)
    rendu=np.copy(image_entree)
    couleurREF=np.array([0,0,0])
    couleur_R=couleurREF
    couleur_D=np.array([255,255,255])
    C=0
    W=image.shape[0]
    H=image.shape[1]
    dX=int(W/segX)
    dY=int(H/segY)
    Frontiere=[]
    C_avant=np.zeros(3,dtype=int)
    C_arriere=np.zeros(3,dtype=int)
    C_haut=np.zeros(3,dtype=int)
    C_bas=np.zeros(3,dtype=int)
    Rmed=0
    Gmed=0
    Bmed=0
    Medianes=np.zeros([segX+ceil(W-(segX*dX)),segY+ceil(H-(segY*dY)),3],dtype=int)
    #Création du tableau des couleurs médianes de chaque région de l'image
    for i in range(Medianes.shape[0]):
        for j in range(Medianes.shape[1]):
            Rmed=0
            Gmed=0
            Bmed=0
            for x in range(i*dX,min((i+1)*dX,W)):
                for y in range(j*dY,min((j+1)*dY,H)):
                    Rmed+=image[x,y,0]
                    Gmed+=image[x,y,1]
                    Bmed+=image[x,y,2]
            Rmed=int(Rmed/max(((min((i+1)*dX,W)-(i*dX))*((min((j+1)*dY,H))-(j*dY))),1))
            Gmed=int(Gmed/max(((min((i+1)*dX,W)-(i*dX))*((min((j+1)*dY,H))-(j*dY))),1))
            Bmed=int(Bmed/max(((min((i+1)*dX,W)-(i*dX))*((min((j+1)*dY,H))-(j*dY))),1))
            Medianes[i,j,0]=int(Rmed)
            Medianes[i,j,1]=int(Gmed)
            Medianes[i,j,2]=int(Bmed)
    #Recherche de la couleur principale de la projection
    while DCouleur(couleurREF,np.array([0,0,0]))<10:
        couleurREF=ref[1,C]
        C+=1
    couleur_D=couleurREF
    #Recherche de la couleur des zones illuminées de la projection et de la couleur des zones qui ne le sont pas
    for i1 in range(Medianes.shape[0]):
        for j1 in range(Medianes.shape[1]):
            if DCouleur(Medianes[i1,j1],couleurREF)<DCouleur(couleur_R,couleurREF):
                couleur_R = Medianes[i1,j1]
            if DCouleur(Medianes[i1,j1],couleurREF)>DCouleur(couleurREF,couleur_D) and list(Medianes[i1,j1])!=list(np.array([0,0,0])):
                couleur_D=Medianes[i1,j1]
    #Recherche des zones monochromes
    #for i2 in range(Medianes.shape[0]):
        #for j2 in range(Medianes.shape[1]):
            #if DCouleur(Medianes[i2,j2],np.array([0,0,0]))>10:
                #if DCouleur(Medianes[i2,j2],couleur_R)<tolerance:
                    #for x2 in range(i2*dX,min((i2+1)*dX,W)):
                        #for y2 in range(j2*dY,min((j2+1)*dY,H)):
                            #rendu[x2,y2]=couleur_R
                #elif DCouleur(Medianes[i2,j2],couleur_D)<tolerance:
                    #for x2 in range(i2*dX,min((i2+1)*dX,W)):
                        #for y2 in range(j2*dY,min((j2+1)*dY,H)):
                            #rendu[x2,y2]=couleur_D
                #else:
                    #Frontiere.append(np.array([i2,j2]))
    #print(Frontiere)
    #plt.imshow(rendu)
    #plt.show()
    #Recherche zone par zone des frontières
#    for i2 in range(Medianes.shape[0]):
#        for j2 in range(Medianes.shape[1]):
#            if DCouleur(Medianes[i2,j2],np.array([0,0,0]))>3:
#                if [i2,j2]==[0,0]:
#
#                elif [i2,j2]==[Medianes.shape[0]-1,0]:
#
#                elif [i2,j2]==[0,Medianes.shape[1]-1]:
#
#                elif [i2,j2]==[Medianes.shape[0]-1,Medianes.shape[1]-1]:
#
#                elif i2==0:#
#
#                elif i2==Medianes.shape[0]-1:
#
#                elif j2==0:
#
#                elif j2==Medianes.shape[1]-1:
#
#                else:
#                    if DCouleur(Medianes[i2-1,j2],couleur_R)<DCouleur(Medianes[i2-1,j2],couleur_D) and DCouleur(Medianes[i2-1,j2],couleur_R)<DCouleur(Medianes[i2-1,j2],np.array([0,0,0])):
#                        C_arriere=couleur_R
#                    else:
#                        C_arriere=couleur_D
#                    if DCouleur(Medianes[i2+1,j2],couleur_R)<DCouleur(Medianes[i2+1,j2],couleur_D) and DCouleur(Medianes[i2+1,j2],couleur_R)<DCouleur(Medianes[i2+1,j2],np.array([0,0,0])):
#                        C_avant=couleur_R
#                    else:
#                        C_avant=couleur_D
#                    if DCouleur(Medianes[i2,j2-1],couleur_R)<DCouleur(Medianes[i2,j2-1],couleur_D) and DCouleur(Medianes[i2,j2-1],couleur_R)<DCouleur(Medianes[i2,j2-1],np.array([0,0,0])):
#                        C_haut=couleur_R
#                    else:
#                        C_haut=couleur_D
#                    if DCouleur(Medianes[i2,j2+1],couleur_R)<DCouleur(Medianes[i2,j2+1],couleur_D) and DCouleur(Medianes[i2,j2+1],couleur_R)<DCouleur(Medianes[i2,j2+1],np.array([0,0,0])):
#                        C_bas=couleur_R
#                    else:
#                        C_bas=couleur_D
#                    if C_arriere==C_avant and C_arriere==C_haut and C_arriere==C_bas:

def filtre_median(image_entree,tailleX=5,tailleY=5):
    image=np.copy(image_entree)
    rendu=np.zeros([image.shape[0],image.shape[1],3],dtype=int)
    W=image.shape[0]
    H=image.shape[1]
    deltaX=tailleX
    deltaY=tailleY
    if tailleX%2==0:
        deltaX=tailleX/2
    else:
        deltaX=(tailleX+1)/2
    if tailleY%2==0:
        deltaY=tailleY/2
    else:
        deltaY=(tailleY+1)/2
    zoneR=[]
    zoneG=[]
    zoneB=[]
    zoneR0=[]
    zoneG0=[]
    zoneB0=[]
    R=0
    G=0
    B=0
    Rmoy=0
    Gmoy=0
    Bmoy=0
    l=0
    for i in range(W):
        for j in range(H):
            zoneR=[]
            zoneG=[]
            zoneB=[]
            zoneR0=[]
            zoneG0=[]
            zoneB0=[]
            R=0
            G=0
            B=0
            Rmoy=0
            Gmoy=0
            Bmoy=0
            for di in range(int(max(0,i-deltaX)),int(min(W-1,i+deltaX))):
                for dj in range(int(max(0,j-deltaY)),int(min(H-1,j+deltaY))):
                    zoneR0.append(image[di,dj,0])
                    zoneG0.append(image[di,dj,1])
                    zoneB0.append(image[di,dj,2])
            l=0
            while zoneB0!=[]:
                n=0
                l=0
                while l<len(zoneR0):
                    if zoneR0[l]<=zoneR0[n]:
                        n=l
                    l+=1
                zoneR.append(zoneR0[n])
                zoneG.append(zoneG0[n])
                zoneB.append(zoneB0[n])
                del zoneR0[n]
                del zoneG0[n]
                del zoneB0[n]
            if len(zoneR)%2==0:
                Rmoy=np.average(np.array(zoneR))
                Gmoy=np.average(np.array(zoneG))
                Bmoy=np.average(np.array(zoneB))
                if DCouleur(np.array([zoneR[(int(len(zoneR)/2))],zoneG[(int(len(zoneR)/2))],zoneB[(int(len(zoneR)/2))]]),np.array([Rmoy,Gmoy,Bmoy])) <= DCouleur(np.array([zoneR[(int(len(zoneR)/2)-1)],zoneG[(int(len(zoneR)/2)-1)],zoneB[(int(len(zoneR)/2)-1)]]),np.array([Rmoy,Gmoy,Bmoy])):
                    rendu[i,j,0]=zoneR[(int(len(zoneR)/2))]
                    rendu[i,j,1]=zoneG[(int(len(zoneR)/2))]
                    rendu[i,j,2]=zoneB[(int(len(zoneR)/2))]
                else:
                    rendu[i,j,0]=zoneR[((int(len(zoneR)/2))-1)]
                    rendu[i,j,1]=zoneG[((int(len(zoneR)/2))-1)]
                    rendu[i,j,2]=zoneB[((int(len(zoneR)/2))-1)]
            else:
                rendu[i,j,0]=zoneR[(int(len(zoneR)/2))]
                rendu[i,j,1]=zoneG[(int(len(zoneR)/2))]
                rendu[i,j,2]=zoneB[(int(len(zoneR)/2))]
        P=(i/W)*100
        print(str(P)+"%")
    return rendu


def filtre_median_iteration(image_entree,n=4,tailleX=5,tailley=5):
    image=np.copy(image_entree)
    for i in range(n):
        image=filtre_median(image,tailleX=5,tailleY=5)
    plt.imshow(image)
    plt.show()






















# -*- coding: utf-8 -*-
# On importe le module matplotlib qui permet de générer des graphiques 2D et 3D
import matplotlib.pyplot as plt
from fringe_detector import *
import numpy as np
#JSON pour lire paramètres
import json
f = open('info.json')
info = json.load(f)
N=info['N']
uRzoom=info['uRzoom']
vRzoom=info['vRzoom']


B=fringe_detector(N,uRzoom,vRzoom)
#Affichage de l'image enregistrée des positions globales des franges
plt.figure()
plt.imshow(B[:,:,1], cmap = plt.get_cmap('gray'))
plt.title('Image des cotés des franges')
plt.xlabel('vRzoom pixels')
plt.ylabel('uRzomm pixels')

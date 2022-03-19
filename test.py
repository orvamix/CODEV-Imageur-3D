# -*- coding: utf-8 -*-
# On importe le module matplotlib qui permet de générer des graphiques 2D et 3D
import matplotlib.pyplot as plt
from fringe_detector import *
from coor3D_objet import *
import numpy as np
#JSON pour lire paramètres
import json
f = open('info.json')
info = json.load(f)
N=info['N']
uRzoom=info['uRzoom']
vRzoom=info['vRzoom']


# fringe_detector(N,uRzoom,vRzoom)
coord_r=np.loadtxt('results/PosiGauche.txt')
for i in range(2**N):
    v_e=(vRzoom*i/(2**N))+1
    coord3D()
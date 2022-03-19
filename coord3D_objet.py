import numpy as np


def coord3D(u,v, v_e):
    ME=np.loadtxt('ME.txt')
    MR=np.loadtxt('MR.txt')
    
    coord_px=np.array([u,v,v_e])
    G=np.array([[MR[2][0], MR[2][0], ME[2][0]], [MR[2][1], MR[2][1], ME[2][1]], [MR[2][2], MR[2][2], ME[2][2]]])*coord_px-np.array([[MR[0][0], MR[1][0], ME[1][0]], [MR[0][1], MR[1][1], ME[1][1]], [MR[0][2], MR[1][2], ME[1][2]]])
    H=np.array([MR[0][3],MR[1][3],ME[1][3]])-coord_px
    G_inv=np.linalg.inv(G)
    return np.matmul(G_inv, H)
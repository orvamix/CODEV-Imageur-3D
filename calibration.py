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

def cal_fenetre():
    global points
    fenetre_cal = tk.Toplevel()
    fenetre_cal.title("Calibration")
    

    
    fen_point=[]
    fen_point_v=[]
    fen_point_f=[]
    
    sb_emet= [tk.StringVar(value=0) for x in range(2*nbr_points_ME)] 
    sb_obj_r=[tk.StringVar(value=0) for x in range(3*nbr_points_MR)] 
    sb_obj_e=[tk.StringVar(value=0) for x in range(3*nbr_points_ME)] 
    sb_recept=[tk.StringVar(value=0) for x in range(2*nbr_points_MR)] 
    
    
    
    def load():
        global points_MR
        global points_ME
        # filepath = askopenfilename(title="Ouvrir le fichier",filetypes=[("Fichiers CODEV",".codev")])
        with open('points_coord_ME.codev', "rb") as fp:   # Unpickling
            points_ME= pickle.load(fp)
        for i in range(nbr_points_ME):
            sb_emet[i*2].set(points_ME["point"+str(i)]["emetteur"][0])
            sb_emet[i*2+1].set(points_ME["point"+str(i)]["emetteur"][1])
            sb_obj_e[i*3].set(points_ME["point"+str(i)]["objet_emetteur"][0])
            sb_obj_e[i*3+1].set(points_ME["point"+str(i)]["objet_emetteur"][1])
            sb_obj_e[i*3+2].set(points_ME["point"+str(i)]["objet_emetteur"][2])
            
        with open('points_coord_MR.codev', "rb") as fp:   # Unpickling
            points_MR= pickle.load(fp)
        # for i in range(nbr_points_MR):
            # sb_emet[i*2].set(points_MR["point"+str(i)]["emetteur"][0])
            # sb_emet[i*2+1].set(points_MR["point"+str(i)]["emetteur"][1])
            # sb_obj_r[i*3].set(points_MR["point"+str(i)]["objet_recepteur"][0])
            # sb_obj_r[i*3+1].set(points_MR["point"+str(i)]["objet_recepteur"][1])
            # sb_obj_r[i*3+2].set(points_MR["point"+str(i)]["objet_recepteur"][2])
        fenetre_cal.update()
    
    def save():
        filepath=asksaveasfilename(title="Enregistrer le fichier",initialfile="points_coord",defaultextension="codev",filetypes=[("Fichiers CODEV",".codev")])
        for i in range(9):
            thisdict = {
              "emetteur": [sb_emet[i*2].get(),sb_emet[i*2+1].get()],
              "objet": [sb_obj[i*3].get(),sb_obj[i*3+1].get(),sb_obj[i*3+2].get()],
              "recepteur": [sb_recept[i*2].get(),sb_recept[i*2+1].get()]
            }
            nom="point"+str(i)
            points[nom]=thisdict
        with open(filepath, "wb") as fp:   #Pickling
            pickle.dump(points, fp)    
            
    
    
    
    
    #Divise en deux horizontalement -> un coté 6 points et un côté calcul+info
    f_glob=tk.PanedWindow(fenetre_cal, orient=tk.HORIZONTAL)
    f_glob.pack(side=tk.TOP, expand=tk.Y, fill=tk.BOTH, pady=2, padx=2)
    f_info=tk.PanedWindow(fenetre_cal, orient=tk.VERTICAL)
    f_info.pack(side=tk.TOP, expand=tk.Y, fill=tk.BOTH, pady=2, padx=2)
    
    #Les 6 points
    point_f=tk.Frame(f_glob, borderwidth=2)
    f_glob.add(point_f)
    for ligne in range(9):
        fen_point.append(tk.LabelFrame(point_f, text="Point n°"+str(ligne+1)))
        fen_point[ligne].pack(fill="both", expand="yes")
        fen_point_v.append(tk.PanedWindow(fen_point[ligne], orient=tk.HORIZONTAL))
        fen_point_v[ligne].pack(side=tk.TOP, expand=tk.Y, fill=tk.BOTH, pady=2, padx=2)
        #émetteur
        fen_point_f.append(tk.Frame(fen_point_v[ligne], borderwidth=2, relief=tk.GROOVE))
       #█ tk.Label(fen_point_f[ligne*3], text="Émetteur").pack()
        
        tk.Entry(fen_point_f[ligne*3],textvariable=sb_emet[ligne*2]).pack()
        tk.Entry(fen_point_f[ligne*3],textvariable=sb_emet[ligne*2+1]).pack()
        
        fen_point_v[ligne].add(fen_point_f[ligne*3])
        
        #objet
        fen_point_f.append(tk.Frame(fen_point_v[ligne], borderwidth=2, relief=tk.GROOVE))
       # tk.Label(fen_point_f[ligne*3+1], text="Objet").pack()
        tk.Entry(fen_point_f[ligne*3+1],textvariable=sb_obj_e[ligne*3]).pack()
        tk.Entry(fen_point_f[ligne*3+1],textvariable=sb_obj_e[ligne*3+1]).pack()
        tk.Entry(fen_point_f[ligne*3+1],textvariable=sb_obj_e[ligne*3+2]).pack()
        fen_point_v[ligne].add(fen_point_f[ligne*3+1])
        
        #objet
        fen_point_f.append(tk.Frame(fen_point_v[ligne], borderwidth=2, relief=tk.GROOVE))
        #tk.Label(fen_point_f[ligne*3+2], text="Récepteur").pack()
        tk.Entry(fen_point_f[ligne*3+2],textvariable=sb_recept[ligne*2]).pack()
        tk.Entry(fen_point_f[ligne*3+2],textvariable=sb_recept[ligne*2+1]).pack()
        fen_point_v[ligne].add(fen_point_f[ligne*3+2])
        
        
        fen_point_v[ligne].pack()
    
    #Boutons sauvegarde et chargement
    boutons=tk.Frame(point_f)
    tk.Button(boutons, text="Sauver",command=save).pack(side='right')
    tk.Button(boutons, text="Charger",command=load).pack(side='right')
    boutons.pack()
    #Calculs
    f_calc=tk.LabelFrame(f_info, text="Calculs")
    tk.Button(f_calc, text="Calculer MR et ME",command=calcul_calibration).pack()
    f_info.add(f_calc)
    #Informations
    f_cotation=tk.LabelFrame(f_info, text="Informations")
    tk.Label(f_cotation, text="Longueur").pack()
    f_info.add(f_cotation)
    
    f_glob.add(f_info)
    
    #Menubar
    menubar = tk.Menu(fenetre_cal)

    menu1 = tk.Menu(menubar, tearoff=0)
    menu1.add_command(label="Charger", command=load)
    menu1.add_command(label="Sauver", command=save)
    menu1.add_command(label="Quitter", command=fenetre_cal.quit)
    menubar.add_cascade(label="Menu", menu=menu1)

    menu2 = tk.Menu(menubar, tearoff=0)
    menu2.add_command(label="Calculer MR et ME",command=calcul_calibration)
    menubar.add_cascade(label="Calculer", menu=menu2)

    fenetre_cal.config(menu=menubar)
    
    
    #Mainloop
    fenetre_cal.mainloop()

def calibration(option=""):
    if(option!="calcul"):
        cal_fenetre()
    else:
        calcul_calibration()





if __name__ == "__main__":
    calibration()
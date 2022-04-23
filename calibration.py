import tkinter as tk
from tkinter.filedialog import *
import pickle

#Définition du dictionnaire "points"
#"point2":
#   "emetteur":[u,v]
#   "objet":[X,Y,Z]
#   "recepteur"[u,v]

points={}

def cal_fenetre():
    global points
    fenetre_cal = tk.Toplevel()
    fenetre_cal.title("Calibration")
    
    fen_point=[]
    fen_point_v=[]
    fen_point_f=[]
    
    sb_emet= [tk.StringVar(value=0) for x in range(12)] 
    sb_obj=[tk.StringVar(value=0) for x in range(18)] 
    sb_recept=[tk.StringVar(value=0) for x in range(12)] 
    
    
    
    def load():
        filepath = askopenfilename(title="Ouvrir le fichier",filetypes=[("Fichiers CODEV",".codev")])
        with open(filepath, "rb") as fp:   # Unpickling
            points= pickle.load(fp)
        for i in range(6):
            sb_emet[i*2].set(points["point"+str(i)]["emetteur"][0])
            sb_emet[i*2+1].set(points["point"+str(i)]["emetteur"][1])
            sb_obj[i*3].set(points["point"+str(i)]["objet"][0])
            sb_obj[i*3+1].set(points["point"+str(i)]["objet"][1])
            sb_obj[i*3+2].set(points["point"+str(i)]["objet"][2])
            sb_recept[i*2].set(points["point"+str(i)]["recepteur"][0])
            sb_recept[i*2+1].set(points["point"+str(i)]["recepteur"][1])
        fenetre_cal.update()
    
    def save():
        filepath=asksaveasfilename(title="Enregistrer le fichier",initialfile="points_coord",defaultextension="codev",filetypes=[("Fichiers CODEV",".codev")])
        for i in range(6):
            thisdict = {
              "emetteur": [sb_emet[i*2].get(),sb_emet[i*2+1].get()],
              "objet": [sb_obj[i*3].get(),sb_obj[i*3+1].get(),sb_obj[i*3+2].get()],
              "recepteur": [sb_recept[i*2].get(),sb_recept[i*2+1].get()]
            }
            nom="point"+str(i)
            points[nom]=thisdict
        with open(filepath, "wb") as fp:   #Pickling
            pickle.dump(points, fp)    
            
    
    
    
    
    
    f_glob=tk.PanedWindow(fenetre_cal, orient=tk.HORIZONTAL)
    f_glob.pack(side=tk.TOP, expand=tk.Y, fill=tk.BOTH, pady=2, padx=2)
    point_f=tk.Frame(f_glob, borderwidth=2)
    f_glob.add(point_f)
    for ligne in range(6):
        fen_point.append(tk.LabelFrame(point_f, text="Point "+str(ligne+1)))
        fen_point[ligne].pack(fill="both", expand="yes")
        fen_point_v.append(tk.PanedWindow(fen_point[ligne], orient=tk.HORIZONTAL))
        fen_point_v[ligne].pack(side=tk.TOP, expand=tk.Y, fill=tk.BOTH, pady=2, padx=2)
        #émetteur
        fen_point_f.append(tk.Frame(fen_point_v[ligne], borderwidth=2, relief=tk.GROOVE))
        tk.Label(fen_point_f[ligne*3], text="Émetteur").pack()
        
        tk.Entry(fen_point_f[ligne*3],textvariable=sb_emet[ligne*2]).pack()
        tk.Entry(fen_point_f[ligne*3],textvariable=sb_emet[ligne*2+1]).pack()
        
        fen_point_v[ligne].add(fen_point_f[ligne*3])
        
        #objet
        fen_point_f.append(tk.Frame(fen_point_v[ligne], borderwidth=2, relief=tk.GROOVE))
        tk.Label(fen_point_f[ligne*3+1], text="Objet").pack()
        tk.Entry(fen_point_f[ligne*3+1],textvariable=sb_obj[ligne*3]).pack()
        tk.Entry(fen_point_f[ligne*3+1],textvariable=sb_obj[ligne*3+1]).pack()
        tk.Entry(fen_point_f[ligne*3+1],textvariable=sb_obj[ligne*3+2]).pack()
        fen_point_v[ligne].add(fen_point_f[ligne*3+1])
        
        #objet
        fen_point_f.append(tk.Frame(fen_point_v[ligne], borderwidth=2, relief=tk.GROOVE))
        tk.Label(fen_point_f[ligne*3+2], text="Récepteur").pack()
        tk.Entry(fen_point_f[ligne*3+2],textvariable=sb_recept[ligne*2]).pack()
        tk.Entry(fen_point_f[ligne*3+2],textvariable=sb_recept[ligne*2+1]).pack()
        fen_point_v[ligne].add(fen_point_f[ligne*3+2])
        
        
        fen_point_v[ligne].pack()
    
    boutons=tk.Frame(point_f)
    tk.Button(boutons, text="Sauver",command=save).pack(side='right')
    tk.Button(boutons, text="Charger",command=load).pack(side='right')
    boutons.pack()
    info_f=tk.LabelFrame(f_glob, text="Informations")
    tk.Label(info_f, text="Longueur").pack()
    f_glob.add(info_f)
    
    
    fenetre_cal.mainloop()


def calibration():
    cal_fenetre()
    





if __name__ == "__main__":
    calibration()
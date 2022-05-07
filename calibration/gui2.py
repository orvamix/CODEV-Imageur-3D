import tkinter as tk
from tkinter.filedialog import *
from PIL import Image, ImageTk

root = tk.Toplevel()
root.title("Calibration")
root.attributes('-fullscreen', True)
w, h = root.winfo_screenwidth(), root.winfo_screenheight()

position=0
points_objet=[tk.StringVar(value=0) for x in range(3)] 
points_emetteur=[tk.StringVar(value=0) for x in range(2)]

def ME():
    
    global root
    
    #Divion en deux
    p = tk.PanedWindow(root, orient=tk.HORIZONTAL)
    p.pack(side=tk.TOP, expand=tk.Y, fill=tk.BOTH, pady=2, padx=2)
    
    #======== Partie gauche — entrée coordonnées ======
    gauche=tk.Frame(p)
    f_coord=tk.Frame(gauche)
    def entree_coord():
        global position
        for widget in f_coord.winfo_children():
            widget.destroy()

        l = tk.LabelFrame(f_coord, text="Point "+str(position))
        test=tk.Label(l, text="A l'intérieure de la frame").pack(fill="both", expand="yes")
        l.pack()
        root.update()
        f_coord.pack()
        
    def entree_coord_g():
        global position
        position=position-1
        entree_coord()
    def entree_coord_d():
        global position
        position=position+1
        entree_coord()
    def nouveau():
        pass
    def supprimer():
        pass

    
    #Boutons
    g_lst_bt=tk.Frame(gauche)
    b_supprimer = tk.Button(g_lst_bt, text ="-").pack(side=tk.LEFT)
    b_precedent = tk.Button(g_lst_bt, text="←",command=entree_coord_g).pack(side=tk.LEFT)
    b_suivant = tk.Button(g_lst_bt, text="→",command=entree_coord_d).pack(side=tk.LEFT)
    b_nouveau = tk.Button(g_lst_bt, text ="+").pack(side=tk.LEFT)
    g_lst_bt.pack()
    
    entree_coord()
    
    #======= Partie droite — image =====
    photo = Image.open("Mire_damier.png")
    test = ImageTk.PhotoImage(photo)

    droite = tk.Label(p, image=test)
    droite.image = test
    
    
    
    #On pack tout ça
    p.add(gauche)
    p.add(droite)
    p.pack()
def MR():
    pass


def main():
    global root
    
    
   
    
    cadre1 = tk.Frame(root)
    
    def nettoyage():
        for widget in cadre1.winfo_children():
            widget.destroy()
    
    def gui_ME():
        nettoyage()
        ME()
    def gui_MR():
        nettoyage()
        MR()
    
    
    cadre1.pack()
    cadre1.place(anchor="c", relx=.5, rely=.5)
    b1 = tk.Button(cadre1, text ="ME", command=gui_ME).pack()
    b2 = tk.Button(cadre1, text ="MR", command=gui_MR).pack()
    
    #Menubar
    menubar = tk.Menu(root)
    menu1 = tk.Menu(menubar, tearoff=0)
    menu1.add_command(label="Calcul de ME", )
    menu1.add_command(label="Calcul de MR", )
    menu1.add_command(label="Quitter", command=root.quit)
    menubar.add_cascade(label="Menu", menu=menu1)
    root.config(menu=menubar)
    
    def fun(event):
        if(event.keysym=='Escape'):
            root.destroy()

    root.bind("<KeyRelease>", fun)
    root.mainloop()

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

if __name__ == "__main__":
    main()
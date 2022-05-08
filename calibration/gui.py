import tkinter as tk
from tkinter.filedialog import *
from PIL import Image, ImageTk
import pickle
import matrices
import numpy as np

root = tk.Toplevel()
root.title("Calibration")
# root.attributes('-fullscreen', True)
w, h = root.winfo_screenwidth(), root.winfo_screenheight()

cadre1 = tk.Frame(root)

ME_position=0
ME_points_objet=[tk.StringVar(value=0) for x in range(3)] 
ME_points_emetteur=[tk.StringVar(value=0) for x in range(2)]
ME_points={}
message=tk.StringVar(value="Bienvenue dans la calibration! \n")

def ME():
    
    global cadre1
    global message
    
    #Divion en deux
    p = tk.PanedWindow(cadre1, orient=tk.HORIZONTAL)
    p.pack(side=tk.TOP, expand=tk.Y, fill=tk.BOTH, pady=2, padx=2)
    
    #======== Partie gauche — entrée coordonnées ======
    
    gauche=tk.Frame(p)
    
    #DialogBox
    text_box = tk.Text(gauche,height=12,width=40)    
    
    
    f_coord=tk.Frame(gauche)
    def entree_coord():
        global ME_position
        global ME_points_objet
        global ME_points_emetteur
        for widget in f_coord.winfo_children():
            widget.destroy()

        l = tk.LabelFrame(f_coord, text="Point "+str(int(ME_position+1)))
        l1=tk.Frame(l)
        tk.Label(l1, text="Émetteur").pack()
        tk.Entry(l1,textvariable=ME_points_emetteur[int(ME_position)*2]).pack()
        tk.Entry(l1,textvariable=ME_points_emetteur[int(ME_position)*2+1]).pack()
        
        l2=tk.Frame(l)
        tk.Label(l2, text="Objet").pack()
        tk.Entry(l2,textvariable=ME_points_objet[int(ME_position)*3]).pack()
        tk.Entry(l2,textvariable=ME_points_objet[int(ME_position)*3+1]).pack()
        tk.Entry(l2,textvariable=ME_points_objet[int(ME_position)*3+2]).pack()
        
        l1.pack(side=tk.LEFT)
        l2.pack(side=tk.RIGHT)
        l.pack(side=tk.TOP)
        f_coord.pack()
        root.update()
        
        
    def entree_coord_g():
        global ME_position
        if(ME_position>0):
            ME_position=ME_position-1
        else:
            ME_position=0
        entree_coord()
    def entree_coord_d():
        global ME_position
        if(ME_position<len(ME_points_emetteur)/2-1):
            ME_position=ME_position+1
        else:
            ME_position=len(ME_points_emetteur)/2-1
        entree_coord()
    def nouveau():
        global ME_points_objet
        global ME_points_emetteur
        global ME_position
        ME_points_objet=ME_points_objet+[tk.StringVar(value=0) for x in range(3)]
        ME_points_emetteur=ME_points_emetteur+[tk.StringVar(value=0) for x in range(2)]
        ME_position=len(ME_points_emetteur)/2-1
        entree_coord()
    def supprimer():
        global ME_points_objet
        global ME_points_emetteur
        global ME_position
        if(ME_position==0):
            return
        else:
            del ME_points_objet[(int(ME_position)*2-1):(int(ME_position*2))]
            del ME_points_emetteur[(int(ME_position)*3-1):(int(ME_position*3)+1)]
        ME_position=ME_position-1
        entree_coord()

    def sauver():
        global message
        global ME_points
        global ME_points_objet
        global ME_points_emetteur
        filepath=asksaveasfilename(title="Enregistrer le fichier",initialfile="ME_points",defaultextension="codev",filetypes=[("Fichiers CODEV",".codev")])
        for i in range(int(len(ME_points_emetteur)/2)):
            thisdict = {
              "emetteur": [ME_points_emetteur[i*2].get(),ME_points_emetteur[i*2+1].get()],
              "objet": [ME_points_objet[i*3].get(),ME_points_objet[i*3+1].get(),ME_points_objet[i*3+2].get()],
            }
            nom="point"+str(i)
            ME_points[nom]=thisdict
        with open(filepath, "wb") as fp:   #Pickling
            pickle.dump(ME_points, fp)  
        
        message.set(message.get()+str(len(ME_points))+" points sauvés dans : "+filepath+"\n")
        text_box.delete(1.0,"end")
        text_box.insert(1.0, message.get())
        
    def charger():
        global ME_points
        global ME_points_objet
        global ME_points_emetteur
        global message
        filepath = askopenfilename(title="Ouvrir le fichier",filetypes=[("Fichiers CODEV",".codev")])
        with open(filepath, "rb") as fp:   # Unpickling
            ME_points= pickle.load(fp)
        
        ME_points_objet=ME_points_objet+[tk.StringVar(value=0) for x in range(3)]*(len(ME_points)-1)
        ME_points_emetteur=ME_points_emetteur+[tk.StringVar(value=0) for x in range(2)]*(len(ME_points)-1)
        for i in range(len(ME_points)):
            ME_points_emetteur[i*2].set(ME_points["point"+str(i)]["emetteur"][0])
            ME_points_emetteur[i*2+1].set(ME_points["point"+str(i)]["emetteur"][1])
            ME_points_objet[i*3].set(ME_points["point"+str(i)]["objet"][0])
            ME_points_objet[i*3+1].set(ME_points["point"+str(i)]["objet"][1])
            ME_points_objet[i*3+2].set(ME_points["point"+str(i)]["objet"][2])
            
        message.set(message.get()+str(len(ME_points))+" points chargés\n")
        text_box.delete(1.0,"end")
        text_box.insert(1.0, message.get())
        entree_coord()
    
    def calculer():
        M=matrices.calculateur(ME_points,"emetteur","objet")
        matrices.sauve(M,"ME")
        message.set(str(M)+"\n")
        text_box.delete(1.0,"end")
        text_box.insert(1.0, message.get())
    
    #Boutons
    g_lst_bt3=tk.Frame(gauche)
    b_charger = tk.Button(g_lst_bt3, text ="calculer ME",command=calculer).pack(side=tk.LEFT)
    g_lst_bt3.pack()
    
    g_lst_bt2=tk.Frame(gauche)
    b_charger = tk.Button(g_lst_bt2, text ="Charger",command=charger).pack(side=tk.LEFT)
    b_sauver = tk.Button(g_lst_bt2, text="Sauver",command=sauver).pack(side=tk.LEFT)
    
    g_lst_bt=tk.Frame(gauche)
    b_supprimer = tk.Button(g_lst_bt, text ="-",command=supprimer).pack(side=tk.LEFT)
    b_precedent = tk.Button(g_lst_bt, text="←",command=entree_coord_g).pack(side=tk.LEFT)
    b_suivant = tk.Button(g_lst_bt, text="→",command=entree_coord_d).pack(side=tk.LEFT)
    b_nouveau = tk.Button(g_lst_bt, text ="+",command=nouveau).pack(side=tk.LEFT)
    g_lst_bt2.pack()
    g_lst_bt.pack()
    
    #TextBox
    text_box.pack(expand=True,side=tk.BOTTOM)
    text_box.insert(1.0, message.get())
       
    
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
    
MR_position=0
MR_points_objet=[tk.StringVar(value=0) for x in range(3)] 
MR_points_recepteur=[tk.StringVar(value=0) for x in range(2)]
MR_points={}

def MR():
    
    global cadre1
    global message
    
    #Divion en deux
    p = tk.PanedWindow(cadre1, orient=tk.HORIZONTAL)
    p.pack(side=tk.TOP, expand=tk.Y, fill=tk.BOTH, pady=2, padx=2)
    
    #======== Partie gauche — entrée coordonnées ======
    
    gauche=tk.Frame(p)
    
    #DialogBox
    text_box = tk.Text(gauche,height=12,width=40)    
    
    
    f_coord=tk.Frame(gauche)
    def entree_coord():
        global MR_position
        global MR_points_objet
        global MR_points_recepteur
        for widget in f_coord.winfo_children():
            widget.destroy()

        l = tk.LabelFrame(f_coord, text="Point "+str(int(MR_position+1)))
        l1=tk.Frame(l)
        tk.Label(l1, text="Récepteur").pack()
        tk.Entry(l1,textvariable=MR_points_recepteur[int(MR_position)*2]).pack()
        tk.Entry(l1,textvariable=MR_points_recepteur[int(MR_position)*2+1]).pack()
        
        l2=tk.Frame(l)
        tk.Label(l2, text="Objet").pack()
        tk.Entry(l2,textvariable=MR_points_objet[int(MR_position)*3]).pack()
        tk.Entry(l2,textvariable=MR_points_objet[int(MR_position)*3+1]).pack()
        tk.Entry(l2,textvariable=MR_points_objet[int(MR_position)*3+2]).pack()
        
        l2.pack(side=tk.LEFT)
        l1.pack(side=tk.RIGHT)
        l.pack(side=tk.TOP)
        f_coord.pack()
        root.update()
        
        
    def entree_coord_g():
        global MR_position
        if(MR_position>0):
            MR_position=MR_position-1
        else:
            MR_position=0
        entree_coord()
    def entree_coord_d():
        global MR_position
        if(MR_position<len(MR_points_recepteur)/2-1):
            MR_position=MR_position+1
        else:
            MR_position=len(MR_points_recepteur)/2-1
        entree_coord()
    def nouveau():
        global MR_points_objet
        global MR_points_recepteur
        global MR_position
        MR_points_objet=MR_points_objet+[tk.StringVar(value=0) for x in range(3)]
        MR_points_recepteur=MR_points_recepteur+[tk.StringVar(value=0) for x in range(2)]
        MR_position=len(MR_points_recepteur)/2-1
        entree_coord()
    def supprimer():
        global MR_points_objet
        global MR_points_recepteur
        global MR_position
        if(MR_position==0):
            return
        else:
            del MR_points_objet[(int(MR_position)*2-1):(int(MR_position*2))]
            del MR_points_recepteur[(int(MR_position)*3-1):(int(MR_position*3)+1)]
        MR_position=MR_position-1
        entree_coord()

    def sauver():
        global message
        global MR_points
        global MR_points_objet
        global MR_points_recepteur
        filepath=asksaveasfilename(title="Enregistrer le fichier",initialfile="MR_points",defaultextension="codev",filetypes=[("Fichiers CODEV",".codev")])
        for i in range(int(len(MR_points_recepteur)/2)):
            thisdict = {
              "recepteur": [MR_points_recepteur[i*2].get(),MR_points_recepteur[i*2+1].get()],
              "objet": [MR_points_objet[i*3].get(),MR_points_objet[i*3+1].get(),MR_points_objet[i*3+2].get()],
            }
            nom="point"+str(i)
            MR_points[nom]=thisdict
        with open(filepath, "wb") as fp:   #Pickling
            pickle.dump(MR_points, fp)  
        
        message.set(message.get()+str(len(MR_points))+" points sauvés dans : "+filepath+"\n")
        text_box.delete(1.0,"end")
        text_box.insert(1.0, message.get())
        
    def charger():
        global MR_points
        global MR_points_objet
        global MR_points_recepteur
        global message
        filepath = askopenfilename(title="Ouvrir le fichier",filetypes=[("Fichiers CODEV",".codev")])
        with open(filepath, "rb") as fp:   # Unpickling
            MR_points= pickle.load(fp)
        
        MR_points_objet=MR_points_objet+[tk.StringVar(value=0) for x in range(3)]*(len(MR_points)-1)
        MR_points_recepteur=MR_points_recepteur+[tk.StringVar(value=0) for x in range(2)]*(len(MR_points)-1)
        for i in range(len(MR_points)):
            MR_points_recepteur[i*2].set(MR_points["point"+str(i)]["recepteur"][0])
            MR_points_recepteur[i*2+1].set(MR_points["point"+str(i)]["recepteur"][1])
            MR_points_objet[i*3].set(MR_points["point"+str(i)]["objet"][0])
            MR_points_objet[i*3+1].set(MR_points["point"+str(i)]["objet"][1])
            MR_points_objet[i*3+2].set(MR_points["point"+str(i)]["objet"][2])
            
        message.set(message.get()+str(len(MR_points))+" points chargés\n")
        text_box.delete(1.0,"end")
        text_box.insert(1.0, message.get())
        entree_coord()
    
    def calculer():
        M=matrices.calculateur(MR_points,"recepteur","objet")
        matrices.sauve(M,"MR")
        message.set(str(M)+"\n")
        text_box.delete(1.0,"end")
        text_box.insert(1.0, message.get())
    
    #Boutons
    g_lst_bt3=tk.Frame(gauche)
    b_charger = tk.Button(g_lst_bt3, text ="calculer MR",command=calculer).pack(side=tk.LEFT)
    g_lst_bt3.pack()
    
    g_lst_bt2=tk.Frame(gauche)
    b_charger = tk.Button(g_lst_bt2, text ="Charger",command=charger).pack(side=tk.LEFT)
    b_sauver = tk.Button(g_lst_bt2, text="Sauver",command=sauver).pack(side=tk.LEFT)
    
    g_lst_bt=tk.Frame(gauche)
    b_supprimer = tk.Button(g_lst_bt, text ="-",command=supprimer).pack(side=tk.LEFT)
    b_precedent = tk.Button(g_lst_bt, text="←",command=entree_coord_g).pack(side=tk.LEFT)
    b_suivant = tk.Button(g_lst_bt, text="→",command=entree_coord_d).pack(side=tk.LEFT)
    b_nouveau = tk.Button(g_lst_bt, text ="+",command=nouveau).pack(side=tk.LEFT)
    g_lst_bt2.pack()
    g_lst_bt.pack()
    
    #TextBox
    text_box.pack(expand=True,side=tk.BOTTOM)
    text_box.insert(1.0, message.get())
       
    
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


def main():
    global cadre1
    
    
    
    
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
    menu1.add_command(label="Calcul de ME", command=gui_ME)
    menu1.add_command(label="Calcul de MR", command=gui_MR)
    menu1.add_command(label="Quitter", command=root.quit)
    menubar.add_cascade(label="Menu", menu=menu1)
    root.config(menu=menubar)
    
    def fun(event):
        if(event.keysym=='Escape'):
            root.destroy()

    root.bind("<KeyRelease>", fun)
    root.mainloop()


if __name__ == "__main__":
    main()
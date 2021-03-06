import tkinter as tk
from tkinter import messagebox
from coord3D_objet import *
from fringe_detector import *
import camera_projecteur as cp
import trames_binaires as tb
import json

import threading
import time

f = open('info.json')
info = json.load(f)
N=info['N']
uRzoom=info['uRzoom']
vRzoom=info['vRzoom']


def parametres():
    
    global N
    global uRzoom
    global vRzoom
    
    root=tk.Toplevel()
    root.title("Paramètres")
    E_uRzoom=tk.StringVar(value=uRzoom)
    E_vRzoom=tk.StringVar(value=vRzoom)
    f1=tk.Frame(root)
    tk.Label(f1, text="uRzoom=").pack(side=tk.LEFT)
    tk.Entry(f1,textvariable=E_uRzoom).pack(side=tk.LEFT)
    f1.pack(side=tk.TOP)
    f2=tk.Frame(root)
    tk.Label(f2, text="vRzoom=").pack(side=tk.LEFT)
    tk.Entry(f2,textvariable=E_vRzoom).pack(side=tk.LEFT)
    f2.pack(side=tk.TOP)
    
    def sauver():
        global N
        global uRzoom
        global vRzoom
        with open('info.json', 'r+') as f:
            data = json.load(f)
            data['uRzoom'] = int(E_uRzoom.get()) 
            data['vRzoom'] = int(E_vRzoom.get()) 
            f.seek(0) 
            json.dump(data, f, indent=4)
            f.truncate() 
        uRzoom=int(E_uRzoom.get())
        vRzoom=int(E_vRzoom.get()) 

    
    f3=tk.Frame(root)
    b_save = tk.Button(root, text ="Sauver",command=sauver).pack(side=tk.LEFT)
    b_quitter = tk.Button(root, text ="Quitter",command=root.destroy).pack(side=tk.LEFT)
    f3.pack(side=tk.BOTTOM)
    

#Config fenetre
fenetre = tk.Tk()
fenetre.title("CODEV - Imageur 3D")
largeur=320
hauteur=240
fenetre.geometry(str(largeur)+"x"+str(hauteur))
fenetre.config(bg = "#87CEEB") 

haut=tk.Frame(fenetre)
Ne=tk.StringVar(value=N)
tk.Label(haut, text="N=").pack(side=tk.LEFT)
tk.Entry(haut,textvariable=Ne).pack(side=tk.LEFT)
haut.pack(side=tk.TOP)
#Cadre bouttons
cadre1 = tk.Frame(fenetre)
cadre1.pack()
cadre1.place(anchor="c", relx=.5, rely=.5)
 

def projeter():
    N=int(Ne.get())
    filepath="img_proj/Trame"
    tb.main(N,filepath)
    
    i=0
    def camera():
        cp.camera("IRZoom"+str(i)+".jpg")
            
    def projection():
        cp.projection(fenetre,1,"Trame"+str(i+1)+".bmp")
        
    while i<N:
        threading.Thread(target=projection).start()
        threading.Thread(target=camera).start()
        i=i+1
        time.sleep(2)
    

def calculer():
    fringe_detector("IRZoom",N,uRzoom,vRzoom)
    coord3D_objet(N)
    messagebox.showinfo("Info", "Les calculs ont été effectués !")
    

def afficher():
    affichage()

def comparer():
    pass


#Barre de menu
menubar = tk.Menu(fenetre)

menu1 = tk.Menu(menubar, tearoff=0)
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Menu", menu=menu1)
menu1 = tk.Menu(menubar, tearoff=0)
menu1.add_command(label="Modifier", command=parametres)
menubar.add_cascade(label="Paramètres", menu=menu1)

fenetre.config(menu=menubar)


#Boutons

b1 = tk.Button(cadre1, width=40, height=3, text ="Projection",command=projeter)
b2 = tk.Button(cadre1, width=40, height=3, text ="Lancer calculs",command=calculer)
b3 = tk.Button(cadre1, width=40, height=3, text ="Afficher",command=afficher)
b1.pack()
b2.pack()
b3.pack()


fenetre.mainloop()
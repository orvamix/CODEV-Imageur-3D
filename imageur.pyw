import tkinter as tk
from tkinter import messagebox
from coord3D_objet import *
from fringe_detector import *
from calibration import *

import json
f = open('info.json')
info = json.load(f)
N=5
uRzoom=info['uRzoom']
vRzoom=info['vRzoom']

#Config fenetre
fenetre = tk.Tk()
fenetre.title("CODEV - Imageur 3D")
largeur=320
hauteur=240
fenetre.geometry(str(largeur)+"x"+str(hauteur))
fenetre.config(bg = "#87CEEB") 

#Cadre bouttons
cadre1 = tk.Frame(fenetre)
cadre1.pack()
cadre1.place(anchor="c", relx=.5, rely=.5)

#Variable globales
statut_calibrer=False
statut_calculer=False

def calibrer():
    global statut_calibrer
    if calibration()==True:
        statut_calibrer=True
        messagebox.showinfo("Info", "Calibration effectuée avec succès")
    else:
        messagebox.showinfo("Erreur", "Problème de calibration")

def calculer():
    global statut_calibrer
    if statut_calibrer==False:
        messagebox.showinfo("Attention", "La calibration n'a pas été effectuée !")
        return
    fringe_detector("IRZoom",N,1200,1300)
    coord3D_objet()
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

menu2 = tk.Menu(menubar, tearoff=0)
menu2.add_command(label="Calibrer", command=calibrer)
menubar.add_cascade(label="Calibration", menu=menu2)

menu3 = tk.Menu(menubar, tearoff=0)
menu3.add_command(label="Afficher", command=afficher)
menu3.add_command(label="Comparer", command=comparer)
menubar.add_cascade(label="Résultats", menu=menu3)

fenetre.config(menu=menubar)


#Boutons

b1 = tk.Button(cadre1, width=40, height=3, text ="Calibration",command=calibrer)

b2 = tk.Button(cadre1, width=40, height=3, text ="Lancer calculs",command=calculer)
b3 = tk.Button(cadre1, width=40, height=3, text ="Afficher",command=afficher)
b1.pack()
b2.pack()
b3.pack()


fenetre.mainloop()
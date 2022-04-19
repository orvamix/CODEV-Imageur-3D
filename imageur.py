import tkinter as tk
from tkinter import messagebox
fenetre = tk.Tk()
fenetre.title("CODEV - Imageur 3D")
fenetre.geometry("320x240")

is_calibrated=False

def calibration():
    global is_calibrated
    is_calibrated=True

def calcul():
    global is_calibrated
    if is_calibrated==False:
        messagebox.showinfo("Attention", "La calibration n'a pas été effectuée !")
        return

#Barre de menu
menubar = tk.Menu(fenetre)

menu1 = tk.Menu(menubar, tearoff=0)
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Menu", menu=menu1)

menu2 = tk.Menu(menubar, tearoff=0)
menu2.add_command(label="Calibrer", command=calibration)
menubar.add_cascade(label="Calibration", menu=menu2)

fenetre.config(menu=menubar)

#Boutons

b1 = tk.Button(fenetre, text ="Calibration",command=calibration).pack()
b2 = tk.Button(fenetre, text ="Lancer calculs",command=calcul).pack()



fenetre.mainloop()
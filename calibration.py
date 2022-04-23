import tkinter as tk

def cal_fenetre():
    fenetre = tk.Tk()
    fenetre.title("Calibration")
    
    
    fen_point=[]
    for ligne in range(6):
        fen_point.append(tk.LabelFrame(fenetre, text="Point "+str(ligne+1), padx=20, pady=20))
       
        fen_point[ligne].pack(fill="both", expand="yes")
        tk.Label(fen_point[ligne], text="A l'intérieure de la frame").pack()
        # p=tk.PanedWindow(fen_point[ligne], orient=tk.HORIZONTAL)
        # p.pack(side=tk.TOP, expand=tk.Y, fill=tk.BOTH, pady=2, padx=2)
        # p.add(tk.Frame(p, borderwidth=2, relief=tk.GROOVE))
        # p.add(tk.Label(p, text='Volet 2', background='white', anchor=tk.CENTER) )
        # p.add(tk.Label(p, text='Volet 3', background='red', anchor=tk.CENTER) )
        # p.pack()
    
    
    print(fen_point)
    fenetre.mainloop()


def calibration():
    cal_fenetre()
    





if __name__ == "__main__":
    calibration()
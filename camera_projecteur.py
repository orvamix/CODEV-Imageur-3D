from tkinter import Tk, Button, Canvas, PhotoImage,Toplevel
from PIL import Image, ImageTk
import cv2 as cv
import time
import asyncio

async def projection():
    
    nom_image="img_proj/Mire_damier.bmp"
    fenetre = Toplevel()
     
    # sert a ne pas avoir la bande noir en haut et en bas de la page en fullscreen
    fenetre.attributes('-fullscreen', True)
     
    w, h = fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()
     
    image = Image.open(nom_image) # imageTest fait 270 x 200
     
    image = image.resize((w, h))
     
    # print(image) # <PIL.Image.Image image mode=RGBA size=1920x1080 at 0x43D5AB0>
     
    photo = ImageTk.PhotoImage(image)
     
    # pour que le canvas n'ai pas de bourdure qui reste autour
    can = Canvas(fenetre, highlightthickness=0)
     
    can.create_image(0, 0, anchor='nw', image=photo)
     
    can.pack(fill='both', expand=1)
     

    def fun(event):
        if(event.keysym=='Escape'):
            fenetre.destroy()
            return
        print(event.keysym, event.keysym=='a')
        print(event)

    fenetre.bind("<KeyRelease>", fun)
    
    fenetre.after(3000, fenetre.destroy)
    fenetre.mainloop()

def camera(nom_cam):
    # initialize the camera
    cam = cv.VideoCapture(0)   # 0 -> index of camera
    s, img = cam.read()
    if s:    # frame captured without any errors

        cv.imwrite("img_cam/"+nom_cam,img) #save image
    cam.release
    return
   
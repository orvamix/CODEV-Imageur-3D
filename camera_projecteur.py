from tkinter import Tk, Button, Canvas, PhotoImage,Toplevel
from PIL import Image, ImageTk
import cv2 as cv
import time
import asyncio
import pygame
import time
import sys
from pygame.locals import *

def projection(master,temps=0,photo="img_proj/Mire_damier.png"):
    
    pygame.init()


    screen = pygame.display.set_mode((0,0), FULLSCREEN,display=0)
    w, h = pygame.display.get_surface().get_size()
    pic = pygame.image.load("img_proj/"+photo) #You need an example picture in the same folder as this file!
    pic=pygame.transform.scale(pic, (w, h))
    screen.blit(pic,(0, 0))
    pygame.display.flip()
    # BOUCLE DE JEU
    if(temps==0):
        clock = pygame.time.Clock()
        while True:
            time = clock.tick(10)	
            
            # GESTION DES EVENEMENTS
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit(0)
                    
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                pygame.quit()

            pygame.display.update()
    else:
        pygame.time.wait(1000*temps)
        pygame.quit()

def camera(nom_cam):
    # initialize the camera
    cam = cv.VideoCapture(0)   # 0 -> index of camera
    s, img = cam.read()
    if s:    # frame captured without any errors

        cv.imwrite("img_cam/"+nom_cam,img) #save image
    cam.release
    return
   
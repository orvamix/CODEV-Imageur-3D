from tkinter import Tk, Button, Canvas, PhotoImage,Toplevel
from PIL import Image, ImageTk
import cv2 as cv
import time
import asyncio
import pygame
import time
from pygame.locals import *

def projection(master):
    
    pygame.init()


    screen = pygame.display.set_mode((0,0), FULLSCREEN,display=0)
    w, h = pygame.display.get_surface().get_size()
    pic = pygame.image.load("img_proj/Mire_damier.png") #You need an example picture in the same folder as this file!
    pic=pygame.transform.scale(pic, (w, h))
    screen.blit(pic,(0, 0))
    pygame.display.flip()

    time.sleep(1)
    pygame.quit()

def camera(nom_cam):
    # initialize the camera
    cam = cv.VideoCapture(0)   # 0 -> index of camera
    s, img = cam.read()
    if s:    # frame captured without any errors

        cv.imwrite("img_cam/"+nom_cam,img) #save image
    cam.release
    return
   
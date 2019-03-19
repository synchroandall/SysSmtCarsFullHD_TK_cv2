import tkinter as tk
from tkinter import *
import cv2
import numpy
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("500x600")
width, height = 800, 600
cap = cv2.VideoCapture(0)

lmain = tk.Label(root)
frame_hsv= tk.Label(root)
lmain.pack()
frame_hsv.place(x=0,y=300)



h_down = Scale(from_=0, to=255, orient=HORIZONTAL)
s_down = Scale(from_=0, to=255, orient=HORIZONTAL)
v_down = Scale(from_=0, to=255, orient=HORIZONTAL)
h_up = Scale(from_=0, to=255, orient=HORIZONTAL)
s_up = Scale(from_=0, to=255, orient=HORIZONTAL)
v_up = Scale(from_=0, to=255, orient=HORIZONTAL)
#Saves=Button(root,text="Save image",width=20)
h_down.place(x=0, y=120)
s_down.place(x=0, y=160)
v_down.place(x=0, y=200)
h_up.place(x=0, y=0)
s_up.place(x=0, y=40)
v_up.place(x=0, y=80)
#Saves.place(x=0, y=240)
Label(text="h_up").place(x=0,y=0)
Label(text="s_up").place(x=0,y=40)
Label(text="v_up").place(x=0,y=80)
Label(text="h_down").place(x=0,y=120)
Label(text="s_down").place(x=0,y=160)
Label(text="v_down").place(x=0,y=200)
#def Save(event):
    #f=open('text.txt','w')
    #f.write(str(h1_down)+'\n')
    #f.write(str(s1_down) + '\n')
    #f.write(str(v1_down) + '\n')
    #f.write(str(h1_up) + '\n')
    #f.write(str(s1_up) + '\n')
    #f.write(str(v1_up) + '\n')
    #f.close()
#Saves.bind("<Button-1>",Save)
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_hsv2 = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)

    cv2image_hsv = cv2.cvtColor(frame_hsv2, cv2.COLOR_BGR2HSV_FULL)

    root.update()
    h1_down=h_down.get()
    s1_down = s_down.get()
    v1_down = v_down.get()
    h1_up = h_up.get()
    s1_up = s_up.get()
    v1_up = v_up.get()

    mask = cv2.inRange(cv2image_hsv, numpy.array([h1_down, s1_down, v1_down]), numpy.array([h1_up, s1_up, v1_up]))
    finish = cv2.bitwise_and(cv2image_hsv, frame_hsv2, mask=mask)
    thresh = cv2.inRange(cv2image_hsv, numpy.array([h1_down, s1_down, v1_down]), numpy.array([h1_up, s1_up, v1_up]))

    img = Image.fromarray(thresh)
    imgtk_hsv = ImageTk.PhotoImage(image=img)
    frame_hsv.imgtk_hsv = imgtk_hsv
    frame_hsv.configure(image=imgtk_hsv)
    #show_frame()
    if cv2.waitKey(1) == 27:
        root.destroy()
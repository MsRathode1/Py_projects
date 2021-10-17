import time
import tkinter
import cv2
import PIL.Image,PIL.ImageTk
from functools import partial
import threading

import imutils as imutils

stream = cv2.VideoCapture("rclip2.mp4")
flag = True
def play(speed):
    global flag
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES ,frame1 + speed)

    grabbed,frame=stream.read()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(120, 25, fill="Red", font="Times 27 bold", text=" Decision pending")
    flag = not flag









def pending(decision):
    frame = cv2.cvtColor(cv2.imread("decision pending.jpg"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame) )
    canvas.image  = frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    time.sleep(2)
    if decision == "OUT":
        frame = cv2.cvtColor(cv2.imread("outt.jpg"), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
        time.sleep(5)
    else:
        frame = cv2.cvtColor(cv2.imread("NOT.jpg"), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
        time.sleep(2)




def not_out():
    thread = threading.Thread(target=pending,args=("NOT OUT",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")

def Out():
    thread = threading.Thread(target=pending,args=("OUT",))
    thread.daemon = 1
    thread.start()
    print("Player is out")

# width and height of main screen
SET_WIDTH = 650
SET_HEIGHT  =600

Window = tkinter.Tk()
Window.title('THIRD UMPIRE! DECISION REVIEW KIT')
cv_img = cv2.cvtColor(cv2.imread('welcome.png.jpg'),cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(Window,width = SET_WIDTH,height = SET_HEIGHT)
photo  = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
Image_on_canvas = canvas.create_image(0,0,ancho = tkinter.NW,image = photo)
canvas.pack()
# buttons are here
btn = tkinter.Button(Window,text ="<<PREVIOUS FAST!!",width = 90,command=partial(play,-25))
btn.pack()

btn = tkinter.Button(Window,text ="<<PREVIOUS SLOW!!",width = 90,command=partial(play,-2))
btn.pack()

btn = tkinter.Button(Window,text ="NEXT (SLOW)>>",width = 90,command=partial(play,2))
btn.pack()

btn = tkinter.Button(Window,text ="NEXT (FAST)>>",width = 90,command=partial(play,25))
btn.pack()


btn = tkinter.Button(Window,text ="NOT OUT",width = 90,command=not_out)
btn.pack()

btn = tkinter.Button(Window,text =" OUT",width = 90,command=Out)
btn.pack()

Window.mainloop()

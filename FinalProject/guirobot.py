#Para poder utilizar esta GUI es necesario tener PILLOW y TKINTER, salu3
import tkinter as tk
from PIL import ImageTk, Image

def manualmode():
    if (manualonoff.get()==1):
        print('Manual mode off')
    elif (manualonoff.get()==2):
        print('Manual mode on')

def automode():
    if (autoonoff.get()==1):
        print('Automode off')
    elif (autoonoff.get()==2):
        print('Automode on')
    
def forward():
    print('Going Forward')

def backward():
    print('Going Backward')

def left():
    print('Turning Left')

def right():
    print('Turning Right')

def stop():
    print('Stop')

#Creacion de la ventana
w=tk.Tk()
w.geometry('1000x400')
w.title('Trueno Chocolate')
w.config(bg='#151B54')
manuallb=tk.Label(w, text='Manual mode', bg='#98AFC7', fg='white', font=('Arial', 20), width=30).place(x=10, y=10)
autolb=tk.Label(w, text='Automode', bg='#98AFC7', fg='white', font=('Arial', 20), width=30).place(x=510, y=10)

#Modo manual
manualonoff=tk.IntVar()
offmanualbutton=tk.Radiobutton(w, text='Off', bg='#ffff1a', relief=tk.GROOVE, command=manualmode, variable=manualonoff, value=1, font=('Arial',10)).place(x=418, y=50)
onmanualbutton=tk.Radiobutton(w, text='On', bg='white', relief=tk.GROOVE, command=manualmode, variable=manualonoff, value=2, font=('Arial', 10)).place(x=370, y=50)

stopimage=Image.open('stop.png')
stopimage=stopimage.resize((60,60))
stopimg=ImageTk.PhotoImage(stopimage)
stopbutton=tk.Button(w, image=stopimg, bg='white', relief=tk.RAISED, command=stop).place(x=200, y=190) #'#F70D1A'

forwardimage=Image.open('forwardarrow')
forwardimage=forwardimage.resize((60,60))
forwardimg=ImageTk.PhotoImage(forwardimage)
forwardbutton=tk.Button(w, image=forwardimg, bg='white', relief=tk.RAISED, command=forward).place(x=200, y=80)

backwardimage=Image.open('backwardarrow')
backwardimage=backwardimage.resize((60,60))
backwardimg=ImageTk.PhotoImage(backwardimage)
backwardbutton=tk.Button(w, image=backwardimg, bg='white', relief=tk.RAISED, command=backward).place(x=200, y=300)

rightimage=Image.open('rightarrow.png')
rightimage=rightimage.resize((60,60))
rightimg=ImageTk.PhotoImage(rightimage)
rightbutton=tk.Button(w, image=rightimg, bg='white', relief=tk.RAISED, command=right).place(x=310, y=190)

leftimage=Image.open('leftarrow')
leftimage=leftimage.resize((60,60))
leftimg=ImageTk.PhotoImage(leftimage)
leftbutton=tk.Button(w, image=leftimg, bg='white', relief=tk.RAISED, command=left).place(x=90, y=190)

#Modo automatico
autoonoff=tk.IntVar()
offautobutton=tk.Radiobutton(w, text='Off', bg='#ffff1a', relief=tk.GROOVE, command=automode, variable=autoonoff, value=1, font=('Arial', 25)).place(x=800, y=70)
onautobutton=tk.Radiobutton(w, text='On', bg='white', relief=tk.GROOVE, command=automode, variable=autoonoff, value=2, font=('Arial', 25)).place(x=650, y=70)

distrecorlb=tk.Label(w, text='Distance traveled (cm)= 00', bg='#2B3856', fg='white', font=('Arial',22)).place(x=550, y=170)
distobjlb=tk.Label(w, text='Distancie to object (cm)= 00', bg='#2B3856', fg='white', font=('Arial',22)).place(x=550, y=250)

#Cambiar el color de cada boton cuando este funcionando

w.mainloop()
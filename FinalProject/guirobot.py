#Para poder utilizar esta GUI es necesario tener PILLOW y TKINTER, salu3
import tkinter as tk
from PIL import ImageTk, Image

#Creacion de la ventana
w=tk.Tk()
w.geometry('1000x400')
w.title('Trueno Chocolate')
w.config(bg='#151B54')
manuallb=tk.Label(w, text='Modo manual', bg='#98AFC7', fg='white', font=('Arial', 20), width=30).place(x=10, y=10)
#manuallb=tk.Label(w, text='Modo manual', bg='#2B3856', fg='white', font=('Arial', 20), width=30).place(x=10, y=10)
#autolb=tk.Label(w, text='Modo automatico', bg='#2B3856', fg='white', font=('Arial', 20), width=30).place(x=510, y=10)
autolb=tk.Label(w, text='Modo automatico', bg='#98AFC7', fg='white', font=('Arial', 20), width=30).place(x=510, y=10)

#Modo manual
offmanualbutton=tk.Button(w, text='Off', bg='#ffff1a', relief=tk.GROOVE, command=None, font=('Arial',10)).place(x=418, y=50)
onmanualbutton=tk.Button(w, text='On', bg='white', relief=tk.GROOVE, command=None, font=('Arial', 10)).place(x=370, y=50)

stopimage=Image.open('stop.png')
stopimage=stopimage.resize((60,60), Image.LANCZOS)
stopimg=ImageTk.PhotoImage(stopimage)
stopbutton=tk.Button(w, image=stopimg, bg='white', relief=tk.RAISED, command=None).place(x=200, y=190) #'#F70D1A'

forwardimage=Image.open('forwardarrow')
forwardimage=forwardimage.resize((60,60), Image.LANCZOS)
forwardimg=ImageTk.PhotoImage(forwardimage)
forwardbutton=tk.Button(w, image=forwardimg, bg='white', relief=tk.RAISED, command=None).place(x=200, y=80)

backwardimage=Image.open('backwardarrow')
backwardimage=backwardimage.resize((60,60), Image.LANCZOS)
backwardimg=ImageTk.PhotoImage(backwardimage)
backwardbutton=tk.Button(w, image=backwardimg, bg='white', relief=tk.RAISED, command=None).place(x=200, y=300)

rightimage=Image.open('rightarrow.png')
rightimage=rightimage.resize((60,60), Image.LANCZOS)
rightimg=ImageTk.PhotoImage(rightimage)
rightbutton=tk.Button(w, image=rightimg, bg='white', relief=tk.RAISED, command=None).place(x=310, y=190)

leftimage=Image.open('leftarrow')
leftimage=leftimage.resize((60,60), Image. LANCZOS)
leftimg=ImageTk.PhotoImage(leftimage)
leftbutton=tk.Button(w, image=leftimg, bg='white', relief=tk.RAISED, command=None).place(x=90, y=190)

#Modo automatico
offautobutton=tk.Button(w, text='Off', bg='#ffff1a', relief=tk.GROOVE, command=None, font=('Arial', 25)).place(x=800, y=70)
onautobutton=tk.Button(w, text='On', bg='white', relief=tk.GROOVE, command=None, font=('Arial', 25)).place(x=650, y=70)

distrecorlb=tk.Label(w, text='Distancia recorrida (cm)= 00', bg='#2B3856', fg='white', font=('Arial',22)).place(x=550, y=170)
distobjlb=tk.Label(w, text='Distancia con objeto (cm)= 00', bg='#2B3856', fg='white', font=('Arial',22)).place(x=550, y=250)

#Cambiar el color de cada boton cuando este funcionando

w.mainloop()
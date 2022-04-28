import tkinter as tk
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

def funled():
    print('LED On')
    time.sleep(5)
    GPIO.output(7,1)
    print('LED Off')
    tim.sleep(5)
    GPIO.output(7,0)
    
w=tk.Tk() #Crea la ventana
w.title('Primer GUI') #Titulo
w.geometry('200x200') #Tamaño
w.config(bg='black') #Color de fondo
l1=tk.Label(w,text="Comunicacion GUI-RaspberryPi",bg='white',fg='red').pack() #Pack() permite ponerlo en el medio
b1=tk.Button(w,text='LED',command=funled).pack() #Pack() lo colocará centrado debajo de Label
b2=tk.Button(w,text='Salir',command=w.destroy).pack() #destroy hace que se cierre la ventana 
w.mainloop()
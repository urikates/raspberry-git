import RPi.GPIO as GPIO
import tkinter as tk

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

#RGB Function
def ledrgb():
    valor=var.get()
    if valor==1:
        print('Red On')
        GPIO.output(11,True)
        GPIO.output(13,False)
        GPIO.output(15,False)
    elif valor==2:
        print('Green On')
        GPIO.output(11,False)
        GPIO.output(13,True)
        GPIO.output(15,False)
    elif valor==3:
        print('Blue On')
        GPIO.output(11,False)
        GPIO.output(13,False)
        GPIO.output(15,True)
    elif valor==4:
        print('Off')
        GPIO.output(11,False)
        GPIO.output(13,False)
        GPIO.output(15,False)



#GUI
w=tk.Tk()
w.title('LED RGB')
w.geometry('400x300')
w.config(bg='salmon')
var=tk.IntVar()
rb1=tk.Radiobutton(w, text='Red', bg='red', variable=var, value=1, command=ledrgb, width=30, font=('arial,20')).place(x=0, y=0)
rb2=tk.Radiobutton(w, text='Green', bg='green', variable=var, value=2, command=ledrgb, width=30, font=('arial,20')).place(x=0, y=50)
rb3=tk.Radiobutton(w, text='Blue', variable=var, value=3, command=ledrgb, width=30, font=('arial,20')).place(x=0, y=100)
rb4=tk.Radiobutton(w, text='Off', variable=var, value=4, command=ledrgb, width=30, font=('arial,20')).place(x=0, y=150)
w.mainloop()
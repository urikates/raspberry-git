import RPi.GPIO as GPIO
import tkinter as tk

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT) #SENTIDO
GPIO.setup(13,GPIO.OUT) #SENTIDO
GPIO.setup(15,GPIO.OUT) #PWM

pwmmotor=GPIO.PWM(15,100) #PWM KHz

def fun(valor):
    sentido=svar.get()
    if sentido=='izquierda':
        print('<-----')
    elif sentido=='derecha':
        print('----->')
    else:
        print('Error')
    print(ivar.get())
    pwmmotor.ChangeDutyCycle(ivar.get())
    
def funr():
    valor=rvar.get()
    if valor==1:
        GPIO.output(11,True)
        GPIO.output(13,False)
        GPIO.output(15, True)
        #pwmmotor.ChangeDutyCycle(100)
        print('<-----')
    elif valor==2:
        print('----->')
        GPIO.output(11,False)
        GPIO.output(13,True)
        GPIO.output(15, True)
    elif valor==3:
        GPIO.output(15,False)

#GUI
w=tk.Tk()
w.title('Control de motor DC')
w.config(bg='red')
w.geometry('400x400')
svar=tk.StringVar()
e1=tk.Entry(w,textvariable=svar).place(x=0,y=0)
ivar=tk.IntVar()
sc1=tk.Scale(w,from_=0, to=100, resolution=2, variable=ivar, command=funr, orient=tk.HORIZONTAL).place(x=0, y=50)
rvar=tk.IntVar()
rb1=tk.Radiobutton(w, text='Izquierda', variable=rvar, value=1, command=funr).place(x=0, y=100)
rb2=tk.Radiobutton(w, text='Derecha', variable=rvar, value=2, command=funr).place(x=0, y=150)
rb2=tk.Radiobutton(w, text='Paro', variable=rvar, value=3, command=funr).place(x=0, y=200)

w.mainloop()



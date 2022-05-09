import RPi.GPIO as GPIO
import tkinter as tk

#PINES
led=(3,5,7)
motor=(8,10,12)
servo=11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(motor,GPIO.OUT)
GPIO.setup(servo,GPIO.OUT)

#PWMS
pwmmotor=GPIO.PWM(12,1000)
pwmservo=GPIO.PWM(11,1000)

#RGB Function
def ledrgb():
    valor=ledcolor.get()
    if valor==1:
        print('Red On')
        GPIO.output(3,False)
        GPIO.output(5,True)
        GPIO.output(7,True)
    elif valor==2:
        print('Green On')
        GPIO.output(3,True)
        GPIO.output(5,False)
        GPIO.output(7,True)
    elif valor==3:
        print('Blue On')
        GPIO.output(3,True)
        GPIO.output(5,True)
        GPIO.output(7,False)
    elif valor==4:
        print('Off')
        GPIO.output(3,True)
        GPIO.output(5,True)
        GPIO.output(7,True)

#MotorDC Function
def motordc():
    val=sentido.get()
    if val==1:
        GPIO.output(8,True)
        GPIO.output(10,False)
        print('<-----')
    else:
        print('----->')
        GPIO.output(8,False)
        GPIO.output(10,True)

#MAIN WINDOW        
w=tk.Tk()
w.title('Trueno Chocolate')
w.geometry('1000x600')
w.config(bg='purple')
titulo=tk.Label(w, text='Control de LED RGB, Motor DC, Servomotor', bg='yellow', font=('Arial',20)).place(x=200,y=0)
 
#LEDRGB
lrgb=tk.Label(w, text='LED RGB', bg='orange', font=('Arial',20)).place(x=50, y=50)
ledcolor=tk.IntVar()
rojo=tk.Radiobutton(w, text='Red', bg='red', variable=ledcolor, value=1, command=ledrgb, width=20, font=('arial',15)).place(x=10, y=150)
verde=tk.Radiobutton(w, text='Green', bg='green', variable=ledcolor, value=2, command=ledrgb, width=20, font=('arial',15)).place(x=10, y=250)
azul=tk.Radiobutton(w, text='Blue', bg='blue', variable=ledcolor, value=3, command=ledrgb, width=20, font=('arial',15)).place(x=10, y=350)
ledapagado=tk.Radiobutton(w, text='Off', bg='black', fg='white', variable=ledcolor, value=4, command=ledrgb, width=20, font=('arial',15)).place(x=10, y=450)

#MOTORDC
lmotor=tk.Label(w, text='Motor DC', bg='snow', font=('Arial',20)).place(x=430, y=50)
sentido=tk.IntVar()
izquierda=tk.Radiobutton(w, text='Izquierda', bg='pink', variable=sentido, value=1, command=motordc, width=20, font=('Arial',15)).place(x=350, y=200)
derecha=tk.Radiobutton(w, text='Derecha', bg='hot pink', variable=sentido, value=2, command=motordc, width=20, font=('Arial',15)).place(x=350, y=400)

w.mainloop()
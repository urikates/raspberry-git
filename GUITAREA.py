import RPi.GPIO as GPIO
import tkinter as tk

#PINES
led=(3,5,7)
motor=(11,13,15)
servo=19

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(motor,GPIO.OUT)
GPIO.setup(servo,GPIO.OUT)

#PWMS
pwmmotor=GPIO.PWM(15,100)
pwmservo=GPIO.PWM(19,100)
pwmservo.start(0)

#RGB Window
def ledrgbwindow():
    print("ejecutando")
    w2=tk.Toplevel(w)
    w2.geometry('400x200')
    w2.config(bg='white')
    l2=tk.Label(w2, text='LED RGB', bg='white', font=('Arial',20)).pack()
    rb1=tk.Radiobutton(w2, text='Red', bg='red', variable=ledcolor, value=1, command=ledcontrol, width=20, font=('arial',20)).pack()
    rb2=tk.Radiobutton(w2, text='Green', bg='green', variable=ledcolor, value=2, command=ledcontrol, width=20, font=('arial',20)).pack()
    rb3=tk.Radiobutton(w2, text='Blue', bg='blue', variable=ledcolor, value=3, command=ledcontrol, width=20, font=('arial',20)).pack()
    rb4=tk.Radiobutton(w2, text='Off', bg='black', fg='white', variable=ledcolor, value=4, command=ledcontrol, width=20, font=('arial',20)).pack()

#Motor Window
def motorwindow():
    w3=tk.Toplevel(w)
    w3.geometry('400x150')
    w3.config(bg='PeachPuff2')
    l3=tk.Label(w3, text='MOTOR DC', bg='PeachPuff2', font=('Arial',20)).pack()
    rb1=tk.Radiobutton(w3, text='Izquierda', bg='snow', variable=senmotor, value=1, command=motorcontrol, width=10, font=('Arial',15)).place(x=10, y=50)
    rb2=tk.Radiobutton(w3, text='Derecha', bg='snow', variable=senmotor, value=2, command=motorcontrol, width=10, font=('Arial',15)).place(x=200, y=50)
    rb3=tk.Radiobutton(w3, text='Paro', bg='snow', variable=senmotor, value=3, command=motorcontrol, width=10, font=('Arial',15)).place(x=120, y=100)
    
#Servo window
def servowindow():
    w4=tk.Toplevel(w)
    w4.geometry('400x200')
    w4.config(bg='dark salmon')
    l4=tk.Label(w4, text='SERVOMOTOR', bg='dark salmon', font=('Arial',20)).pack()
    l5=tk.Label(w4, text='DEGREES', bg='dark salmon', font=('Arial',12)).place(x=150, y=80)
    entrada=tk.Scale(w4,from_=0, to=180, resolution=10, bg='light coral',variable=servogrados, command=servomotion, orient=tk.HORIZONTAL).place(x=150, y=100)
    
#RGB Function
def ledcontrol():
    color=ledcolor.get()
    if color==1:
        print('Red On')
        GPIO.output(3,False)
        GPIO.output(5,True)
        GPIO.output(7,True)
    elif color==2:
        print('Green On')
        GPIO.output(3,True)
        GPIO.output(5,False)
        GPIO.output(7,True)
    elif color==3:
        print('Blue On')
        GPIO.output(3,True)
        GPIO.output(5,True)
        GPIO.output(7,False)
    elif color==4:
        print('Off')
        GPIO.output(3,True)
        GPIO.output(5,True)
        GPIO.output(7,True)
        

def motorcontrol():
    valor=senmotor.get()
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

#Servo Function
def servomotion(angulo):
    duty=float(angulo)/10.0+2
    pwmservo.ChangeDutyCycle(duty)
    print(str(duty))

#MAIN WINDOW        
w=tk.Tk()
w.title('Trueno Chocolate')
w.geometry('400x100')
w.config(bg='azure')
titulo=tk.Label(w, text='Control de LED RGB, Motor DC, Servomotor', bg='mint cream', font=('Arial,20')).place(x=25,y=0)
ledrgb=tk.Button(w, text='LED RGB', bg='alice blue', relief=tk.GROOVE, command=ledrgbwindow).place(x=10, y=50)
motorbot=tk.Button(w, text='Motor DC', bg='alice blue', relief=tk.GROOVE, command=motorwindow).place(x=150, y=50)
servobot=tk.Button(w, text='Servomotor',bg='alice blue', relief=tk.GROOVE, command=servowindow).place(x=280, y=50)
ledcolor=tk.IntVar()
senmotor=tk.IntVar()
servogrados=tk.IntVar()
w.mainloop()
 


import tkinter as tk
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

def gradosservo():
    duty=100/180+1
    pwmServo.ChangeDutyCycle(duty)
    print(str(duty))

def fun():
    color = data.get()
    
    print(data.get())
    if color == 'trueno':
        #import Servomotor as servo
        print('contraseña: correcta')
        pwmServo.ChangeDutyCycle(100)
        #gradosservo() #FAlta la funciòn para convertir a grados
        #print(str(gradosservo()))
    else:
        print('contraseña: incorrecta')
        pwmServo.ChangeDutyCycle(0)
              
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
pwmServo = GPIO.PWM(8,50)
pwmServo.start(0)

w = tk.Tk()
w.title('Contraseña')
w.geometry('400x200')
w.config(bg='coral1')
l1 = tk.Label(w,text='Introduzca contraseña: ').grid(row=0,column=0)
data = tk.StringVar()
el = tk.Entry(w,textvariable=data).grid(row=0,column=1)
b1 = tk.Button(w,text='Enter',command=fun).grid(row=1,column=0)
w.mainloop()
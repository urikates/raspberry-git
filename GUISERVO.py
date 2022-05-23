import RPi.GPIO as GPIO
import time
import tkinter as tk

GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.OUT)
pwmservo=GPIO.PWM(32,100)
pwmservo.start(0)

def grados(angulo):
    duty=float(angulo)/10.0+2
    pwmservo.ChangeDutyCycle(duty)
    print(str(duty))
    
#GUI
w=tk.Tk()
w.geometry('400x200')
w.title('Control Servomotor')
w.config(bg='blue')
angulo=tk.IntVar()
#entrada=tk.Entry(w,textvariable=valor,command=grados).place(x=0,y=0)
entrada=tk.Scale(w,from_=0, to=180, resolution=10, variable=angulo, command=grados, orient=tk.HORIZONTAL).place(x=0, y=50)

w.mainloop()
#Checar si es correcta la actualizacion de la distancia con un objeto
#Agregar los encoders y la modificacion de la distancia recorrida
#Agregar candados para modo manual y auto



#Para poder utilizar esta GUI es necesario tener PILLOW y TKINTER, salu3
import tkinter as tk
from PIL import ImageTk, Image
import RPi.GPIO as GPIO
import time

#global distancia, distanciai, distanciad, vueltas,
contador=0
encoder=0
smotori=0
vueltas=0

#PINES
servo=32
trig=11
echo=13
motori=(3,5,7)
motord=(8,10,12)
encoders=(40, 18)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.OUT)
GPIO.setup(servo, GPIO.OUT)
GPIO.setup(motori, GPIO.OUT)
GPIO.setup(motord, GPIO.OUT)
GPIO.setup(encoders, GPIO. IN)

#PWMs
pwmservo=GPIO.PWM(servo, 100)
pwmservo.start(14)
pwmmotori=GPIO.PWM(5, 100)
pwmmotord=GPIO.PWM(10, 100)

# def grados(angulo):
#     duty=float(angulo)/10.0+2
#     pwmservo.ChangeDutyCycle(duty)
#     print(str(duty))


def ultrasonico():
    #Funciòn que nos da la distancia con un objeto por medio del sensor ultrasònico
    GPIO.output(trig, 0)
    time.sleep(0.1)
    GPIO.output(trig, 1)
    time.sleep(0.000012)
    GPIO.output(trig, 0)
    
    if GPIO.input(echo)==0:
        start=time.time()
    
    if GPIO.input(echo)==1:
        end=time.time()
    
    tiempo=end-start
    tiemposeg=tiempo*17150
    distancia=round(tiemposeg, 2)
    distobjlb.config(text='Distance to object (cm)= '+str(distancia))
    
def distancia():
    global contador, vueltas
#     distrecorlb.config(text='Distance traveled (cm)= '+str(contador))
    if(smotori==1):
        if (GPIO.input(40)==0):
            contador=contador
        else:
            contador=contador+1.17
            contador=round(contador, 2)
            print(str(contador))
    w.after(1, distancia)
    

def mode():
    if (onoff.get()==1):
        print('Automode on')
        autofun()
    elif (onoff.get()==2):
        print('Manual mode on')
        ultrasonico()
        
def autofun():
    global contador
    if(onoff.get()==1):
        contador=contador+1
        print(str(contador))
#         ultrasonico()
#         if (distancia>30):
#             forwardauto()
#         else:
#             stopauto()
#             pwmservo.ChangeDutyCycle(15.5)
#             ultrasonico()
#             distanciad=distancia
#             pwmservo.ChangeDutyCycle(6.5)
#             ultrasonico()
#             distanciai=distancia
#             if (distanciai>distanciad):
#                 leftauto()
#                 time.sleep(2)
#                 stop()
#             elif (distanciai<distanciad):
#                 rightauto()
#                 time.sleep(2)
#                 stopauto()
    w.after(1000, autofun)
#
            

    
def forwardauto():
        print('Going Forward')
        GPIO.output(3, True)
        GPIO.output(7, False)
        pwmmotori.ChangeDutyCycle(100)
        GPIO.output(8, True)
        GPIO.output(12, False)
        pwmmotord.ChangeDutyCycle(100)
    
def forwardmanual():
    if(onoff.get()==2):
        print('Going Forward')
        GPIO.output(3, True)
        GPIO.output(7, False)
        global smotori
        smotori=1
        pwmmotori.ChangeDutyCycle(100)
        GPIO.output(8, True)
        GPIO.output(12, False)
        pwmmotord.ChangeDutyCycle(100)
        distancia()

def backwardauto():
    print('Going Backward')
    GPIO.output(3, False)
    GPIO.output(7, True)
    pwmmotori.ChangeDutyCycle(50)
    GPIO.output(8, False)
    GPIO.output(12, True)
    pwmmotord.ChangeDutyCycle(50)

def backwardmanual():
    if(onoff.get()==2):
        print('Going Backward')
        GPIO.output(3, False)
        GPIO.output(7, True)
        pwmmotori.ChangeDutyCycle(50)
        GPIO.output(8, False)
        GPIO.output(12, True)
        pwmmotord.ChangeDutyCycle(50)

def leftauto():
    print('Turning Left')
    GPIO.output(3, True)
    GPIO.output(7, False)
    pwmmotori.ChangeDutyCycle(100)
    GPIO.output(8, True)
    GPIO.output(12, False)
    pwmmotord.ChangeDutyCycle(50)

def leftmanual():
    if(onoff.get()==2):
        print('Turning Left')
        GPIO.output(3, True)
        GPIO.output(7, False)
        pwmmotori.ChangeDutyCycle(100)
        GPIO.output(8, False)
        GPIO.output(12, False)
        pwmmotord.ChangeDutyCycle(50) 

def rightauto():
    print('Turning Right')
    GPIO.output(3, True)
    GPIO.output(7, False)
    pwmmotori.ChangeDutyCycle(50)
    GPIO.output(8, True)
    GPIO.output(12, False)
    pwmmotord.ChangeDutyCycle(100)
    
def rightmanual():
        if(onoff.get()==2):
            print('Turning Right')
            GPIO.output(3, False)
            GPIO.output(7, False)
            pwmmotori.ChangeDutyCycle(50)
            GPIO.output(8, True)
            GPIO.output(12, False)
            pwmmotord.ChangeDutyCycle(100) 

def stopauto():
    print('Stop')
    GPIO.output(3, False)
    GPIO.output(7, False)
    pwmmotori.ChangeDutyCycle(0)
    GPIO.output(8, False)
    GPIO.output(12, False)
    pwmmotord.ChangeDutyCycle(0)
    
def stopmanual():
    if(onoff.get()==2):
        print('Stop')
        GPIO.output(3, False)
        GPIO.output(7, False)
        global smotori
        smotori=0
        pwmmotori.ChangeDutyCycle(0)
        GPIO.output(8, False)
        GPIO.output(12, False)
        pwmmotord.ChangeDutyCycle(0) 

#Creacion de la ventana
w=tk.Tk()
w.geometry('1000x400')
w.title('Trueno Chocolate')
w.config(bg='#151B54')
manuallb=tk.Label(w, text='Manual mode', bg='#98AFC7', fg='white', font=('Arial', 20), width=30).place(x=10, y=10)
autolb=tk.Label(w, text='Automode', bg='#98AFC7', fg='white', font=('Arial', 20), width=30).place(x=510, y=10)

#Modo manual
onoff=tk.IntVar()
onmanualbutton=tk.Radiobutton(w, text='On', bg='#ffff1a', relief=tk.GROOVE, command=mode, variable=onoff, value=2, font=('Arial',10)).place(x=418, y=50)

stopimage=Image.open('stop.png')
stopimage=stopimage.resize((60,60))
stopimg=ImageTk.PhotoImage(stopimage)
stopbutton=tk.Button(w, image=stopimg, bg='white', relief=tk.RAISED, command=stopmanual).place(x=200, y=190) #'#F70D1A'

forwardimage=Image.open('forwardarrow')
forwardimage=forwardimage.resize((60,60))
forwardimg=ImageTk.PhotoImage(forwardimage)
forwardbutton=tk.Button(w, image=forwardimg, bg='white', relief=tk.RAISED, command=forwardmanual).place(x=200, y=80)

backwardimage=Image.open('backwardarrow')
backwardimage=backwardimage.resize((60,60))
backwardimg=ImageTk.PhotoImage(backwardimage)
backwardbutton=tk.Button(w, image=backwardimg, bg='white', relief=tk.RAISED, command=backwardmanual).place(x=200, y=300)

rightimage=Image.open('rightarrow.png')
rightimage=rightimage.resize((60,60))
rightimg=ImageTk.PhotoImage(rightimage)
rightbutton=tk.Button(w, image=rightimg, bg='white', relief=tk.RAISED, command=rightmanual).place(x=310, y=190)

leftimage=Image.open('leftarrow')
leftimage=leftimage.resize((60,60))
leftimg=ImageTk.PhotoImage(leftimage)
leftbutton=tk.Button(w, image=leftimg, bg='white', relief=tk.RAISED, command=leftmanual).place(x=90, y=190)

#Modo automatico
onautobutton=tk.Radiobutton(w, text='On', bg='#ffff1a', relief=tk.GROOVE, command=mode, variable=onoff, value=1, font=('Arial', 25)).place(x=800, y=70)

distrecorlb=tk.Label(w, text='Distance traveled (cm)= 00', bg='#2B3856', fg='white', font=('Arial',22)).place(x=550, y=170)
distobjlb=tk.Label(w, text='Distance to object (cm)= 00', bg='#2B3856', fg='white', font=('Arial',22)).place(x=550, y=250)

w.mainloop()
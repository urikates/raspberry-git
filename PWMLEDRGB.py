import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
L=[11,13,15] #Esta lista guarda los valores de los pines
GPIO.setup(L,GPIO.OUT)
#Posible declaración de PWMs mal, por los pines
pwmr=GPIO.PWM(11,1000) #1000 Indica la frecuencia
pwmg=GPIO.PWM(13,1000)
pwmb=GPIO.PWM(15,1000)

while True:
    color=int(input('Color [1-Rojo, 2-Verde, 3-Azul]'))
    if color==1:
        pwmr.ChangeDutyCycle(100)
        pwmg.ChangeDutyCycle(0)
        pwmb.ChangeDutyCycle(0)
    elif color==2:
        pwmr.ChangeDutyCycle(0)
        pwmg.ChangeDutyCycle(100)
        pwmb.ChangeDutyCycle(0)
    else:
        pwmr.ChangeDutyCycle(0)
        pwmg.ChangeDutyCycle(0)
        pwmb.ChangeDutyCycle(100)
GPIO.cleanup() #Limpia todos los GPIO 
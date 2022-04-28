#Se necesitan 3 GPIO, dos para sentido y uno para la velocidad
import RPi.GPIO as GPIO
import time

pines=[11,13,15]

#GPIO.setwarning(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pines,GPIO.OUT)

motorpwm=GPIO.PWM(pines[1],500)

def paro():
    GPIO.output(pines[0],0)
    GPIO.output(pines[2],0)

def izquierda():
    GPIO.output(pines[0],True)
    GPIO.output(pines[2],False)
    
def derecha():
    GPIO.output(pines[0],False)
    GPIO.output(pines[2],True)

def velocidad(valor):
    motorpwm.ChangeDutyCycle(valor)
    

while True:
    duty=int(input('Introduce Velocidad: [0-100]'))
    velocidad(duty)
    sentido=input('Introduce sentido: [D,I]')
    if sentido=='D':
        izquierda()
    else:
        derecha()
GPIO.cleanup()
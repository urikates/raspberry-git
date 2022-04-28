# Incompleto
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

pwmservo=GPIO.PWM(7,50)
pwmservo.start(0)

def gradosservo(grados):
    duty=grados/180+1
    pwmservo.ChangeDutyCycle(duty)

while True:
    angulo=int(input('Introduce un ángulo [0-180]'))
    gradosservo(angulo)
    print('Grados: '+str(angulo))
    #print('Duty: '+str())
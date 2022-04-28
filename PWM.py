import RPi.GPIO as GPIO
import time

def funled(duty):
    if duty>100:
        duty=100
    pwmled.ChangeDutyCycle(duty)
    print('Duty: ' +str(duty))

def incremento():
    for i in range(100):
        pwmled.ChangeDutyCycle(i)
        time.sleep(0.2)
        print('Duty: '+str(i))
        
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.OUT)
pwmled=GPIO.PWM(5,500) #frecuencia dada en Hz, el 100 marca la frecuencia
pwmled.start(100)

while True:
    #valor=int(input('Introduce un valor (0-100): '))
    #funled(valor)
    incremento()
    
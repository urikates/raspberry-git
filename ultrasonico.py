import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
trig=11
echo=13
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

def distancia():
    GPIO.output(trig, 0)
    time.sleep(0.1)
    GPIO.output(trig, 1)
    time.sleep(0.000012)
    GPIO.output(trig, 0)
    
    while GPIO.input(echo)==0:
        start=time.time()
    
    while GPIO.input(echo)==1:
        end=time.time()
    
    tiempo=end-start
    tiemposeg=tiempo*17150
    medida1=round(tiemposeg, 2)
    
    if medida1>2 and medida1<400:
        print(medida1)
    else:
        print('Fuera de rango')

while True:
    distancia()
    
print('Limpiando...')
GPIO.cleanup()
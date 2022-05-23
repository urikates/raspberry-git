import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
trig=11
echo=13
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
end=0
start=0

def distancia():
    GPIO.output(trig, 0)
    time.sleep(0.1)
    GPIO.output(trig, 1)
    time.sleep(0.000012)
    GPIO.output(trig, 0)
    global end
    global start
    while GPIO.input(echo)==0:
        start=time.time()
    
    while GPIO.input(echo)==1:
        end=time.time()
    
    tiempo=end-start
    print(str(tiempo))
    tiemposeg=tiempo*17150
    print(str(tiemposeg))
    medida1=round(tiemposeg, 2)
    
    
    if medida1>2 and medida1<400:
        print(medida1)
    else:
        print('Fuera de rango')

while True:
    distancia()
    
print('Limpiando...')
GPIO.cleanup()
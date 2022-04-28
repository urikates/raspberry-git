import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

while True:
    valor=GPIO.input(11)
    if valor==1:
        print("Boton on")
        GPIO.output(7,1)
        time.sleep(1)
    else:
        print('Boton off')
        GPIO.output(7,0)
        time.sleep(1)
    print('Leer Boton')
GPIO.cleanup() #LIMPIA TODOS LOS PINES



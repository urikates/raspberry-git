import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

def blink(pin,valor):
    GPIO.output(pin,valor)
    time.sleep(1)

while True:
    blink(7,1)
    print("LED On")
    blink(7,0)
    print("LED Off")
GPIO.cleanup(7)
print("Salida de la RPi")

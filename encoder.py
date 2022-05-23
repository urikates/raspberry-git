import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

contador=0
while (contador<1000):
    valor=GPIO.input(40)
    if (valor==1) :
        contador= contador+1
        print(str(contador))
        #time.sleep(0.1)
    else:
        print('Detenido')
    


# while True:
#     valor=GPIO.input(40)
#     if valor==1:
#         print("Boton on")
#         time.sleep(1)
#     else:
#         print('Boton off')
#         time.sleep(1)
GPIO.cleanup() #LIMPIA TODOS LOS PINES
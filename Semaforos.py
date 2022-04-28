import RPi.GPIO as GPIO
import time

sem1=[3,5,7]
sem2=[8,10,12] #semaforo1= 3 5 7 y semaforo2 8 10 12
res=16
sens=18
      
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sem1,GPIO.OUT)
GPIO.setup(sem2,GPIO.OUT)
GPIO.setup(res,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sens,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

state_reg='suno'
state_next='suno'

while True:
    sensor=GPIO.input(sens)
    reset=GPIO.input(res)
    
    if reset==1:
        GPIO.output(sem1,0)
        GPIO.output(sem2,0)
        state_next='suno'
    
    if state_reg=='suno':
        GPIO.output(3,1)
        GPIO.output(12,1)
        if sensor==1:
            state_next='sdos'
        else:
            state_next='suno'
    
    if state_reg=='sdos':
        GPIO.output(3,0)
        GPIO.output(5,1)
        GPIO.output(12,1)
        time.sleep(2)
        state_next='stres'
    
    if state_reg=='stres':
        GPIO.output(5,0)
        GPIO.output(12,0)
        GPIO.output(7,1)
        GPIO.output(8,1)
        time.sleep(10)
        state_next='scuatro'
             
    if state_reg=='scuatro':
        GPIO.output(8,0)
        GPIO.output(7,1)
        GPIO.output(10,1)
        time.sleep(2)
        state_next='scinco'
    
    if state_reg=='scinco':
        GPIO.output(7,0)
        GPIO.output(10,0)
        GPIO.output(3,1)
        GPIO.output(12,1)
        time.sleep(8)
        state_next='suno'

    
    state_reg=state_next
    print("Sensor: "+str(sensor))
    print("Reset: "+str(reset))
    print("Estado actual: "+state_reg)
    print("Siguente estado: "+state_next)
    time.sleep(0.1)
GPIO.cleanup()
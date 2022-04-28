import RPi.GPIO as GPIO
import time

push=[16,18]
GPIO.setmode(GPIO.BOARD)
GPIO.setup(push,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

state_reg='S0'
state_next='S0'
contador=0

while True:
    a=GPIO.input(16)
    b=GPIO.input(18)
    
    if state_reg=='S0':
        if a==1:
            state_next='S1'
        else:
            if b==1:
                state_next='S4'
                
    if state_reg=='S1':
        if a==1:
            if b==1:
                state_next='S2'
        else:
            state_next='S0'
    
    if state_reg=='S2':
        if a==1:
            if b==0:
                state_next='S1'
        else:
            if b==1:
                 state_next='S3'
    
    if state_reg=='S3':
        if a==0:
            if b==0:
                state_next='S0'
                contador=contador+1
        else:
            if b==1:
                state_next='S2'
    
    if state_reg=='S4':
        if b==1:
            if a==1:
                state_next='S5'
        else:
            if a==0:
                state_next='S0'
    
    if state_reg=='S5':
        if b==0:
            if a==1:
                state_next='S6'
        else:
            if a==0:
                state_next='S4'
     
    if state_reg=='S6':
        if a==1:
            if b==1:
                state_next='S5'
        else:
            if b==0:
                state_next='S0'
                contador=contador-1
                
    state_reg=state_next
    print("Estado Actual: "+state_reg)
    print("Estado Siguiente: "+state_next)
    print("Valor de a: "+str(a))
    print("Valor de b: "+str(b))
    print("Contador: "+str(contador))
    time.sleep(0.1)
GPIO.cleanup()
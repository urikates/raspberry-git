    contador=0
    while True:
        if (GPIO.input(16)==1):
            contador=contador+1
            print(str(contador))
            if(contador==16):
                vueltas=vueltas+1
                print(str(contador))
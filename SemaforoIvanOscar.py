SEMAFORO:
v=[0,0] #pines de la raspberry
a=[0,0] 
r=[0,0]
sensor = 0 #botón
contador = 0 #temp
state_reg = 's1' #estado actual
state_next = 's1' #estado siguiente
while True:
    if state_reg == 's1':
        v[1],r[2] = 1
    if sensor == 1:
        state_next = 's2'
    else:
        state_next = 's1'
    
    if state_reg == 's2':
        v[1] = 0
        a[1],r[2] = 1 #contador para 2 segundos condicion contador
        state_next = 's3'
    if state_reg == 's3':
        r[1],v[2] = 1
        a[1],r[2] = 0
    #se introduce un contador 
        if contador != 10:
            state_next = 's3'
        else:
            state_next = 's4'
    if state_reg == 's4':
        v[2] = 0
        r[1],a[2] = 1 #contador para 2 segundos 
        state_next = 's5'
    if state_reg == 's5': #no toma en cuenta el botón
        a[2],r[1] = 0
        v[1],r[2] = 1
    state_reg = state_next
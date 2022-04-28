y0=0
y1=0
state_reg='S0'
state_next='S0'
a=0
b=0
while True:
    if state_reg=='S0':
        y1=1
        if a==1:
            if b==1:
                state_next='S2'
            else:
                state_next='S1'
        else:
            state_next='S0'
    if state_reg=='S1':
        if a==1:
            state_next='S0'
        else:
            state_next='S1'
        y1=1
    if state_reg=='S2':
        state_next='S0'
    state_reg=state_next
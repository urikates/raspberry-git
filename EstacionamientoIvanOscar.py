s=[0,0]

state_reg = 's1' #estado actual
state_next = 's1' #estado siguiente

while True:
    if state_reg == 's1':
        if s[1] == 1 & s[2] == 0:
            state_next='s2'
        else:
            state_next ='s1'
    if state_reg == 's2':
        if s[1] == 0:
            state_next = 's1'
        if s[1] == 1 & s[2] == 1:
            state_next='s3'
        else: state_next = 's2'
    if state_reg == 's3':
        if s[2] == 0:
            state_next = 's2'
        if s[1] == 0 & s[2] == 1:
            state_next = 's4'
        else: state_next = 's3'
    if state_reg == 's4': #se agrega el servo
        if s[2] == 1:
            state_next = 's3'
        if s[1] == 0 & s[2] == 0:
            state_next = 's1'
        else: state_next = 's4'
        state_reg = state_next
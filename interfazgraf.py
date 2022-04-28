import tkinter as tk
import RPi.GPIO as GPIO

def funled1():
    print('Led on')
    GPIO.output(7,True)
def funled2():
    print('Led off')
    GPIO.output(7,False)
    
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
w = tk.Tk()
w.title('LED')
w.geometry('400x200')
w.config(bg='black')
l1 = tk.Label(w,text='Led: ',bg='black',fg='white').pack()
b1 = tk.Button(w,text='on',bg='orange',command=funled1).pack()
b1 = tk.Button(w,text='off',bg='purple',command=funled2).pack()
w.mainloop()
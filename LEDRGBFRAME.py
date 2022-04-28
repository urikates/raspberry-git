import tkinter as tk
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

def fun():
    color = data.get()
    print(data.get())
    if data == 'red':
        GPIO.output(11,True)
        GPIO.output(13,False)
        GPIO.output(15,False)
    elif data == 'blue':
        GPIO.output(13,True)
        GPIO.output(11,False)
        GPIO.output(15,False)
    elif data == 'green':
        GPIO.output(15,True)
        GPIO.output(11,False)
        GPIO.output(13,False)
    else:
        print('Introduce otro color')
    
    
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

w = tk.Tk()
w.title('LED RGB')
w.geometry('400x200')
w.config(bg='darkorange')
l1 = tk.Label(w,text='Introduce color: ').grid(row=0,column=0)
data = tk.StringVar()
el = tk.Entry(w,textvariable=data).grid(row=0,column=1)
b1 = tk.Button(w,text='Ingresar',command=fun).grid(row=1,column=0)
w.mainloop()

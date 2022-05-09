import RPi.GPIO as GPIO
import tkinter as tk

#PINES
led=(3,5,7)
motor=(8,10,12)
servo=11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(motor,GPIO.OUT)
GPIO.setup(servo,GPIO.OUT)

#PWMS
pwmmotor=GPIO.PWM(12,1000)
pwmservo=GPIO.PWM(11,1000)

#RGB Function
def ledrgbwindow():
    print("ejecutando")
    w2=tk.Toplevel(w)
    w2.geometry('400x400')
    l2=tk.Label(w2, text='LED RGB', font=('Arial',20)).place(x=120, y=0)
    rb1=tk.Radiobutton(w2, text='Red', bg='red', variable=ledcolor, value=1, command=ledrgb, width=40, font=('arial,20')).place(x=0, y=50)
    rb2=tk.Radiobutton(w2, text='Green', bg='green', variable=ledcolor, value=2, command=ledrgb, width=40, font=('arial,20')).place(x=0, y=100)
    rb3=tk.Radiobutton(w2, text='Blue', bg='blue', variable=ledcolor, value=3, command=ledrgb, width=40, font=('arial,20')).place(x=0, y=150)
    rb4=tk.Radiobutton(w2, text='Off', bg='black', fg='white', variable=ledcolor, value=4, command=ledrgb, width=40, font=('arial,20')).place(x=0, y=200)
    
def rgbwindow():
    print("ejecutando")
    w2=tk.Toplevel(w)
    w2.geometry('400x400')
    l2=tk.Label(w2, text='SERVO', font=('Arial',20)).place(x=120, y=0)
    rb1=tk.Radiobutton(w2, text='Red', bg='red', variable=ledcolor, value=1, command=turnrgb, width=40, font=('arial,20')).place(x=0, y=50)
    rb2=tk.Radiobutton(w2, text='Green', bg='green', variable=ledcolor, value=2, command=turnrgb, width=40, font=('arial,20')).place(x=0, y=100)
    rb3=tk.Radiobutton(w2, text='Blue', bg='blue', variable=ledcolor, value=3, command=turnrgb, width=40, font=('arial,20')).place(x=0, y=150)
    rb4=tk.Radiobutton(w2, text='Off', bg='black', fg='white', variable=ledcolor, value=4, command=turnrgb, width=40, font=('arial,20')).place(x=0, y=200)
def turnrgb():
    valor=ledcolor.get()
    if valor==1:
        print('Red On')
        GPIO.output(3,False)
        GPIO.output(5,True)
        GPIO.output(7,True)
    elif valor==2:
        print('Green On')
        GPIO.output(3,True)
        GPIO.output(5,False)
        GPIO.output(7,True)
    elif valor==3:
        print('Blue On')
        GPIO.output(3,True)
        GPIO.output(5,True)
        GPIO.output(7,False)
    elif valor==4:
        print('Off')
        GPIO.output(3,True)
        GPIO.output(5,True)
        GPIO.output(7,True)
        

        

#MAIN WINDOW        
w=tk.Tk()
w.title('Trueno Chocolate')
w.geometry('400x200')
w.config(bg='purple')
titulo=tk.Label(w, text='Control de LED RGB, Motor DC, Servomotor', bg='yellow', font=('Arial,20')).place(x=25,y=0)
led=tk.Button(w, text='LED RGB', relief=tk.GROOVE, command=ledrgbwindow).place(x=10, y=50)
turninrgb=tk.Button(w, text='TURNING RGB', relief=tk.GROOVE, command=rgbwindow).place(x=10, y=80)
ledcolor=tk.IntVar()
w.mainloop()
#rgb window  

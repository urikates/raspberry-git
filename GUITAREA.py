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

#RGB Window
def ledrgbwindow():
    print("ejecutando")
    w2=tk.Toplevel(w)
    w2.geometry('400x200')
    w2.config(bg='white')
    l2=tk.Label(w2, text='LED RGB', bg='white', font=('Arial',20)).pack()
    rb1=tk.Radiobutton(w2, text='Red', bg='red', variable=ledcolor, value=1, command=ledcontrol, width=20, font=('arial',20)).pack()
    rb2=tk.Radiobutton(w2, text='Green', bg='green', variable=ledcolor, value=2, command=ledcontrol, width=20, font=('arial',20)).pack()
    rb3=tk.Radiobutton(w2, text='Blue', bg='blue', variable=ledcolor, value=3, command=ledcontrol, width=20, font=('arial',20)).pack()
    rb4=tk.Radiobutton(w2, text='Off', bg='black', fg='white', variable=ledcolor, value=4, command=ledcontrol, width=20, font=('arial',20)).pack()

#Motor Window
def motorwindow():
    
#RGB Function
def ledcontrol():
    color=ledcolor.get()
    if color==1:
        print('Red On')
        GPIO.output(3,False)
        GPIO.output(5,True)
        GPIO.output(7,True)
    elif color==2:
        print('Green On')
        GPIO.output(3,True)
        GPIO.output(5,False)
        GPIO.output(7,True)
    elif color==3:
        print('Blue On')
        GPIO.output(3,True)
        GPIO.output(5,True)
        GPIO.output(7,False)
    elif color==4:
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
ledrgb=tk.Button(w, text='LED RGB', relief=tk.GROOVE, command=ledrgbwindow).place(x=10, y=50)
motorbot=tk.Button(w, text='Motor DC', relief=tk.GROOVE, command=motorwindow).place(x=50, y=50)
ledcolor=tk.IntVar()
w.mainloop()
#rgb window  


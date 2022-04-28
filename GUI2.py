import tkinter as tk
from tkinter import messagebox
import time
from click import command

def fun1():
    messagebox.showinfo('Échale ganas', 'Ponte pilas')
    
def fun2():
    messagebox.showwarning('Cuidado', 'No hay morras con pito, solo vatos con tetas')

def fun3():
    messagebox.showerror('Chale', 'La uni no era lo que pensaba')
    
def fun4():
    messagebox.askretrycancel('Ojo','Cuidao con quien te metes')

def fun5():
    messagebox.askyesno('Testing', 'Uriel Villavicencio Ramirez')

def fun6():
    messagebox.askquestion('Titulo', 'Probanding')
    
def fun7():
    messagebox.showinfo('Tiempo', 'Valor: '+str(varCheck.get()))
    time.sleep(5)
    w.destroy()
    
w=tk.Tk()
w.config(bg='white')
w.title('GUI')
w.geometry('400x200')
b1=tk.Button(w, text='B1', relief=tk.RAISED, bg='gold', command=fun1).grid(row=0, column=0)
b2=tk.Button(w, text='B2', relief=tk.GROOVE, bg='coral', command=fun2).grid(row=0, column=1)
b3=tk.Button(w, text='B3', relief=tk.RAISED, bg='khaki', command=fun3).grid(row=1, column=0)
b4=tk.Button(w, text='B4', relief=tk.GROOVE, bg='plum1', command=fun4).grid(row=1, column=1)
b5=tk.Button(w, text='B5', relief=tk.RAISED, bg='yellow', command=fun5).grid(row=2, column=0)
b6=tk.Button(w, text='B6', relief=tk.GROOVE, bg='snow', command=fun6).grid(row=2, column=1)
varCheck=tk.IntVar()
c1=tk.Checkbutton(w, text='On', variable=varCheck, command=fun7).grid(row=3, column=0)
w.mainloop()
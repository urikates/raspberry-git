import tkinter as tk

contador=0

def fun():
    global contador
    contador= contador+1
    l1.config(text='Temporizador: '+str(contador))
    w.after(1000,fun)

w=tk.Tk()
w.title('Temporizador')
w.geometry('400x200')
w.config(bg='white')
l1=tk.Label(w,text='Temporizador: 00')
l1.place(x=0,y=0)
b1=tk.Button(w, text='Iniciar', command=fun, bg='green')
b1.place(x=50,y=20)

w.mainloop()
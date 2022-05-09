import tkinter as tk

def fun(valor):
    print(varI.get())

def fun2(valor2):
    print(varD.get())

w=tk.Tk()
w.title("Top Level GUI")
w.geometry("400x200")
w.config(bg='coral')
l1=tk.Label(w, text='CONTROL DE MOTOR DC', font=('Arial',15), width=25)
l1.place(x=0,y=0)
varD=tk.DoubleVar()
s2=tk.Scale(w, from_=0,to=100, variable=varD, resolution=0.5, command=fun2, orient=tk.HORIZONTAL, bg='purple', length=100)
s2.place(x=0,y=100)

w2=tk.Toplevel(w)
l2=tk.Label(w2, text='CONTROL DE SERVOMOTORES', font=('Arial',15), width=50)
l2.place(x=0,y=0)
varI=tk.IntVar()
s1=tk.Scale(w2, from_=0,to=180, variable=varI, command=fun)
s1.place(x=0,y=100)


w.mainloop()
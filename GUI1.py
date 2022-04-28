import tkinter as tk

def fun():
    if var.get()==1:
        print('Red')
    elif var.get()==2:
        print('Blue')
    elif var.get()==3:
        print('Green')
    else:
        print('ERROR')

def fun2():
    print(varsentido.get())

def fun3():
    print(varsentido.get())

w=tk.Tk()
w.geometry('300x200')
w.config(bg='black')
w.title('Radio Button')
l1=tk.Label(w, text='GUI', bg='blue', fg='red').pack()
var=tk.IntVar()
r1=tk.Radiobutton(w, text='Red', bg='red', variable=var, value=1, command=fun).pack()
r2=tk.Radiobutton(w, text='Blue', bg='blue', variable=var, value=2, command=fun).pack()
r3=tk.Radiobutton(w, text='Green', bg='green', variable=var, value=3, command=fun).pack()
varsentido=tk.IntVar()
r4=tk.Radiobutton(w, text='------>', variable=varsentido, value=10, command=fun2).pack()
r5=tk.Radiobutton(w, text='<------', variable=varsentido, value=20, command=fun3).pack()
l2=tk.Label(w, text='Uriel Villavicencio Ramirez', bg='pink', fg='purple').pack()
w.mainloop()
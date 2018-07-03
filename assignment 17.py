# ques 1
import tkinter as tk
from tkinter import *
def destroy():
    m.destroy()
m=tk.Tk()
m.title("abhishek")
var=StringVar()
label=Label(m,textvariable=var)
var.set("hello world")
button=tk.Button(m,text='exit',width=25,command=destroy)
label.pack()
button.pack()
m.mainloop()

## ques 2
m=tk.Tk()
m.title("abhishek")
def abhishek():
    var=StringVar()
    label=Label(m,textvariable=var)
    var.set("my name is abhi")
    label.pack()
button=tk.Button(m,text='display',width=35,command=abhishek)
button.pack()
m.mainloop

### ques 3
from tkinter import *
import tkinter as tk
s=tk.Tk()
s.title("kashyap")
def ab():
    s.destroy()
button1 = tk.Button(s, text='exit',width=25,command=ab)
button1.pack()
def abh():
    var1 = StringVar()
    label1 = Label1(s, textvariable=var1)
    var1.set("my name is kashyap")
    label11.pack()
    label12.destroy()
button2 = tk.Button(s, text='name',command=abh)
button2.pack()
var2 = StringVar()
label2 = Label(s, textvariable=var2)
var2.set("my name is abhishek")
label2.pack()
s.mainloop()

####ques4

from tkinter import *
import tkinter
import tkinter as tk
z=tk.Tk()
z.title("abhishek kashyap")
l1=Label(z,text='name')
l1.grid(row=0)
e1=Entry(z)
e1.grid(row=0,column=3)
def abhish():
    e=e1.get()
    print(e)
    z.destroy()
b1=Button(z,text='enter',width=25,command=abhish)
b1.grid(row=4,column=4)

mainloop()
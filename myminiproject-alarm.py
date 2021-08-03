from tkinter import *
import datetime
from tkinter import messagebox
from tkinter.ttk import *
import winsound
obj=Tk()
def alarm():
    if(c1.get()=="AM"):
        x=int(e1.get())
        y=int(e2.get())
    if(c1.get()=="PM"):
        x=int(e1.get())+12
        y=int(e2.get())
    messagebox.showinfo("notification","alarm has been set")
    while(True):
        if(x==datetime.datetime.now().hour and y==datetime.datetime.now().minute):
            for i in range(0,100):
                winsound.Beep(1000,100)
            messagebox.showinfo("notification","WAKE UP")
            break
obj.geometry("400x200")
l1=Label(obj,text="HOURS:")
l2=Label(obj,text="MINUTES:")
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
e1=Entry(obj)
e2=Entry(obj)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
b1=Button(obj,text="SET ALARM",command=alarm)
b1.grid(row=2,column=1)
c1=Combobox(obj,values=["AM","PM"])
c1.grid(row=0,column=2)
l3=Label(obj,text="AM OR PM")
l3.grid(row=0,column=3)
obj.mainloop()

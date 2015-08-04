#!/usr/bin/env python


from Tkinter import *


def resize(ev=None):
    label.config(font='Helvetica -%d bold ' % scale.get())
top = Tk()
top.geometry('400x300')
label = Label(top, text='Hello world!', font='Helvetica -12 bold')
label.pack(fill=Y, expand=1)
scale = Scale(top, from_ = 10, to = 1000, orient = HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=X, expand=1)
quit = Button(top, text='quit', command=top.quit,
                      activebackground='red', activeforeground='white')

quit.pack()

mainloop()

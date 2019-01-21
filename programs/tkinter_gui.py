# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 14:34:58 2019

@author: joshu
see tutorial details here: https://www.tutorialspoint.com/python/python_gui_programming.htm
"""

import tkinter
import tkinter.messagebox as tkMessageBox

top = tkinter.Tk()

# %% buttons

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

B = tkinter.Button(top, text ="Hello", command = helloCallBack)
D = tkinter.Button(top, text ="How are you doing?", command = helloCallBack)

B.pack()
D.pack()
#top.mainloop()

# %% canvas

C = tkinter.Canvas(top, bg="blue", height=250, width=300)

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")

#C.pack()
top.mainloop()
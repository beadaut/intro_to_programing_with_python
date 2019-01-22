# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 14:34:58 2019

@author: joshu
see tutorial details here: https://www.tutorialspoint.com/python/python_gui_programming.htm
"""

import tkinter
import tkinter.messagebox as tkMessageBox

top = tkinter.Tk()

# %% buttons and message boxes
# https://www.tutorialspoint.com/python/tk_button.htm
# https://www.tutorialspoint.com/python/tk_pack.htm

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

B = tkinter.Button(top, text ="Hello", command = helloCallBack, fg="blue")
D = tkinter.Button(top, text ="How are you doing?", command = helloCallBack)

B.pack(side=tkinter.LEFT)
#D.pack()
#top.mainloop()

# %% canvas
# https://www.tutorialspoint.com/python/tk_canvas.htm

C = tkinter.Canvas(top, bg="blue", height=250, width=300)

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")

#C.pack()


# %% message
# https://www.tutorialspoint.com/python/tk_message.htm
var = tkinter.StringVar() # you can change the content of the variable with time
label = tkinter.Message(top, text="Where are you now? \nI know where I am but do you?")
#label = tkinter.Message(top, textvariable=var)
#label = tkinter.Message( top, textvariable=var, relief=tkinter.RAISED )

var.set("Hey!?\nHow are you doing?")
label.pack()

# %% grid: arrange widget in grids
#for r in range(3):
#   for c in range(4):
#      tkinter.Label(top, text='R%s/C%s'%(r,c),
#         borderwidth=1 ).grid(row=r,column=c)

# %%
B.place(bordermode=tkinter.OUTSIDE, height=100, width=100)

top.mainloop()
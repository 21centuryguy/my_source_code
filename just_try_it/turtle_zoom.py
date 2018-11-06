import turtle
import Tkinter
import time

root = Tkinter.Tk()
START_WIDTH = 700 
START_HEIGHT = 700 

frame = Tkinter.Frame(root, width=START_WIDTH, height=START_HEIGHT)
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

xscrollbar = Tkinter.Scrollbar(frame, orient=Tkinter.HORIZONTAL)
xscrollbar.grid(row=1, column=0, sticky=Tkinter.E+Tkinter.W)

yscrollbar = Tkinter.Scrollbar(frame, orient=Tkinter.VERTICAL)
yscrollbar.grid(row=0, column=1, sticky=Tkinter.N+Tkinter.S)

canvas = Tkinter.Canvas(frame, width=START_WIDTH, height=START_HEIGHT,
                        scrollregion=(0, 0, START_WIDTH, START_HEIGHT),
                        xscrollcommand=xscrollbar.set,
                        yscrollcommand=yscrollbar.set)

canvas.grid(row=0, column=0, sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)

xscrollbar.config(command=canvas.xview)
yscrollbar.config(command=canvas.yview)

frame.pack()

turt = turtle.RawTurtle(canvas)
time.sleep(100)
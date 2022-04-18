from tkinter import *

class UIFrame(Frame):
    def __init__(self, window):
        Frame.__init__(self,window, bg = '#355C7D', pady=10)
        button = Button(self, text='Play')
        button.pack()
        

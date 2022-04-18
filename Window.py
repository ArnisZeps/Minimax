from tkinter import *

class Window(Tk):
    def __init__(self, title, sizeX, sizeY):  
        Tk.__init__(self)
        self.resizable(False, False)
        self.title(title)
        self.geometry(str(sizeX)+'x'+str(sizeY))
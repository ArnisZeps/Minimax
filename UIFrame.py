from tkinter import *
from turtle import left

class UIFrame(Frame):
    def __init__(self, window, gameManager):
        self.gameManager = gameManager
        Frame.__init__(self,window, bg = '#355C7D', pady=10)
        rightPane = Frame(self)
        rightPane.pack(side=RIGHT, expand=True)
        button = Button(rightPane, text='Play', command=gameManager.startGame)
        button.pack()
        leftPane = Frame(self)
        leftPane.pack(side=LEFT, expand=True)
        self.playerSelect = None
        R1 = Radiobutton(leftPane, text="Player one", variable=self.playerSelect, value=1)
        R1.pack()
        R2 = Radiobutton(leftPane, text="Player two", variable=self.playerSelect, value=2)
        R2.pack()
    
    def getPlayerSelect(self):
        return self.playerSelect
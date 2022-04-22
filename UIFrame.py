from tkinter import *
from turtle import left

class UIFrame(Frame):
    def __init__(self, window, gameManager):
        self.gameManager = gameManager
        Frame.__init__(self,window, bg = '#355C7D', pady=10)
        rightPane = Frame(self)
        rightPane.pack(side=RIGHT, expand=True)
        self.button = Button(rightPane, text='Play', command=self.playPressed)
        self.button.pack()
        leftPane = Frame(self)
        leftPane.pack(side=LEFT, expand=True)
        self.playerSelect = StringVar(None, "PLAYER_ONE")
        self.R1 = Radiobutton(leftPane, text="Player one", variable=self.playerSelect, value="PLAYER_ONE")
        self.R1.pack()
        self.R2 = Radiobutton(leftPane, text="Player two", variable=self.playerSelect, value="PLAYER_TWO")
        self.R2.pack()
    
    def playPressed(self):
        self.button.config(text = "Restart")
        self.gameManager.startGame(self.playerSelect.get())
        
    def getPlayerSelect(self):
        return self.playerSelect
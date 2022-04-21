from tkinter import *
from Window import Window
from GameFrame import GameFrame
from UIFrame import UIFrame
from GameCanvas import GameCanvas
from GamePointManager import GamePointManager
from GameLineManager import GameLineManager
from CanvasEventHandler import CanvasEventHandler
from GameManager import GameManager
from AI import AI

window = Window("Lines", 1024 ,576)

gameFrame = GameFrame(window)
gameFrame.pack(expand=True, fill=BOTH)

gameCanvas = GameCanvas(gameFrame)
gameCanvas.pack(expand=True, fill=BOTH)
gameCanvas.update()

gamePointManager = GamePointManager(gameCanvas, 8)
# gamePointManager.drawPoints()

gameLineManager = GameLineManager(gameCanvas)

ai = AI(gamePointManager, gameLineManager, 'PLAYER_TWO', gameLineManager, gamePointManager)
gameManager = GameManager(ai, gamePointManager, gameLineManager)

uIFrame = UIFrame(window, gameManager)
uIFrame.pack(side="bottom", fill=BOTH)

canvasEventHandler = CanvasEventHandler(gameCanvas,
                                        uIFrame,
                                        gamePointManager, 
                                        gameLineManager, 
                                        gameManager)        
                                        
gameCanvas.bind("<Button-1>", canvasEventHandler.handleClick)

window.mainloop()


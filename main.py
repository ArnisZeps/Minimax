from tkinter import *
from Window import Window
from GameFrame import GameFrame
from UIFrame import UIFrame
from GameCanvas import GameCanvas
from PointManager import PointManager
from LineManager import LineManager
from CanvasEventHandler import CanvasEventHandler
from GameManager import GameManager

window = Window("Lines", 1024 ,576)

gameFrame = GameFrame(window)
gameFrame.pack(expand=True, fill=BOTH)

gameCanvas = GameCanvas(gameFrame)
gameCanvas.pack(expand=True, fill=BOTH)
gameCanvas.update()

pointManager = PointManager(gameCanvas, 8)
# pointManager.drawPoints()

lineManager = LineManager(gameCanvas)

gameManager = GameManager(pointManager, lineManager, gameCanvas)

uIFrame = UIFrame(window, gameManager)
uIFrame.pack(side="bottom", fill=BOTH)

canvasEventHandler = CanvasEventHandler(gameCanvas,
                                        uIFrame,
                                        pointManager, 
                                        lineManager, 
                                        gameManager)        
                                        
gameCanvas.bind("<Button-1>", canvasEventHandler.handleClick)

window.mainloop()


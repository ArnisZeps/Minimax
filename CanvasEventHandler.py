from tkinter import *
from GameFieldLine import GameFieldLine

class CanvasEventHandler:
    CLICKED = False
    START_POINT_BUFFER = None
    END_POINT_BUFFER = None

    def __init__(self, canvas, uIFrame, gamePointManager, gameLineManager, gameManager):
        self.canvas = canvas
        self.uIFrame = uIFrame
        self.gamePointManager = gamePointManager
        self.gameLineManager = gameLineManager
        self.gameManager = gameManager
    
    def handleClick(self, event):
        gamePoints = self.gamePointManager.getGamePoints()
        if(not self.CLICKED):
            for point in gamePoints:
                if((event.x >= point.getX() - 10 and event.x <= point.getX() + 10) and ((event.y >= point.getY() - 10 and event.y <= point.getY() + 10))):
                    self.START_POINT_BUFFER = point
                    self.CLICKED = True
                    break
        else:
            for point in gamePoints:
                if((event.x >= point.getX() - 10 and event.x <= point.getX() + 10) and ((event.y >= point.getY() - 10 and event.y <= point.getY() + 10))):
                    self.END_POINT_BUFFER = point
                    if(self.gameLineManager.canExist(GameFieldLine(self.START_POINT_BUFFER, self.END_POINT_BUFFER))):
                        self.gameLineManager.drawLine(self.START_POINT_BUFFER, self.END_POINT_BUFFER)
                        self.CLICKED = False
                        self.gameManager.switchPlayer()
                        self.gamePointManager.removeAvailablePoints(self.START_POINT_BUFFER, self.END_POINT_BUFFER)
                        break

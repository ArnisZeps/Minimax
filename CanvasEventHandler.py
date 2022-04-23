from tkinter import *
from GameFieldLine import GameFieldLine

class CanvasEventHandler:
    CLICKED = False
    START_POINT_BUFFER = None
    END_POINT_BUFFER = None

    def __init__(self, canvas, uIFrame, pointManager, lineManager, gameManager):
        self.canvas = canvas
        self.uIFrame = uIFrame
        self.pointManager = pointManager
        self.lineManager = lineManager
        self.gameManager = gameManager
    
    def handleClick(self, event):
        gamePoints = self.pointManager.getGamePoints()
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
                    if(self.lineManager.canExist(GameFieldLine(self.START_POINT_BUFFER, self.END_POINT_BUFFER))):
                        self.lineManager.drawLine(self.START_POINT_BUFFER, self.END_POINT_BUFFER)
                        self.CLICKED = False
                        self.gameManager.handleMove()
                        self.pointManager.removeAvailablePoints(self.START_POINT_BUFFER, self.END_POINT_BUFFER)
                        break

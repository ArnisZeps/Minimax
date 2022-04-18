from tkinter import *

class GameFieldLine():
    def __init__(self, startPoint, endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint

    def getStartPoint(self):
        return self.startPoint

    def getEndPoint(self):
        return self.endPoint
        
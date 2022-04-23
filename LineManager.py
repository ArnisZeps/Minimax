from tkinter import *
from GameFieldLine import GameFieldLine

class LineManager():
    gameLines = []
    def __init__(self, canvas):
        self.canvas = canvas
        
    def resetLines(self):
        self.gameLines = []

    def addLine(self, line):
        self.gameLines.append(line)

    def removeLine(self, line):
        self.gameLines.remove(line)  

    def drawLine(self, startPoint, endPoint):
        self.canvas.create_line(
            startPoint.getX(),
            startPoint.getY(),
            endPoint.getX(),
            endPoint.getY()
        )
        self.addLine(GameFieldLine(startPoint, endPoint))

    def canExist(self, newLine):
        if(len(self.gameLines) == 0):
            return True
        else:       
            for line in self.gameLines:
                if((line.getStartPoint() == newLine.getStartPoint() or line.getStartPoint() == newLine.getEndPoint()) or 
                (line.getEndPoint() == newLine.getStartPoint() or line.getEndPoint() == newLine.getEndPoint())
                ):
                    return False
               
            for line in self.gameLines:
                x1 = line.getStartPoint().getX()
                x2 = line.getEndPoint().getX() 
                x3 = newLine.getStartPoint().getX()
                x4 = newLine.getEndPoint().getX() 
                y1 = (line.getStartPoint().getY()) * - 1 
                y2 = (line.getEndPoint().getY()) * - 1 
                y3 = (newLine.getStartPoint().getY()) * - 1 
                y4 = (newLine.getEndPoint().getY()) * - 1 
                a1 = ((y2 - y1) / (x2 - x1))
                try:
                    a2 = ((y3 - y4) / (x3 - x4))
                except:
                    print("ERR X3: ", x3, " X4: ", x4, " Y3: ", y3, " Y4: ", y4)
                b1 = y1 - a1 * x1
                b2 = y3 - a2 * x3
                xa = (b2 - b1) / (a1 - a2) 
                ya = a2 * xa + b2
                if ((xa < max(x1,x2) ) and (xa > min(x1,x2))):
                    if(ya > min(y3,y4) and  ya < max(y3,y4)):
                        return False
        return True

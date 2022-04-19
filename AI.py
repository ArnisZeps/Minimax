from audioop import minmax
import math
from GameFieldLine import GameFieldLine

class AI():
    def __init__(self, points, lines, playerType, gameLineManager, gamePointManager):
        self.playerType = playerType
        self.points = points
        self.lines = gameLineManager.getLines()
        self.gameLineManager = gameLineManager
        self.gamePointManager = gamePointManager

    def setGameManager(self, gameManager):
        self.gameManager = gameManager

    def getPlayerType(self):
        return self.playerType

    def getHeuristicEvaluation(self):
        eval = 0
        for pointOne in self.gamePointManager.getAvailablePoints():
            for pointTwo in self.gamePointManager.getAvailablePoints():
                if(pointOne != pointTwo):
                    if (not (self.gameLineManager.canExist(GameFieldLine(pointOne, pointTwo)))):
                        eval = eval + 1
        return eval/2

    def miniMax(self, depth, player):
        otherPlayer = 'PLAYER_TWO' if player == 'PLAYER_ONE' else 'PLAYER_ONE'
        bestMove = None
        test = None
        if(depth == 1 ): 
            return self.getHeuristicEvaluation()
        if(self.playerType == 'PLAYER_ONE'):
            bestScore = -math.inf
        else:
            bestScore = math.inf
        for pointOne in self.gamePointManager.getAvailablePoints():
            for pointTwo in self.gamePointManager.getAvailablePoints():
                if(pointOne != pointTwo):
                    if (self.gameLineManager.canExist(GameFieldLine(pointOne, pointTwo))):
                        tmpLine = GameFieldLine(pointOne, pointTwo)
                        self.gameLineManager.addLine(tmpLine)
                        self.gamePointManager.removeAvailablePoints(pointOne, pointTwo)
                        option = self.miniMax(depth + 1, otherPlayer)
                        self.lines.remove(tmpLine)
                        self.gamePointManager.addAvailablePoints(pointOne, pointTwo)
                        if(self.playerType == 'PLAYER_ONE'):
                            if(option>bestScore):
                                bestScore = option      
                                bestMove = [pointOne, pointTwo]
                        else:
                            if(option<bestScore):
                                bestScore = option      
                                bestMove = [pointOne, pointTwo]
        if(bestMove is None ):
            return self.getHeuristicEvaluation()

        if(depth == 0):
            self.gameLineManager.drawLine(bestMove[0], bestMove[1])
            self.gamePointManager.removeAvailablePoints(bestMove[0], bestMove[1])
            print(bestScore)
        else:
            return bestScore

    def makeTurn(self):
        self.miniMax(0, self.playerType)
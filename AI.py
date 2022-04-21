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

    def miniMax(self, depth, player, alpha, beta):
        otherPlayer = 'PLAYER_TWO' if player == 'PLAYER_ONE' else 'PLAYER_ONE'
        bestMove = None
        test = None
        if(depth > 2 ): 
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
        self.miniMax(0, self.playerType, -math.inf, math.inf)




#         import math
# from GameFieldLine import GameFieldLine

# class AI():
#     def __init__(self, points, lines, playerType, gameLineManager, gamePointManager):
#         self.playerType = playerType
#         self.points = points
#         self.lines = gameLineManager.getLines()
#         self.gameLineManager = gameLineManager
#         self.gamePointManager = gamePointManager

#     def setGameManager(self, gameManager):
#         self.gameManager = gameManager

#     def getPlayerType(self):
#         return self.playerType

#     def miniMax(self, depth):
#         winner = self.gameManager.checkState()
#         result = None
#         if(winner == 'PLAYER_ONE'):
#             result = 1
#         elif(winner == 'PLAYER_TWO'):
#             result = -1
#         if(result == -1 or result == 1):
#             return result
#         if(self.playerType == 'PLAYER_TWO'):
#             bestScore = -math.inf
#             for firstPoint in self.gamePointManager.getAvailablePoints():
#                 for secondPoint in self.gamePointManager.getAvailablePoints():
#                     if(firstPoint != secondPoint):
#                         exists = False
#                         for line in self.lines:
#                             if(firstPoint == line.getStartPoint() or firstPoint == line.getEndPoint()):
#                                 exists = True
#                         if(not exists):
#                             if (self.gameLineManager.canExist(GameFieldLine(firstPoint, secondPoint))):
                                # self.gameLineManager.addLine(GameFieldLine(firstPoint, secondPoint))
                                # self.gamePointManager.removeAvailablePoints(firstPoint, secondPoint)
#                                 score = self.miniMax(depth + 1)
                                # for line in self.lines:
                                #     if(firstPoint == line.getStartPoint() or firstPoint == line.getEndPoint()):
                                #         self.lines.remove(line)
#                                 self.gamePointManager.addAvailablePoints(firstPoint, secondPoint)
#                                 if(score > bestScore):
#                                     bestScore = score
#                                     bestMove = [firstPoint, secondPoint]
#             return bestScore


#     def makeTurn(self):
#         bestScore = -math.inf
#         i = 1
#         for firstPoint in self.gamePointManager.getAvailablePoints():
#             for secondPoint in self.gamePointManager.getAvailablePoints():
#                     if(firstPoint != secondPoint):
#                         exists = False
#                         for line in self.lines:
#                             if(firstPoint == line.getStartPoint() or firstPoint == line.getEndPoint()):
#                                 exists = True
#                         if(not exists):
#                             if (self.gameLineManager.canExist(GameFieldLine(firstPoint, secondPoint))):
#                                 self.gameLineManager.addLine(GameFieldLine(firstPoint, secondPoint))
#                                 self.gamePointManager.removeAvailablePoints(firstPoint, secondPoint)
#                                 score = self.miniMax(0)
#                                 i = i+1
#                                 print(i)
#                                 for line in self.lines:
#                                     if(firstPoint == line.getStartPoint() or firstPoint == line.getEndPoint()):
#                                         self.lines.remove(line)
#                                 self.gamePointManager.addAvailablePoints(firstPoint, secondPoint)
#                                 if(score > bestScore):
#                                     bestScore = score
#                                     bestMove = [firstPoint, secondPoint]
        # self.gameLineManager.drawLine(bestMove[0], bestMove[1])
        # self.gamePointManager.removeAvailablePoints(bestMove[0], bestMove[1])
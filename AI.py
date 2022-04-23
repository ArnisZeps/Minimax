from audioop import minmax
import math
from GameFieldLine import GameFieldLine

class AI():
    def __init__(self, playerType, lineManager, pointManager):
        self.playerType = playerType
        self.lineManager = lineManager
        self.pointManager = pointManager

    def setGameManager(self, gameManager):
        self.gameManager = gameManager

    def getPlayerType(self):
        return self.playerType
        
    def getHeuristicEvaluation(self):
        eval = 0
        for pointOne in self.pointManager.getAvailablePoints():
            for pointTwo in self.pointManager.getAvailablePoints():
                if(pointOne != pointTwo):
                    if (not (self.lineManager.canExist(GameFieldLine(pointOne, pointTwo)))):
                        eval = eval + 1
        return eval/2

    def miniMax(self, depth, player, alpha, beta):
        otherPlayer = 'MINIMIZER' if player == 'MAXIMIZER' else 'MAXIMIZER'
        bestMove = None
        test = None
        if(self.gameManager.checkState() != 'STILL ARE MOVES'):
            if(player == 'MAXIMIZER'):
                return -math.inf
            elif(player == 'MINIMIZER'):
                return math.inf
        if(depth > 3):
            return self.getHeuristicEvaluation()
        if(player == 'MAXIMIZER'):
            bestScore = -math.inf
        else:
            bestScore = math.inf
        for pointOne in self.pointManager.getAvailablePoints():
            for pointTwo in self.pointManager.getAvailablePoints():
                if(pointOne != pointTwo):
                    if (self.lineManager.canExist(GameFieldLine(pointOne, pointTwo))):
                        tmpLine = GameFieldLine(pointOne, pointTwo)
                        self.lineManager.addLine(tmpLine)
                        self.pointManager.removeAvailablePoints(pointOne, pointTwo)
                        option = self.miniMax(depth + 1, otherPlayer, alpha, beta)
                        self.lineManager.removeLine(tmpLine)
                        self.pointManager.addAvailablePoints(pointOne, pointTwo)
                        if(player == 'MAXIMIZER'):
                            if(option>bestScore):
                                bestScore = option      
                                bestMove = [pointOne, pointTwo]
                        else:
                            if(option<bestScore):
                                bestScore = option      
                                bestMove = [pointOne, pointTwo]
                        if (player == 'MINIMIZER'):
                            alpha = max(alpha, option)
                        else:
                            beta = min(beta, option)
                        if (beta < alpha):
                            break
        if(bestMove is None ):
            for pointOne in self.pointManager.getAvailablePoints():
                for pointTwo in self.pointManager.getAvailablePoints():
                    if(pointOne != pointTwo):
                        if (self.lineManager.canExist(GameFieldLine(pointOne, pointTwo))):
                            bestMove = [pointOne, pointTwo]

        if(depth == 0):
            self.lineManager.drawLine(bestMove[0], bestMove[1])
            self.pointManager.removeAvailablePoints(bestMove[0], bestMove[1])
            print(bestScore)
        else:
            return bestScore

    def makeTurn(self):
        self.miniMax(0, self.playerType, -math.inf, math.inf)




#         import math
# from GameFieldLine import GameFieldLine

# class AI():
#     def __init__(self, points, lines, playerType, lineManager, pointManager):
#         self.playerType = playerType
#         self.points = points
#         self.lines = lineManager.getLines()
#         self.lineManager = lineManager
#         self.pointManager = pointManager

#     def setGameManager(self, gameManager):
#         self.gameManager = gameManager

#     def getPlayerType(self):
#         return self.playerType

#     def miniMax(self, depth):
#         winner = self.gameManager.checkState()
#         result = None
#         if(winner == 'MAXIMIZER'):
#             result = 1
#         elif(winner == 'MINIMIZER'):
#             result = -1
#         if(result == -1 or result == 1):
#             return result
#         if(self.playerType == 'MINIMIZER'):
#             bestScore = -math.inf
#             for firstPoint in self.pointManager.getAvailablePoints():
#                 for secondPoint in self.pointManager.getAvailablePoints():
#                     if(firstPoint != secondPoint):
#                         exists = False
#                         for line in self.lines:
#                             if(firstPoint == line.getStartPoint() or firstPoint == line.getEndPoint()):
#                                 exists = True
#                         if(not exists):
#                             if (self.lineManager.canExist(GameFieldLine(firstPoint, secondPoint))):
                                # self.lineManager.addLine(GameFieldLine(firstPoint, secondPoint))
                                # self.pointManager.removeAvailablePoints(firstPoint, secondPoint)
#                                 score = self.miniMax(depth + 1)
                                # for line in self.lines:
                                #     if(firstPoint == line.getStartPoint() or firstPoint == line.getEndPoint()):
                                #         self.lines.remove(line)
#                                 self.pointManager.addAvailablePoints(firstPoint, secondPoint)
#                                 if(score > bestScore):
#                                     bestScore = score
#                                     bestMove = [firstPoint, secondPoint]
#             return bestScore


#     def makeTurn(self):
#         bestScore = -math.inf
#         i = 1
#         for firstPoint in self.pointManager.getAvailablePoints():
#             for secondPoint in self.pointManager.getAvailablePoints():
#                     if(firstPoint != secondPoint):
#                         exists = False
#                         for line in self.lines:
#                             if(firstPoint == line.getStartPoint() or firstPoint == line.getEndPoint()):
#                                 exists = True
#                         if(not exists):
#                             if (self.lineManager.canExist(GameFieldLine(firstPoint, secondPoint))):
#                                 self.lineManager.addLine(GameFieldLine(firstPoint, secondPoint))
#                                 self.pointManager.removeAvailablePoints(firstPoint, secondPoint)
#                                 score = self.miniMax(0)
#                                 i = i+1
#                                 print(i)
#                                 for line in self.lines:
#                                     if(firstPoint == line.getStartPoint() or firstPoint == line.getEndPoint()):
#                                         self.lines.remove(line)
#                                 self.pointManager.addAvailablePoints(firstPoint, secondPoint)
#                                 if(score > bestScore):
#                                     bestScore = score
#                                     bestMove = [firstPoint, secondPoint]
        # self.lineManager.drawLine(bestMove[0], bestMove[1])
        # self.pointManager.removeAvailablePoints(bestMove[0], bestMove[1])
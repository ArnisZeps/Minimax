from GameFieldLine import GameFieldLine
class GameManager:
    def __init__(self, ai, gamePointManager, gameLineManager):
        self.playerOne = 'PLAYER_ONE'
        self.playerTwo = 'PLAYER_TWO'
        self.isGameInProgress = False
        self.gameLineManager = gameLineManager
        self.gamePointManager = gamePointManager
        self.currentPlayer = self.playerOne
        self.ai = ai
        self.ai.setGameManager(self)

    def startGame(self):
        if(not self.isGameInProgress):
            self.gamePointManager.createPoints()
            self.gamePointManager.drawPoints()
            if(self.ai.getPlayerType() == self.currentPlayer):
                self.ai.makeTurn()
                self.switchPlayer()

    def getCurrentPlayer(self):
        return self.currentPlayer
    
    def checkState(self):
        for firstPoint in self.gamePointManager.getAvailablePoints(): 
            for secondPoint in self.gamePointManager.getAvailablePoints():
                if(firstPoint != secondPoint): 
                    if(self.gameLineManager.canExist(GameFieldLine(firstPoint, secondPoint))):
                        return 'STILL ARE MOVES'
        return self.currentPlayer

    def switchPlayer(self):
        state = self.checkState()
        if(state == 'STILL ARE MOVES'):
            if(self.currentPlayer == self.playerOne):
                self.currentPlayer = self.playerTwo
            else:
                self.currentPlayer = self.playerOne

            if(self.currentPlayer == self.ai.getPlayerType()):
                self.ai.makeTurn()
                self.switchPlayer()
        else:
            print(state, " WON!")

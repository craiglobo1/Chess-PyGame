import  pygame as pg
from pieces import King, Queen, Bishop, Rook,Knight, Pawn
from constants import boxsize
from utility import drawBoard

class Board:
    def __init__(self):
        self.board = self.piecesInit()
        self.moves = []
        self.movePiece([7,7],[2,0])
        self.movePiece([7,3],[2,2])


        self.selectedPiece = None
        self.playerTurn = "b"

    def piecesInit(self):
        board = [[ None for j in range(8)] for i in range(8)]
        for i in range(8):
            board[1][i] = Pawn(1,i,"w")
        for i in range(8):
            board[6][i] = Pawn(6,i,"b")

        for color in [["w",0],["b",7]]:
            for i in [0,7]:
                board[color[1]][abs(i- 0)] = Rook(color[1], abs(i- 0), color[0])
                board[color[1]][abs(i- 1)] = Knight(color[1], abs(i - 1), color[0])
                board[color[1]][abs(i- 2)] = Bishop(color[1], abs(i - 2), color[0])
            board[color[1]][3] = Queen(color[1],3,color[0])
            board[color[1]][4] = King(color[1],4,color[0])
        return board


    def draw(self, win):
        drawBoard(win)
        for row in self.board:
            for val in row:
                if val != None:
                    val.draw(win)
        
        for val in self.moves:
            pg.draw.circle(win,pg.Color(255,0,0),(val[0]*boxsize + boxsize//2, val[1]*boxsize + boxsize//2),13)
        
    
    def setSelected(self, newSelected):
        newSelected = self.getBoardPos(newSelected)
        if self.board[newSelected[0]][newSelected[1]]:
            if self.board[newSelected[0]][newSelected[1]].color == self.playerTurn:
                if self.selectedPiece:
                    self.board[self.selectedPiece[0]][self.selectedPiece[1]].setSelected(False)
                
                self.board[newSelected[0]][newSelected[1]].setSelected(True)

                for val in self.board:
                    print(val)

                if newSelected == self.selectedPiece:
                    self.board[newSelected[0]][newSelected[1]].setSelected(False)
                    self.selectedPiece = None
                else:
                    self.selectedPiece = newSelected
        if self.selectedPiece:
            self.moves = self.board[self.selectedPiece[0]][self.selectedPiece[1]].getMoveSet(self.board,self.playerTurn)
        else:
            self.moves = []

    
    def movePiece(self, pos1, pos2):
        if self.board[pos1[0]][pos1[1]]:
            self.board[pos1[0]][pos1[1]].row = pos2[0]
            self.board[pos1[0]][pos1[1]].col = pos2[1]
        if self.board[pos2[0]][pos2[1]]:
            self.board[pos2[0]][pos2[1]].row = pos1[0]
            self.board[pos2[0]][pos2[1]].col = pos1[0]

        temp = self.board[pos1[0]][pos1[1]]
        self.board[pos1[0]][pos1[1]] = self.board[pos2[0]][pos2[1]]
        self.board[pos2[0]][pos2[1]] = temp
        

    def getBoardPos(self,point):
        pos = [point[1]//boxsize,point[0]//boxsize]
        return pos

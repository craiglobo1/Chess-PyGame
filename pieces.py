import pygame as pg
from utility import isBlackCell, isInBoard
from constants import boxsize,padding

class Piece:
    def __init__(self,row,col,color):
        self.row = row
        self.col = col
        self.x,self.y = self.col*boxsize,self.row*boxsize
        self.selected = False

        if color == "w":
            self.dir = 1
        elif color == "b":
            self.dir = -1

        self.color = color
        # self.img = pg.transform.scale(pg.image.load(img),(boxsize- padding,boxsize- padding))


    def draw(self,win):
        if self.selected:
            pg.draw.rect(win,(255,0,0),(self.x+5//2,self.y+5//2,boxsize-5,boxsize-5))
            ls = 10
            
            if isBlackCell([self.row,self.col]):
                pg.draw.rect(win,(75,75,75),(self.x+ls//2,self.y+ls//2,boxsize-ls,boxsize-ls))
            else:
                pg.draw.rect(win,(255,255,255),(self.x+ls//2,self.y+ls//2,boxsize-ls,boxsize-ls))
        else:
            if isBlackCell([self.row,self.col]):
                pg.draw.rect(win,(75,75,75),(self.x,self.y,boxsize,boxsize))
            else:
                pg.draw.rect(win,(255,255,255),(self.x,self.y,boxsize,boxsize))
        
        win.blit(self.img,(self.x+padding//2, self.y+padding//2))
    
    def movePiece(self,win, pos2,dt):
        duration = 12
        if dt >= duration:
            self.x = pos2[0]
            self.y = pos2[1]
            return None
        perDone = dt / duration
        xChange = int((pos2[0] - self.x)*perDone)
        yChange = int((pos2[1] - self.y)*perDone)
        self.x = self.x + xChange
        self.y = self.y + yChange

        dt += 1/60
        return dt

    def setSelected(self,selected):
        self.selected = selected

class King(Piece):
    def __init__(self,row,col,color):
        super().__init__(row,col,color)
        self.img = pg.transform.scale(pg.image.load(f"imgs\{color}_king_1x_ns.png"),(boxsize- padding,boxsize- padding))
    
    def __repr__(self) -> str:
        return "king"

class Queen(Piece):
    def __init__(self,row,col,color):
        super().__init__(row,col,color)
        self.img = pg.transform.scale(pg.image.load(f"imgs\{color}_queen_1x_ns.png"),(boxsize- padding,boxsize- padding))
    
    def getMoveSet(self, board, playerTurn):
        bis = Bishop(self.row,self.col,self.color)
        rook = Rook(self.row,self.col,self.color)
        moveSet = bis.getMoveSet(board,playerTurn) + rook.getMoveSet(board,playerTurn)
        return moveSet

    
    def __repr__(self) -> str:
        return "quen"

class Bishop(Piece):
    def __init__(self,row,col,color):
        super().__init__(row,col,color)

        self.img = pg.transform.scale(pg.image.load(f"imgs\{color}_bishop_1x_ns.png"),(boxsize- padding,boxsize- padding))

    def getMoveSet(self, board, playerTurn):
        moveSet = []

        for upLeft in range(min(self.row,self.col)):
            newX = self.col - 1  - upLeft
            newY = self.row - 1 - upLeft

            if board[newY][newX]:
                if board[newY][newX].color == playerTurn:
                    print(newX,newY, "broken")
                    break
                else:
                    moveSet.append([newX,newY])
                    break
            moveSet.append([newX,newY])

        for upRight in range(min(self.row ,7-self.col)):
            newX = self.col + 1 + upRight
            newY = self.row -1  - upRight
            if isInBoard([newY, newX]):
                print(newY, newX)
                if board[newY][newX]:
                    if board[newY][newX].color == playerTurn:
                        break
                    else:
                        moveSet.append([newX,newY])
                        break
                moveSet.append([newX,newY])
        
        for downRight in range(max(7-self.row,7-self.col)):
            newX = self.col + 1 + downRight
            newY = self.row + 1 + downRight
            if isInBoard([newX, newY]):
                if board[newY][newX]:
                    if board[newY][newX].color == playerTurn:
                        break
                    else:
                        moveSet.append([newX,newY])
                        break
                moveSet.append([newX,newY])

        for downLeft in range(min(7-self.row,self.col)):
            newX = self.col - 1 - downLeft
            newY = self.row + 1 + downLeft
            if isInBoard([newY, newX]):
                if board[newY][newX]:
                    if board[newY][newX].color == playerTurn:
                        break
                    else:
                        moveSet.append([newX,newY])
                        break
                moveSet.append([newX,newY])
        return moveSet
        

    def __repr__(self) -> str:
        return "Bshp"

class Knight(Piece):
    def __init__(self,row,col,color):
        super().__init__(row,col,color)
        self.img = pg.transform.scale(pg.image.load(f"imgs\{color}_knight_1x_ns.png"),(boxsize- padding,boxsize- padding))
    
    def getMoveSet(self,board, playerTurn):
        moveSet = []
        X = [2, 1, -1, -2, -2, -1, 1, 2]
        Y = [1, 2, 2, 1, -1, -2, -2, -1]
        
        for i in range(8):
            newX = self.row + X[i]
            newY = self.col + Y[i]
            if isInBoard([newX,newY]):
                if board[newX][newY]:
                    if board[newX][newY].color == playerTurn:
                        continue
                moveSet.append([newY, newX])
        return moveSet

    
    def __repr__(self) -> str:
        return "kngt"

class Rook(Piece):
    def __init__(self,row,col,color):
        super().__init__(row,col,color)
        self.img = pg.transform.scale(pg.image.load(f"imgs\{color}_rook_1x_ns.png"),(boxsize- padding,boxsize- padding))
    
    def getMoveSet(self, board, playerTurn):
        u = d = self.row
        l = r = self.col
        moveSet = []

        for up in range(u-1,-1,-1):
            if board[up][self.col]:
                if board[up][self.col].color == playerTurn:
                    break
                moveSet.append([self.col,up])
                break       

            moveSet.append([self.col, up])

        for left in range(l-1,-1,-1):
            if board[self.row][left]:
                if board[self.row][left].color == playerTurn:
                    break
                moveSet.append([left,self.row])
                break

            moveSet.append([left, self.row])
        
        for down in range(d+1,8):
            if board[down][self.col]:
                if board[down][self.col].color == playerTurn:
                    break
                moveSet.append([self.col,down])
                break

            moveSet.append([self.col,down])

        for right in range(r+1,8):
            if board[self.row][right]:
                if board[self.row][right].color == playerTurn:
                    break
                moveSet.append([right, self.row])
                break
            moveSet.append([right, self.row])
        return moveSet
    
    def __repr__(self) -> str:
        return "rook"

            


class Pawn(Piece):
    def __init__(self,row,col,color):
        super().__init__(row,col,color)
        self.img = pg.transform.scale(pg.image.load(f"imgs\{color}_pawn_1x_ns.png"),(boxsize- padding,boxsize- padding))

    def getMoveSet(self,board,playerTurn):
        moveSet = []
        if self.color == "w":
            dir = 1
        else:
            dir =-1
        curRow = self.row
        curCol = self.col
        for i in range(2):
            curRow += dir
            curCol += dir
            if board[curRow][self.col]:
                break
            moveSet.append([self.col, curRow])
        
        if isInBoard([self.row+dir, self.col+1]):
            if board[self.row+dir][self.col+1]:
                if board[self.row+dir][self.col+1].color != playerTurn:
                    moveSet.append([self.col+1,self.row+dir])

        if isInBoard([self.row+dir, self.col-1]):
            if board[self.row+dir][self.col-1]:
                if board[self.row+dir][self.col-1].color != playerTurn:
                    moveSet.append([self.col-1,self.row+dir])

        return moveSet


    def __repr__(self) -> str:
        return "pawn"


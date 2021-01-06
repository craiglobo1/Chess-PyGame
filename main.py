import pygame as pg
from constants import boxsize
from board import Board
from utility import drawBoard

size = width,height  = 8*boxsize,8*boxsize
FPS = 60

class Game:
    def __init__(self):
        pg.font.init()
        pg.init()
        self.win = pg.display.set_mode(size,pg.SRCALPHA)
        pg.display.set_caption("platformer")
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        self.board = Board()
        drawBoard(self.win)
        self.run()
    
    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            # check for closing window
            pos = pg.mouse.get_pos()
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False

            if event.type == pg.MOUSEBUTTONUP:
                self.board.setSelected(pos)
                print(self.board.getBoardPos(pos))
                
                    
    def update(self):
        pass

    def draw(self):
        self.board.draw(self.win)
        pg.display.flip()

g = Game()

g.new()

pg.quit()
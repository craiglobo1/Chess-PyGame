import pygame as pg

class Ball:
    def __init__(self) -> None:
        self.x = 100
        self.y = 100
        self.moving = False

    def moveBall(self, win, pos2,dt):
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

pg.font.init()
pg.init()
win = pg.display.set_mode((500,500),pg.SRCALPHA)
pg.display.set_caption("platformer")
clock = pg.time.Clock()
running = True
ball = Ball()
dt = 0.1
while running:
    clock.tick(60)
    for event in pg.event.get():
        pos = pg.mouse.get_pos()
        if event.type == pg.QUIT:
            if running:
                running = False

    if dt:
        dt = ball.moveBall(win,(201,458),dt)
    pg.draw.circle(win,(255,0,0),(ball.x,ball.y),15)
    
    pg.display.flip()
    win.fill((0,0,0))


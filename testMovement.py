import pygame as pg

class Ball:
    def __init__(self) -> None:
        self.x = 100
        self.y = 100

    def moveBall(win, pos1,pos2,dt):
        duration = 1
        if dt >= duration:
            return None
        perDone = dt / duration
        xChange = int((pos2[0] - pos1[0])*perDone)
        yChange = int((pos2[1] - pos1[1])*perDone)
        ans = (pos1[0]+ xChange,pos1[1]+ yChange)

        pg.draw.circle(win,(255,0,0),ans,15)
        dt += 1/60
        return dt

pg.font.init()
pg.init()
win = pg.display.set_mode((500,500),pg.SRCALPHA)
pg.display.set_caption("platformer")
clock = pg.time.Clock()
running = True
dt = 0.1
while running:
    clock.tick(60)
    for event in pg.event.get():
        pos = pg.mouse.get_pos()
        if event.type == pg.QUIT:
            if running:
                running = False

    if dt:
        dt = moveBall(win,(100,100),(201,458),dt)
    
    pg.display.flip()
    win.fill((0,0,0))


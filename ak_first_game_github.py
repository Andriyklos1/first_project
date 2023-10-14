import pygame as pg

pg.init()
back=(255,200,65)
w=500
h=500
mw=pg.display.set_mode((w,h))
mw.fill(back)

clock=pg.time.Clock()
start=True
while start:
    for e in pg.event.get():
        if e.type==pg.QUIT:
            start=False
    pg.display.update()
    clock.tick(40) 


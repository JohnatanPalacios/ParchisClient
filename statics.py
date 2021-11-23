import os
import pygame as pg


path = 'assets/'

WIDTH = 600
HEIGHT = 600
INTERFACE = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Parchis")
CLOCK = pg.time.Clock()
TIME_DELTA = CLOCK.tick(60)/1000.0


BG = pg.image.load(os.path.join(path, 'Tablero.png'))
BG_NICKNAME = pg.image.load(os.path.join(path, 'nickname.png'))
BG_LOADING = pg.image.load(os.path.join(path, 'loading.png'))

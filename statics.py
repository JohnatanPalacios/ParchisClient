import pygame as pg


width = 600
height = 600
INTERFACE = pg.display.set_mode((width, height))
pg.display.set_caption("Parchis")
clock = pg.time.Clock()
time_delta = clock.tick(60)/1000.0


bg = pg.image.load('assets/Tablero.png')
bgNickname = pg.image.load('assets/nickname.png')
bgLoading = pg.image.load('assets/loading.png')

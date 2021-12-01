import pygame as pg
from Maths import Vec2D


class Pawn(pg.sprite.Sprite):
    def __init__(self, **kwargs):
        super().__init__()
        self.current_sprite = 0
        self.image = pg.image.load(kwargs['address']).convert_alpha()
        self.id = kwargs['id']
        self.name = kwargs['name']
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = kwargs['pos']
        self.vel = Vec2D()

    def update(self):
        #self.rect.y = int(self.rect.y + self.vel.y)
        #self.rect.x = int(self.rect.x + self.vel.x)
        pass


class PawnManager:
    def __init__(self, redPawns, greenPawns, yellowPawns, bluePawns):
        self.redPawns = redPawns
        self.greenPawns = greenPawns
        self.yellowPawns = yellowPawns
        self.bluePawns = bluePawns
        self.update()

    def update(self):
        pass
    
    def __movePawns(self):
        for event in pg.event.get():
            # if event.type == pg.QUIT:
            #     run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                # obtener ficha
                # evaluar posición de nuevo lugar
                    # mover al nuevo lugar
                # {
                #     "operation":2,
                #     "pawn_1":1,
                #     "pawn_2":2
                # }
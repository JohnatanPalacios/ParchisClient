import pygame as pg
from Maths import Vec2D


class Ficha(pg.sprite.Sprite):
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
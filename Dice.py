import pygame as pg


class Dice(pg.sprite.Sprite):
    def __init__(self, **kwargs):
        super().__init__()
        self.sprites = self.__build(kwargs['address'], kwargs['size'], kwargs['frames'])
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = kwargs['pos']
    
    def __build(self, address, size, frames):
        _sabana = pg.image.load(address).convert_alpha()
        _sprites = []
        for i in range(frames):
            temp = _sabana.subsurface(size[0] * i, 0, size[0], size[1])
            _sprites.append(pg.transform.scale(temp, (64, 64)))
        return _sprites

    def update(self):
        self.current_sprite += 1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]


class DiceNum(pg.sprite.Sprite):
    def __init__(self, address, pos):
        super().__init__()
        self.image = pg.image.load(address).convert_alpha()
        self.image = pg.transform.scale(self.image, (48, 48))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
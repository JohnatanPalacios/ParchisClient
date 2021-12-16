import pygame as pg


# posiciones para mostrar el resultado de los dados al jugador
# {0:'Amarillo', 1:'Verde', 2:'Rojo', 3:'Azul'}
pPos = {2: [[82, 502], [135, 502]],
        1: [[417, 502], [470, 502]],
        0: [[417, 50], [470, 50]],
        3: [[82, 50], [135, 50]]}


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
    
    def is_clicked(self):
        return pg.mouse.get_pressed()[0] and self.rect.collidepoint(pg.mouse.get_pos())


class DiceNum(pg.sprite.Sprite):
    def __init__(self, address, pos=[0,0]):
        super().__init__()
        self.image = pg.image.load(address).convert_alpha()
        self.image = pg.transform.scale(self.image, (48, 48))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
    
    def setPos(self, pos):
        self.rect.topleft = pos


class DiceManager:
    def __init__(self, dices, diceNums):
        self.dices = dices
        self.diceNums = diceNums
        self.__createDices()
    
    def __createDices(self):
        dice1 = Dice(**{'address': 'assets/spriteDados.png',
                        'size': (157,158),
                        'pos': [235,268],
                        'frames': 4})
        dice2 = Dice(**{'address': 'assets/spriteDados.png',
                        'size': (157,158),
                        'pos': [300,268],
                        'frames': 4})
        self.dices.add(dice1, dice2)
    
    def setDiceNums(self, dices_result, color):
        dr1, dr2 = dices_result
        path1 = 'assets/dado' + str(dr1) + '.png'
        path2 = 'assets/dado' + str(dr2) + '.png'
        pos1, pos2 = pPos[color][0], pPos[color][1]
        
        d1 = DiceNum(path1, pos1)
        d2 = DiceNum(path2, pos2)
        self.diceNums.add(d1, d2)

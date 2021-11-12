import pygame as pg


# posiciones para mostrar el resultado de los dados al jugador
pPos = {'Azul': [[82, 50], [135, 50]],
        'Amarillo': [[417, 50], [470, 50]],
        'Rojo': [[82, 502], [135, 502]],
        'Verde': [[417, 502], [470, 502]]}


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
    def __init__(self, address, pos=[0,0]):
        super().__init__()
        self.image = pg.image.load(address).convert_alpha()
        self.image = pg.transform.scale(self.image, (48, 48))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
    
    def setPos(self, playerActive):
        self.rect.topleft = pPos[playerActive]


class DiceManager:
    def __init__(self, dices, diceNums):
        self.dices = dices
        self.diceNums = diceNums
        self.__diceNumbers = dict()
        self.__createDices()
        self.__createDiceNumbers()
    
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
        
    def __createDiceNumbers(self):
        self.__diceNumbers = {'1': DiceNum('assets/dado1.png'),
                              '2': DiceNum('assets/dado2.png'),
                              '3': DiceNum('assets/dado3.png'),
                              '4': DiceNum('assets/dado4.png'),
                              '5': DiceNum('assets/dado5.png'),
                              '6': DiceNum('assets/dado6.png')}
    
    def setDiceNums(self, d1, d2, playerActive):
        _d1 = self.__diceNumbers[d1].setPos(playerActive)
        _d2 = self.__diceNumbers[d2].setPos(playerActive)
        self.diceNums.add(_d1, _d2)

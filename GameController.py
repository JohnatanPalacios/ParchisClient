import pygame as pg
from Dice import Dice, DiceNum
from BoardLoader import BoardLoader
from statics import INTERFACE, clock, bg, width, height
import pygame_gui



time_delta = clock.tick(60)/1000.0




diceNums = pg.sprite.Group()
dices = pg.sprite.Group()

fichasRojo = pg.sprite.Group()
fichasVerde = pg.sprite.Group()
fichasAmarillo = pg.sprite.Group()
fichasAzul = pg.sprite.Group()


tablero = BoardLoader(['Azul', 'Amarillo', 'Rojo', 'Verde'],
                      fichasAzul, fichasAmarillo, fichasRojo, fichasVerde)

board = tablero.getTablero()

manager = pygame_gui.UIManager((width, height), 'label.json')





# posiciones para mostrar el resultado de los dados al jugador
pPos = {'Azul': [[82, 50], [135, 50]],
        'Amarillo': [[417, 50], [470, 50]],
        'Rojo': [[82, 502], [135, 502]],
        'Verde': [[417, 502], [470, 502]]}





class GameController:
    def __init__(self, nickname):
        self.__createDices()
        self.__nicknames()
        self.__t = 1
        self.nickname = nickname # recuperar los nickname del servidor
        self.__run = True
        self.__throwDice = True
        self.__diceNumbers
    
    def __nicknames(self):
        # crear un for que ubique todos los nicknames
        pygame_gui.elements.UILabel(relative_rect=pg.Rect((20, 20), (100, 25)),
                                    text=self.nickname,
                                    manager=manager)
        
    def main(self):
        while self.__run:
            # crear función para activar los dados
            # crear delay para esperar a que rueden
            # enviar petición con el resultado obtenido

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.__run = False

                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    # función click de las fichas del jugador
            
            
            self.__drawGame()
            self.__updateGroups()
            
            pg.display.flip()
            pg.display.update()
            clock.tick(15)
    
    def __drawGame(self):
        INTERFACE.blit(bg, (0,0))
        if self.__throwDice:
            dices.draw(INTERFACE)
            self.__t += 1
            if self.__t % 40 == 0:
                    print('OK')
                    self.__throwDice = False
                    self.__t = 1
        fichasAzul.draw(INTERFACE)
        fichasAmarillo.draw(INTERFACE)
        fichasRojo.draw(INTERFACE)
        fichasVerde.draw(INTERFACE)
        diceNums.draw(INTERFACE)
        
        manager.update(time_delta)
        manager.draw_ui(INTERFACE)
    
    def __updateGroups(self):
        diceNums.update(INTERFACE)
        dices.update()
        fichasAzul.update()
        fichasAmarillo.update()
        fichasRojo.update()
        fichasVerde.update()
    
    
    # Crear una clase DiceManager para esto
    def __createDices(self):
        dice1 = Dice(**{'address': 'assets/spriteDados.png',
               'size': (157,158),
               'pos': [235,268],
               'frames': 4})
        dice2 = Dice(**{'address': 'assets/spriteDados.png',
                    'size': (157,158),
                    'pos': [300,268],
                    'frames': 4})
        dices.add(dice1, dice2)
        
    def __createDiceNumbers(self):
        self.__diceNumbers = {'1': DiceNum('assets/dado1.png', pPos['Azul'][0]),
                              '2': DiceNum('assets/dado2.png', pPos['Azul'][1]),
                              '3': DiceNum('assets/dado3.png', pPos['Rojo'][0]),
                              '4': DiceNum('assets/dado4.png', pPos['Rojo'][1]),
                              '5': DiceNum('assets/dado5.png', pPos['Verde'][0]),
                              '6': DiceNum('assets/dado6.png', pPos['Verde'][1])}
    
    def __diceNumbers(self):
        diceNums.add()

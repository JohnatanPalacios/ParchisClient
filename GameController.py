import pygame as pg
from Dice import DiceManager
from BoardLoader import BoardLoader
from statics import INTERFACE, clock, bg, width, height, time_delta
import pygame_gui


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


class GameController:
    def __init__(self, nickname):
        self.__player = 'Azul' # consultar que color es este jugador
        self.__nickname = nickname # recuperar los nickname del servidor
        self.__nicknames()
        self.__t = 1
        self.__run = True
        self.__dices = DiceManager(dices, diceNums)
    
    def __nicknames(self):
        # crear un for que ubique todos los nicknames
        pygame_gui.elements.UILabel(relative_rect=pg.Rect((20, 20), (100, 25)),
                                    text=self.__nickname,
                                    manager=manager)
        
    def drawResult(self, playerActive):
        d1, d2 = 3, 4 # consultar al servidor el resultad
        self.__dices.setDiceNums(d1, d2, playerActive)
    
    def __checkTurn(self):
        throwing, playerActive = False, 'Azul' # consultar el servidor
        if playerActive == self.__player:
            dices.draw(INTERFACE)
            self.__t += 1
            if self.__t % 40 == 0:
                self.__t = 1
                # enviar mensaje de terminado el lanzamiento
            if not throwing:
                self.__drawResult(playerActive)
                # permitir mover fichas
                # self.__moveTiles()
        if not throwing:
            self.__drawResult(playerActive)
                
    def __moveTiles(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.__run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                # obtener ficha
                # evaluar posición de nuevo lugar
                    # mover al nuevo lugar
        
    def main(self):
        while self.__run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.__run = False
            
            self.__checkTurn()
            self.__updateGroups()
            self.__drawGame()
            
            pg.display.flip()
            pg.display.update()
            clock.tick(15)
    
    def __drawGame(self):
        INTERFACE.blit(bg, (0,0))
        fichasAzul.draw(INTERFACE)
        fichasAmarillo.draw(INTERFACE)
        fichasRojo.draw(INTERFACE)
        fichasVerde.draw(INTERFACE)
        diceNums.draw(INTERFACE)
        manager.draw_ui(INTERFACE)
    
    def __updateGroups(self):
        manager.update(time_delta)
        diceNums.update(INTERFACE)
        dices.update()
        fichasAzul.update()
        fichasAmarillo.update()
        fichasRojo.update()
        fichasVerde.update()

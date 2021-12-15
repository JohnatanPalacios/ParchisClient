import pygame as pg
from Dice import DiceManager
from Pawn import PawnManager
from BoardLoader import BoardLoader
from statics import INTERFACE, CLOCK, BG, WIDTH, HEIGHT, TIME_DELTA, BG_LOADING
import pygame_gui
from Client import Client


diceNums = pg.sprite.Group()
dices = pg.sprite.Group()
fichasRojo = pg.sprite.Group()
fichasVerde = pg.sprite.Group()
fichasAmarillo = pg.sprite.Group()
fichasAzul = pg.sprite.Group()


tablero = BoardLoader(['Azul', 'Amarillo', 'Rojo', 'Verde'],
                      fichasAzul, fichasAmarillo, fichasRojo, fichasVerde)
board = tablero.getTablero()
manager = pygame_gui.UIManager((WIDTH, HEIGHT), 'label.json')
COLORS = {0:'Azul', 1:'Amarillo', 2:'Rojo', 3:'Verde'}


class GameController:
    def __init__(self, username):
        self.start = False
        self.__ws = Client(username)
        self.__username = username
        self.__color = self.color()
        self.turno = dict()
        self.__run = True
        self.__dices = DiceManager(dices, diceNums)
        self.__pawns = PawnManager(fichasRojo, fichasVerde, fichasAmarillo, fichasAzul)
    
    def color(self):
        for j in self.__ws.jugadores:
            if j["username"] == self.__username:
                self.__color = j["color"]
    
    def __usernames(self):
        # {0:'Azul', 1:'Amarillo', 2:'Rojo', 3:'Verde'}
        if self.__ws.jugadores:
            for j in self.__ws.jugadores:
                if j["color"] == 0:
                    pygame_gui.elements.UILabel(relative_rect=pg.Rect((20, 20), (100, 25)),
                                                text=j["username"],
                                                manager=manager)
                if j["color"] == 1:
                    pygame_gui.elements.UILabel(relative_rect=pg.Rect((480, 20), (100, 25)),
                                                text=j["username"],
                                                manager=manager)
                if j["color"] == 2:
                    pygame_gui.elements.UILabel(relative_rect=pg.Rect((20, 500), (100, 25)),
                                                text=j["username"],
                                                manager=manager)
                if j["color"] == 3:
                    pygame_gui.elements.UILabel(relative_rect=pg.Rect((480, 500), (100, 25)),
                                                text=j["username"],
                                                manager=manager)
    
    def __checkTurn(self):
        if self.__ws.turno:
            if self.__ws.turno['username'] == self.__username:
                dices.draw(INTERFACE)
                for dice in dices:
                    if dice.is_clicked():
                        self.__ws.send({"operation":1})
                if self.__ws.resultado_dados:
                    self.__dices.setDiceNums(self.__ws.resultado_dados, self.__color)
                #-----------------#
                # permitir mover fichas
                # self.__movePawns()
                # {"type": "exit jail", "message": "Your pawns have exit jail"}
                #-----------------#
        
    def __drawGame(self):
        INTERFACE.blit(BG, (0,0))
        fichasAzul.draw(INTERFACE)
        fichasAmarillo.draw(INTERFACE)
        fichasRojo.draw(INTERFACE)
        fichasVerde.draw(INTERFACE)
        diceNums.draw(INTERFACE)
        manager.draw_ui(INTERFACE)
        self.__usernames()
    
    def __updateGroups(self):
        manager.update(TIME_DELTA)
        diceNums.update(INTERFACE)
        dices.update()
        fichasAzul.update()
        fichasAmarillo.update()
        fichasRojo.update()
        fichasVerde.update()
    
    def main(self):
        while self.__run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.__run = False
            
            if not self.start:
                if (len(self.__ws.jugadores) >= 2):
                    self.start = True
                    self.__ws.send({"start_status":"true"})
            else:
                if self.__ws.iniciar:
                    self.__drawGame()
                    self.__checkTurn()
                    self.__pawns.update()
                    self.__updateGroups()
                    
                else:
                    INTERFACE.blit(BG_LOADING, (0,0))

            pg.display.flip()
            pg.display.update()
            CLOCK.tick(10)

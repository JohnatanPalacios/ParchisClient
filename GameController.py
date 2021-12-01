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
nm_rect = pg.Rect((20, 20), (100, 25))
manager = pygame_gui.UIManager((WIDTH, HEIGHT), 'label.json')
COLORS = {0:'Azul', 1:'Amarillo', 2:'Rojo', 3:'Verde'}


class GameController:
    def __init__(self, username):
        self.status = None
        self.operation = None
        self.players = list()
        self.player_status = list()
        self.current_turn = None
        self.dices_result = list()






        self.start = False
        self.__ws = Client(username)
        self.__username = username
        self.__throwing = False
        self.__t = 1 # variable para calcular tiempo de rotacion de los dados
        self.__run = True
        self.__dices = DiceManager(dices, diceNums)
        self.__pawns = PawnManager(fichasRojo, fichasVerde, fichasAmarillo, fichasAzul)
        self.__usernames()

    def __updateData(self):
        data_type = self.__ws.data.get('type')

        if data_type == 'new player':
            self.players = self.__ws.data.get('players')
        elif data_type == 'start_status':
            self.status = self.__ws.data.get('start_status')
        elif data_type == "state":
            self.status = self.__ws.data.get('message')
        elif data_type == "players status":
            self.players = self.__ws.data.get('status')
        elif data_type == "current turn":
            self.current_turn = self.__ws.data.get('current_turn')
        elif data_type == "dice result":
            self.dices_result = self.__ws.data.get('dice_result')
    
    def __usernames(self):
        # imprimir nicknames
        pygame_gui.elements.UILabel(relative_rect=nm_rect, text=self.__username, manager=manager)
    
    def __checkTurn(self):
        if self.current_turn:
            playerActive = self.current_turn.get('username')
            color = COLORS.get(self.current_turn.get('color'))
            if playerActive == self.__username:
                dices.draw(INTERFACE)
                self.__t += 1
                if self.__t % 40 == 0:
                    self.__t = 1
                    self.__ws.send({"operation":1})
                if not self.__throwing:
                    self.__dices.setDiceNums(self.dices_result, color)
                    #-----------------#
                    # permitir mover fichas
                    # self.__movePawns()
                    # {"type": "exit jail", "message": "Your pawns have exit jail"}
                    #-----------------#
            elif not self.__throwing:
                self.__dices.setDiceNums(self.dices_result, color)
    
    def __drawGame(self):
        INTERFACE.blit(BG, (0,0))
        fichasAzul.draw(INTERFACE)
        fichasAmarillo.draw(INTERFACE)
        fichasRojo.draw(INTERFACE)
        fichasVerde.draw(INTERFACE)
        diceNums.draw(INTERFACE)
        manager.draw_ui(INTERFACE)
    
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
            self.__updateData()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.__run = False
            
            if not self.start:
                print(self.players) # punto de verificación
                if (len(self.players) >= 2):
                    self.start = True
                    self.__ws.send({"start_status":"true"})
            else:
                if self.status == "The game has started":
                    self.__checkTurn()
                    self.__pawns.update()
                    self.__updateGroups()
                    self.__drawGame()
                else:
                    INTERFACE.blit(BG_LOADING, (0,0))

            pg.display.flip()
            pg.display.update()
            CLOCK.tick(10)

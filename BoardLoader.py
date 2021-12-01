import json
import pygame as pg
from Pawn import Pawn


f_locate = {'Azul': 'assets/azul.png',
            'Amarillo': 'assets/amarillo.png',
            'Rojo': 'assets/rojo.png',
            'Verde': 'assets/verde.png'}


class BoardLoader:
    def __init__(self, jugadores, fichasAzul, fichasAmarillo, fichasRojo, fichasVerde):
        self.jugadores = jugadores
        self.fichasAzul = fichasAzul
        self.fichasAmarillo = fichasAmarillo
        self.fichasRojo = fichasRojo
        self.fichasVerde = fichasVerde
        self.tablero = dict()
        self.__crearTablero()
        self.__crearFichas()
        self.players = pg.font.SysFont
    
    def getTablero(self):
        return self.tablero
        
    def __crearTablero(self):
        _boardJson = None
        with open('assets/Posiciones.json') as posJson:
            _boardJson = json.load(posJson)
            posJson.close()
        _tableroTemp = _boardJson['layers'][1]['objects']
        for i in _tableroTemp:
            self.tablero[i['name']] = {'taken': False, 'pos': (i['x'], i['y'])}
        
    def __crearFichas(self):
        for j in self.jugadores:
            for i in range(4):
                name = 'carcel' + j + '_' + str(i+1)
                ficha = Pawn(**{'address': f_locate[j],
                                 'id': i+1,
                                 'name': j,
                                 'pos': self.tablero[name]['pos']})
                self.tablero['taken'] = True
                self.fichasAzul.add(ficha)
                        
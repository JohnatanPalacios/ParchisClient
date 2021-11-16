import pygame as pg
from pygame_textinput import TextInputManager, TextInputVisualizer
import pygame_gui
import time
from GameController import GameController
from statics import INTERFACE, clock, bgNickname, bgLoading, width, height
from Client import Client

# PyGame
pg.init()

# Text nickname
manager = TextInputManager(validator = lambda input: len(input) <= 15)
textinput = TextInputVisualizer(manager=manager)
# Button
manager = pygame_gui.UIManager((width, height), 'thems.json')
button_layout_rect = pg.Rect(160, 24, 100, 20)
jugar_button = pygame_gui.elements.UIButton(relative_rect=pg.Rect((480, 279), (100, 50)),
                                            text='Jugar!',
                                            manager=manager)


class Menu:
    def __init__(self, websocket):
        self.ws = websocket
        self.run = True
        self.inputUser = False
        self.nickname = None
        self.time_delta = clock.tick(60)/1000.0

    def print_players(self):
        for key, value in self.ws.data.items():
            print(key, value)

    def loader(self):
        self.inputUser = True
        self.nickname = textinput.value
        c.conn({"username": self.nickname})
        self.print_players()
        # verificar el json que llega para mostrar los jugadores conectados
        # crear un sala para ver los jugadores conectados 
        # {"type": "new player", "players": [{"id": 2, "username": "test_usr", "color": 1}, {"id": 1, "username": "test_usr2", "color": 0}]}
        # el type new player es para ver los jugadores conectados

        # el type start accepted es para ver que jugador aceptó iniciar el juego
        # {"type": "start accepted", "message": {"id": 1, "username": "test_usr2", "color": 0}}

        
        # si hay dos jugadores, habilitar la posibilidad de iniciar juego
        ###### ws.sendMessage({"start_status":"true"}) # enviar esto

        # cuando los jugadores en sala acepten llegará
        # {"type": "state", "message": "The game has started"} # este mensaje
    
    def stop(self):
        self.run = False
        pg.quit()
        # cerrar websocket
    
    def start(self):
        while self.run:
            if not self.inputUser:
                INTERFACE.blit(bgNickname, (0,0))
                events = pg.event.get()
                textinput.update(events)
                INTERFACE.blit(textinput.surface, (208, 295))
                for event in events:
                    if event.type == pg.QUIT:
                        self.stop()
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_RETURN:
                            self.loader()
                    if event.type == pg.USEREVENT:
                        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                            if event.ui_element == jugar_button:
                                self.loader()
                    manager.process_events(event)
                manager.update(self.time_delta)
                manager.draw_ui(INTERFACE)
            else:
                INTERFACE.blit(bgLoading, (0,0))
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.stop()
                        # "state", "message": "The game has started"
                    if True:#['start_status'] == True: # revisar la respuesta del servidor para iniciar
                                # con la orden de iniciar la partida 
                        time.sleep(1)
                        run = False
                        # esperar orden del servidor para iniciar la partida
                        # cambiar conexion por wsapp y respuesta
                        gameController = GameController(self.nickname)
                        gameController.main()
                        
            pg.display.update()
            clock.tick(30)


if __name__ == '__main__':
    c = Client()
    menu = Menu(c)
    menu.start()
    pg.quit()

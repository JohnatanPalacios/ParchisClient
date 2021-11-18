import pygame as pg
from pygame_textinput import TextInputManager, TextInputVisualizer
import pygame_gui as pg_gui
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
manager = pg_gui.UIManager((width, height), 'thems.json')
manager2 = pg_gui.UIManager((width, height), 'thems.json')
button_layout_rect = pg.Rect(160, 24, 100, 20)
send_button = pg_gui.elements.UIButton(relative_rect=pg.Rect((480, 279), (100, 50)),
                                            text='OK!',
                                            manager=manager)
play_button = pg_gui.elements.UIButton(relative_rect=pg.Rect((480, 279), (100, 50)),
                                            text='Jugar!',
                                            manager=manager2)


class Menu:
    def __init__(self, websocket):
        self.ws = websocket
        self.run = True
        self.inputUser = False
        self.username = None
        self.time_delta = clock.tick(60)/1000.0

    def print_players(self):
        # acomodar esto para imprimir los nombres en la ventana
        try:
            for p in self.ws.getPlayers():
                print('--> Player: {}'.format(p))
        except:
            pass
    
    def start(self):
        while self.run:
            if not self.inputUser:
                INTERFACE.blit(bgNickname, (0,0))
                INTERFACE.blit(textinput.surface, (208, 295))
                manager.draw_ui(INTERFACE)
                manager.update(self.time_delta)
                events = pg.event.get()
                textinput.update(events)
                for event in events:
                    if event.type == pg.QUIT:
                        self.run = False
                        break
                    elif event.type == pg.USEREVENT:
                        if event.user_type == pg_gui.UI_BUTTON_PRESSED:
                            if event.ui_element == send_button:
                                self.inputUser = True
                                self.username = textinput.value
                                self.ws.setUsername(self.username)
                    manager.process_events(event)
            else:
                INTERFACE.blit(bgLoading, (0,0))
                self.print_players()
                events = pg.event.get()
                if 2 <= self.ws.countPlayers() <= 4:
                    manager2.draw_ui(INTERFACE)
                    manager2.update(self.time_delta)
                else:
                    print('\n-----ESPERANDO JUGADORES-----\n')
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.run = False
                        break
                    elif event.type == pg.USEREVENT:
                        if event.user_type == pg_gui.UI_BUTTON_PRESSED:
                            if event.ui_element == play_button:
                                self.ws.setGameStart()
                                self.run = False
                                gameController = GameController(self.username, self.ws)
                                gameController.main()
            pg.display.update()
            clock.tick(30)

if __name__ == '__main__':
    c = Client()
    menu = Menu(c)
    menu.start()
    pg.quit()
 
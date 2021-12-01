import pygame as pg
from pygame_textinput import TextInputManager, TextInputVisualizer
import pygame_gui as pg_gui
from GameController import GameController
from statics import INTERFACE, CLOCK, BG_NICKNAME, BG_LOADING, WIDTH, HEIGHT, TIME_DELTA
from Client import Client
from threading import Thread


# Text nickname
manager = TextInputManager(validator=lambda input: len(input) <= 15)
textinput = TextInputVisualizer(manager=manager)
# Button
manager = pg_gui.UIManager((WIDTH, HEIGHT), 'thems.json')
manager2 = pg_gui.UIManager((WIDTH, HEIGHT), 'thems.json')
# button_layout_rect = pg.Rect(160, 24, 100, 20)
btn_rect = pg.Rect((480, 279), (100, 50))
button = pg_gui.elements.UIButton(relative_rect=btn_rect, text='Enviar', manager=manager)


class Menu:
    def __init__(self):
        self.__ws = None
        self.run = True
        self.username = None

    def print_players(self):
        try:
            if self.__ws.players:
                pos = {0: (100,280), 1: (230,280), 2: (100,300), 3: (230,300)}
                fuente = pg.font.Font(None, 30)
                for ply in self.__ws.players:
                    text = fuente.render(ply.get('username'), 1, (255,255,255))
                    INTERFACE.blit(text, pos[ply.get('id')])
        except:
            pass
        # def run(*args):
        #     for ply in self.__ws.players:
        #         text = fuente.render(ply.get('username'), 1, (255,255,255))
        #         INTERFACE.blit(text, pos[ply.get('id')])
        # Thread(target=run).start()

    def start(self):
        while self.run:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT: self.run = False
                manager.process_events(event)
            if not self.username:
                INTERFACE.blit(BG_NICKNAME, (0,0))
                INTERFACE.blit(textinput.surface, (208, 295))
                textinput.update(events)
                if button.check_pressed():
                    self.username = textinput.value
                    self.__ws = Client(username=self.username)
                    button.set_text(text='Jugar!')
            else:
                INTERFACE.blit(BG_LOADING, (0,0))
                self.print_players()
                if 2 <= len(self.__ws.players) <= 4 and button.check_pressed():
                    self.__ws.send({"start_status":"true"})
                    self.run = False
                    gameController = GameController(self.username, self.__ws)
                    gameController.main()
            manager.update(TIME_DELTA)
            manager.draw_ui(INTERFACE)
            pg.display.update()
            CLOCK.tick(15)


if __name__ == '__main__':
    pg.init()
    pg.font.init()
    menu = Menu()
    menu.start()
    pg.quit()
 
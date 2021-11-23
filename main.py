import pygame as pg
from pygame_textinput import TextInputManager, TextInputVisualizer
import pygame_gui as pg_gui
from GameController import GameController
from statics import INTERFACE, CLOCK, BG_NICKNAME, BG_LOADING, WIDTH, HEIGHT, TIME_DELTA
from Client import Client


# Text nickname
manager = TextInputManager(validator=lambda input: len(input) <= 15)
textinput = TextInputVisualizer(manager=manager)
# Button
manager = pg_gui.UIManager((WIDTH, HEIGHT), 'thems.json')
manager2 = pg_gui.UIManager((WIDTH, HEIGHT), 'thems.json')
button_layout_rect = pg.Rect(160, 24, 100, 20)
button = pg_gui.elements.UIButton(relative_rect=pg.Rect((480, 279), (100, 50)),
                                    text='Enviar',
                                    manager=manager)


class Menu:
    def __init__(self, websocket=None):
        self.ws = websocket
        self.run = True
        self.username = None

    def print_players(self):
        pos = {0: (100,280), 1: (230,280),
                2: (100,300), 3: (230,300)}
        fuente = pg.font.Font(None, 30)
        for p in range(len(self.ws.players)):
            text = fuente.render(self.ws.players[p], 1, (255,255,255))
            INTERFACE.blit(text, pos[p])

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
                    self.ws = Client(username=self.username)
                    button.set_text(text='Jugar!')
            else:
                self.print_players()
                INTERFACE.blit(BG_LOADING, (0,0))
                if 2 <= len(self.ws.players) <= 4 and button.check_pressed():
                    self.ws.send({"start_status":"true"})
                    self.run = False
                    gameController = GameController(self.username, self.ws)
                    gameController.main()
            manager.update(TIME_DELTA)
            manager.draw_ui(INTERFACE)
            pg.display.update()
            CLOCK.tick(30)


if __name__ == '__main__':
    pg.init()
    pg.font.init()
    # c = Client()
    menu = Menu()
    menu.start()
    pg.quit()
 
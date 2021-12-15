import pygame as pg
from pygame_textinput import TextInputManager, TextInputVisualizer
import pygame_gui as pg_gui
from GameController import GameController
from statics import INTERFACE, CLOCK, BG_NICKNAME, WIDTH, HEIGHT, TIME_DELTA

# Text nickname
manager = TextInputManager(validator=lambda input: len(input) <= 15)
textinput = TextInputVisualizer(manager=manager)
# Button
manager = pg_gui.UIManager((WIDTH, HEIGHT), 'thems.json')
manager2 = pg_gui.UIManager((WIDTH, HEIGHT), 'thems.json')
# button_layout_rect = pg.Rect(160, 24, 100, 20)
btn_rect = pg.Rect((480, 279), (100, 50))
button = pg_gui.elements.UIButton(relative_rect=btn_rect,
                                    text='Jugar!',
                                    manager=manager)


def menu():
    run = True
    while run:
        INTERFACE.blit(BG_NICKNAME, (0,0))
        INTERFACE.blit(textinput.surface, (208, 295))

        events = pg.event.get()
        textinput.update(events)
        for event in events:
            if event.type == pg.QUIT:
                run = False
            manager.process_events(event)

        if button.check_pressed() and textinput.value:
            pg.display.set_caption("Parchis   " + textinput.value)
            run = False
            return textinput.value
        
        manager.update(TIME_DELTA)
        manager.draw_ui(INTERFACE)
        pg.display.update()
        CLOCK.tick(60)


if __name__ == '__main__':
    pg.init()
    pg.font.init()
    username = menu()
    game = GameController(username)
    game.main()
    pg.quit()
 
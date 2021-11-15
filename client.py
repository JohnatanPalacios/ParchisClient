import pygame as pg
from pygame_textinput import TextInputManager, TextInputVisualizer
import pygame_gui
import json
import websockets
import asyncio
import time
from GameController import GameController
from statics import INTERFACE, clock, bgNickname, bgLoading, width, height

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






class Client:
    def __init__(self, port='8081'):
        self.port = port
        self.uri = "ws://localhost:" + self.port
        self.__startClient()
        
    async def __startClient(self):
        connection = websockets.connect(uri=self.uri)
        async with connection as websocket:
            await asyncio.Future()

        # recibir mensajes
        # async for messsage in websocket:
        #     print(messsage)
            
        # cerrar conexión
        # await websocket.close()
    
    async def send(self, websocket, message):
        await websocket.send(json.dumps(message))
            





conexion = True


def menu_screen():
    run = True
    inputUser = False
    nickname = None
    time_delta = clock.tick(60)/1000.0
    while run:
        if not inputUser:
            INTERFACE.blit(bgNickname, (0,0))
            events = pg.event.get()
            textinput.update(events)
            INTERFACE.blit(textinput.surface, (208, 295))
            
            for event in events:
                if event.type == pg.QUIT:
                    run = False
                    pg.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        print('Cargando juego...')
                        inputUser = True
                        nickname = textinput.value
                if event.type == pg.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == jugar_button:
                            print('Cargando juego...')
                            inputUser = True
                            nickname = textinput.value
                            #### enviar nickname al servidor
                
                manager.process_events(event)
            manager.update(time_delta)
            manager.draw_ui(INTERFACE)
        else:
            INTERFACE.blit(bgLoading, (0,0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    run = False
                if conexion: # esta conexión debe ser una respuesta del servidor
                             # con la orden de iniciar la partida 
                    time.sleep(1)
                    run = False
                    # esperar orden del servidor para iniciar la partida
                    # cambiar conexion por wsapp y respuesta
                    gameController = GameController(nickname)
                    gameController.main()
                    
        pg.display.update()
        clock.tick(30)


#########################
# wsapp = websocket.WebSocketApp()
# wsapp = websocket.WebSocketApp("wss://stream.meetup.com/2/rsvps", cookie="chocolate")
# wsapp.run_forever(origin="testing_websockets.com", host="127.0.0.1")
# wsapp.close(status=websocket.STATUS_PROTOCOL_ERROR)
# Alternatively, use wsapp.close(status=1002)
#########################


if __name__ == '__main__':
    menu_screen()
    pg.quit()
        

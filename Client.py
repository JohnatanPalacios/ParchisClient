import json
import websocket
from threading import Thread


class Client:
    def __init__(self, port='8081', username=''):
        self.username = username
        self.port = port
        self.ws = None
        self.status = None
        self.operation = None
        self.players = list()
        self.player_status = list()
        self.current_turn = None
        self.dices_result = list()
        #### create conexion ####
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp("ws://localhost:" + self.port + "/",
                                            on_open = self.on_open,
                                            on_message = self.on_message,
                                            on_error = self.on_error)
        self.ws.run_forever()

    def on_message(self, ws, message):
        temp =json.loads(message)
        if 'new player' in temp:
            self.players = temp.get('players')
        elif 'start_status' in temp:
            self.status = temp.get('start_status')
        elif "state" in temp and "message" in temp:
            self.status = temp.get('message')
        elif "players status" in temp:
            self.players = temp.get('status')
        elif "current turn" in temp:
            self.current_turn = temp.get('current_turn')
        elif "dice result" in temp:
            self.dices_result = temp.get('dice_result')

    def on_error(self, ws, error):
        print(error)
    
    def on_open(self, ws):
        def run(*args):
            ws.send(json.dumps({'username':self.username}))
        Thread(target=run).start()
    
    def send(self, msg):
        def sending(*args):
            self.ws.send(json.dumps(msg))
        Thread(target=sending).start()

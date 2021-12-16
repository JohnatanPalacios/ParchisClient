import json
import websocket
from threading import Thread


class Client:
    def __init__(self, username):
        self.username = username
        self.port = '8081'
        self.data = dict()
        self.iniciar = False
        self.turno = None
        self.jugadores = list()
        self.estado_jugadores = list()
        self.resultado_dados = list()
        self.liberar_fichas = False
        self.color = None
        #### create conexion ####
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp("ws://localhost:" + self.port + "/",
                                            on_open = self.on_open,
                                            on_message = self.on_message,
                                            on_error = self.on_error,
                                            on_close = self.on_close)
        self.thread = Thread(target=self.ws.run_forever)
        self.thread.daemon = True
        self.thread.start()
    
    def on_message(self, ws, message):
        self.data = json.loads(message)
        if self.data["type"] == "state":
            if self.data["message"] == "The game has started":
                self.iniciar = True
        if self.data["type"] == "current turn":
            self.turno = self.data["message"]
        if self.data["type"] == "new player":
            self.jugadores = self.data["players"]
        if self.data["type"] == "players status":
            self.estado_jugadores = self.data["status"]
        if self.data["type"] == "dice result":
            self.resultado_dados = self.data["message"]
        if self.data["type"] == "exit jail":
            self.liberar_fichas = self.data["message"] # "Your pawns have exit jail"
        if not self.color:
            for j in self.jugadores:
                if self.username == j["username"]:
                    self.color = j["color"]

    def on_error(self, ws, error):
        print(error)
    
    def on_close(self, ws):
        print("**Disconnected**")
    
    def on_open(self, ws):
        def run(*args):
            ws.send(json.dumps({'username':self.username}))
        Thread(target=run).start()
    
    def send(self, msg):
        self.ws.send(json.dumps(msg))

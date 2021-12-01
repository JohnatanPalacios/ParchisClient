import json
import websocket
from threading import Thread


class Client:
    def __init__(self, username):
        self.username = username
        self.port = '8081'
        self.data = dict()
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
        # def sending(*args):
        #     self.ws.send(json.dumps(msg))
        # Thread(target=sending).start()

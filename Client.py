import json
import websocket
from threading import Thread


class Client:
    def __init__(self, port='8081', username=''):
        self.username = username
        self.port = port
        self.ws = None
        self.data = dict()
        self.start_status = None
        self.operation = None
        self.players = list()
        self.start()
    
    def start(self):
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp("ws://localhost:" + self.port + "/",
                                            on_open = self.on_open,
                                            on_message = self.on_message,
                                            on_error = self.on_error,
                                            on_close = self.on_close)
        self.ws.run_forever()

    def on_message(self, ws, message):
        temp =json.loads(message)
        if 'players' in temp: self.players = [p.get('username') for p in temp.get('players')]
        elif 'start_status' in temp: self.start_status = temp.get('start_status')
        self.data = temp
        print(message)

    def on_error(self, ws, error):
        print(error)
        print('Reconectando')
        #self.start()

    def on_close(self, ws):
        print("#----- Closed -----#")
    
    def on_open(self, ws):
        def run(*args):
            ws.send(json.dumps({'username':self.username}))
        Thread(target=run).start()
    
    def send(self, value):
        msg = json.dumps(value)
        def sending(*args):
            if 'start_status' in value and not self.start_status: self.ws.send(msg)
        Thread(target=sending).start()





# from websocket import create_connection
# import _thread
# class Client:
#     def __init__(self, port='8081'):
#         self.port = port
#         self.data = dict()
#         self.ws = create_connection("ws://localhost:" + self.port + "/")
#         self.start_status = None
#         self.operation = None
#         self.players = list()

#     def conn(self, data=False):
#         if data:
#             self.ws.send(json.dumps(data))
#             self.data = json.loads(self.ws.recv())
#             try:
#                 self.players = [p.get('username') for p in self.data.get('players')]
#             except:
#                 pass
#         else:
#             try:
#                 self.players = [p.get('username') for p in self.data.get('players')]
#             except:
#                 pass
#             self.data = json.loads(self.ws.recv())

#     def getGameState(self):
#         self.conn()
#         return self.data.get('state')
    
#     def setGameStart(self):
#         if not self.start_status: self.conn({"start_status":"true"})

#     def setUsername(self, username):
#         self.conn({"username": username})
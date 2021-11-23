import json
from websocket import create_connection


class Client:
    def __init__(self, port='8081'):
        self.port = port
        self.data = dict()
        self.ws = create_connection("ws://localhost:" + self.port + "/")

        self.start_status = None
        self.operation = None
        self.players = list()

    def conn(self, data=False):
        if data:
            self.ws.send(json.dumps(data))
            self.data = json.loads(self.ws.recv())
            try:
                self.players = [p.get('username') for p in self.data.get('players')]
            except:
                pass
        else:
            try:
                self.players = [p.get('username') for p in self.data.get('players')]
            except:
                pass
            self.data = json.loads(self.ws.recv())

    def getGameState(self):
        self.conn()
        return self.data.get('state')
    
    def setGameStart(self):
        if not self.start_status: self.conn({"start_status":"true"})

    def setUsername(self, username):
        self.conn({"username": username})

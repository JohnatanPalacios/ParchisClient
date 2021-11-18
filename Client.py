import json
import asyncio
from websockets import connect


class Client:
    def __init__(self, port='8081'):
        self.port = port
        self.data = dict()
        asyncio.run(self.conn())

    async def conn(self, data=False):
        async with connect("ws://localhost:" + self.port + "/") as ws:
            if data:
                await ws.send(json.dumps(data))
                self.data = json.loads(await ws.recv())
            else:
                self.data = json.loads(await ws.recv())
    
    def countPlayers(self):
        asyncio.run(self.conn())
        print('\n-----COUNT PLAYERS-----\n{}'.format(self.data))
        return len(self.data.get('players'))
    
    def getPlayers(self):
        asyncio.run(self.conn())
        print('\n-----DATA PLAYERS-----\n{}'.format(self.data))
        return [p.get('username') for p in self.data.get('players')]
    
    def getGameState(self):
        asyncio.run(self.conn())
        return self.data.get('state')
    
    def setGameStart(self):
        asyncio.run(self.conn({"start_status":"true"}))

    def setNickname(self, username):
        asyncio.run(self.conn({"username": username}))
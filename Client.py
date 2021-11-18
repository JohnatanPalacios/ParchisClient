import json
from websocket import create_connection


class Client:
    def __init__(self, port='8081'):
        self.port = port
        self.data = dict()
        self.ws = create_connection("ws://localhost:" + self.port + "/")

    def conn(self, data=False):
        if data:
            self.ws.send(json.dumps(data))
            self.data = json.loads(self.ws.recv())
        else:
            self.data = json.loads(self.ws.recv())
    
    def countPlayers(self):
        self.conn()
        print('--> Count Players: {}'.format(len(self.data.get('players'))))
        return len(self.data.get('players'))
    
    def getPlayers(self):
        self.conn()
        return [p.get('username') for p in self.data.get('players')]
    
    def getGameState(self):
        self.conn()
        return self.data.get('state')
    
    def setGameStart(self):
        self.conn({"start_status":"true"})

    def setUsername(self, username):
        self.conn({"username": username})






# import json
# import asyncio
# from websockets import connect


# class Client:
#     def __init__(self, port='8081'):
#         self.port = port
#         self.data = dict()
#         # asyncio.run(self.conn())
#         asyncio.get_event_loop().run_until_complete(asyncio.wait([self.conn()]))

#     async def conn(self, data=False):
#         async with connect("ws://localhost:" + self.port + "/") as ws:
#             if data:
#                 await ws.send(json.dumps(data))
#                 self.data = json.loads(await ws.recv())
#                 print('\n\n{}\n\n'.format(self.data))
#             else:
#                 self.data = json.loads(await ws.recv())
    
#     def countPlayers(self):
#         asyncio.run(self.conn())
#         print('\n-----COUNT PLAYERS-----\n{}'.format(self.data))
#         print(self.data.get('players'))
#         return len(self.data.get('players'))
    
#     def getPlayers(self):
#         asyncio.run(self.conn())
#         print('\n-----DATA PLAYERS-----\n{}'.format(self.data))
#         return [p.get('username') for p in self.data.get('players')]
    
#     def getGameState(self):
#         asyncio.run(self.conn())
#         return self.data.get('state')
    
#     def setGameStart(self):
#         asyncio.run(self.conn({"start_status":"true"}))

#     def setUsername(self, username):
#         asyncio.run(self.conn({"username": username}))

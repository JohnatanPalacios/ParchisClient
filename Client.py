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

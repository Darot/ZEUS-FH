__author__ = 'Dominik Krichbaum'

from twisted.internet import reactor
from autobahn.asyncio.websocket import *
from sys import getsizeof
from os import urandom



class WebsocketClient(WebSocketClientProtocol):

    def onOpen(self):
        print("Connection established")
        for i in range(0,10):
            msg = urandom(2)
            print(str(getsizeof(msg)))
            self.sendMessage(msg, binary=0)

if __name__ == '__main__':
    factory = WebSocketClientFactory("ws://localhost:9000", debug=False)
    factory.protocol = WebsocketClient
    connectWS(factory)
    reactor.run()
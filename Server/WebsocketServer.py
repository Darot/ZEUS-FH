__author__ = 'Dominik Krichbaum'

from twisted.internet import reactor
from autobahn.twisted.websocket import *
from sys import getsizeof


class WebsocketNamespace(WebSocketServerProtocol):

    connection_count = 0

    def onConnect(self, request):
        print("Client connecting: {}".format(request.peer))


    def onOpen(self):
        WebsocketNamespace.connection_count+=1
        print("Connection established. Count of connections: " + str(WebsocketNamespace.connection_count))

    def onMessage(self, msg, binary):
        print("message received: {} bytes".format(msg))
        #print(str(getsizeof(msg)))


    def onClose(self, wasClean, code, reason):
        print reason

def run_ws(port, status, gsize, gdelay, *args):
    factory = WebSocketServerFactory("ws://localhost:9000", debug = False)
    factory.protocol = WebsocketNamespace
    reactor.listenTCP(9000, factory)
    status.add_server("WS", str(port))
    reactor.run(installSignalHandlers=0)
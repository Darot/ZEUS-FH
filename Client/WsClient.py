__author__ = 'Dominik Krichbaum'


from twisted.internet import reactor
from autobahn.twisted.websocket import *
import sys
import time
import datetime

from sys import getsizeof
from sys import getsizeof
from os import urandom

#Globals
flow = 0
size = 0
delay = 0
endurance = 0
progress = 0

class WebsocketClient(WebSocketClientProtocol):

    def onOpen(self):
        print("Connection established")
        global flow
        global size
        global progress
        global endruance
        self.flow = flow
        self.size = size
        self.delay = delay
        self.endurance = endurance
        self.progress = progress
        print self.endurance
        if self.endurance == 0:
            self.sendMsg()
        else:
            self.sendMsg_time()

    def sendMsg(self):
        # This method is use to send messages by count
        for i in range(self.flow):
            time.sleep(self.delay)
            self.sendMessage(bytes(self.size), bin(0))
            self.progress.update_progress()
        self.sendClose(1000, "")

    def sendMsg_time(self):
        #this method is used to send messages by time
        stop = time.time() + endurance
        self.progress.set_starttime(datetime.datetime.now())
        self.progress.set_endurance(self.endurance)
        while time.time() < stop:
            time.sleep(self.delay)
            self.sendMessage(bytes(self.size), bin(0))
            self.progress.update_progress_time(datetime.datetime.now())
        self.sendClose(1000, "")

    def onMessage(self, payload, isBinary):
        print payload

    def onClose(self, wasClean, code, reason):
        print "Transmission Complete"

def run_ws(gflow, gsize, gprogress, gendurance, *args):
    #this is a HACK!
    #this function is used to run a Websocket server in a new thread
    #this is not the normal way you should do this!!!
    global flow
    flow = gflow
    global size
    size = gsize
    global progress
    progress = gprogress
    global endurance
    endurance = gendurance
    factory = WebSocketClientFactory("ws://localhost:9000", debug=False)
    factory.protocol = WebsocketClient
    connectWS(factory)
    reactor.run()